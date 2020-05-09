Reverse Proxy
=============

Although a basic Tryton system can be run using just the official Tryton Docker
image and a PostgreSQL database, using a reverse proxy such as Nginx_ can help
improve the performance and security of your system.

Here we are using Nginx in front of the Tryton server, and allowing it to
handle the incoming connections and serve the static content.  This filters
out the requests that don't need to be handled by the Tryton server freeing
it up to deal with the requests that only it can process.


Update the ``docker-compose.yaml`` File
---------------------------------------

Add the ``nginx`` Service
^^^^^^^^^^^^^^^^^^^^^^^^^

An ``nginx`` service needs to be added to the ``docker-compose.yaml`` file:

.. code-block::

    version: "3.5"

    services:
        ...
        nginx:
            image: nginx:1.17
            restart: always
            environment:
              - TZ=Europe/London
            volumes:
              - ./nginx-config:/etc/nginx/conf.d:ro
              - tryton-www-static-data:/var/www/static/tryton:ro
            ports:
              - "127.0.0.1:80:80"
            depends_on:
              - tryton
        ...

.. note::

    Set the ``TZ`` environment variable based on your location, so Nginx logs
    have the correct time in them.  Pick an appropriate ``TZ database name``
    from the `list of timezones`_.

Add a Shared Volume for Static Content
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``nginx`` service that was defined above will serve static content from
the ``tryton-www-static-data`` Docker volume.  This volume needs to defined and
added to the ``tryton`` service so the data can be shared between the
``tryton`` and ``nginx`` services, so define the volume:

.. code-block::

    version: "3.5"

    ...

    volumes:
        ...
        tryton-www-static-data:
        ...

and add it to the ``tryton`` service:

.. code-block::

    version: "3.5"

    services:
        tryton:
            volumes:
                ...
              - tryton-www-static-data:/var/lib/trytond/www
                ...

.. note::

    Unlike the ``tryton-data`` and ``tryton-postgres-data`` volumes, because
    the ``tryton-www-static-data`` volume is not external it will be created
    automatically when Docker Compose starts the services.

Only Allow Connection via Nginx
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Now that connections to your Tryton system will be through Nginx instead of
directly to the ``tryton`` service, you need to change the ``ports`` section of
the ``tryton`` service to an ``expose`` section instead, so change this:

.. code-block::

    version: "3.5"

    services:
        tryton:
            ...
            ports:
              - "127.0.0.1:8000:8000"
            ...

to this:

.. code-block::

    version: "3.5"

    services:
        tryton:
            ...
            expose:
              - "8000"
            ...

Configure Tryton Service
^^^^^^^^^^^^^^^^^^^^^^^^

You also need to let your ``tryton`` service know that it is behind a reverse
proxy by setting the ``num_proxies`` configuration option from the ``web``
section:

.. code-block::

    version: "3.5"

    services:
        tryton:
            ...
            environment:
                ...
              - TRYTOND_WEB__NUM_PROXIES=1
                ...


Create the Nginx Configuration
------------------------------

The ``nginx`` service has been setup to use configuration settings from a
``nginx-config`` directory that is in the same directory as your
``docker-compose.yaml`` file, so create this directory:

.. code-block:: bash

    mkdir nginx-config

Inside this config directory you need to create several files that will
provide the configuration for the Nginx web server, these files are:

* ``gzip.conf``:

    .. code-block::

        #
        # conf.d/gzip.conf - gzip settings
        #

        gzip on;
        gzip_vary on;
        gzip_proxied any;
        gzip_types text/plain text/css text/xml text/javascript application/x-javascript application/xml;
        gzip_min_length 10240;

* ``misc.conf``:

    .. code-block::

        #
        # conf.d/misc.conf - miscellaneous http settings
        #

        tcp_nopush on;
        tcp_nodelay on;

        types_hash_max_size 2048;

        server_names_hash_bucket_size 64;

        server_name_in_redirect on;
        server_tokens off;

* ``tryton.conf``:

    .. code-block::

        #
        # conf.d/tryton.conf - tryton site file
        #

        upstream tryton {
            server tryton:8000;
        }

        server {
            server_name localhost;
            listen 80 http2;

            root /var/www/static/tryton;

            location / {
                if ($request_method = GET) {
                    rewrite ^ /index.html last;
                }

                proxy_pass http://tryton;

                proxy_set_header Host $http_host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
                proxy_set_header X-Forwarded-Host $server_name;

                proxy_read_timeout 1200s;

                client_max_body_size 0;
            }

            location ~ ^/(bower_components|dist|images|index.html|locale)/ {
                expires max;
            }
        }


Connect to your Tryton System
-----------------------------

With this setup you can now connect to your Tryton system from the computer it
is running on at http://localhost/.


Allow Secure Remote Connections
-------------------------------

With all the configurations so far any information sent to, or retrieved from,
your Tryton system will have been over unencrypted connections.  This is not
a problem if you can only access your Tryton system from the computer that it
is setup on, which is how all the examples so far have been configured.

For remote connections it is much better and far more secure to use encrypted
connections.  To do this we will need to setup a private key and certificate,
and use these with an updated Nginx configuration to force all connections to
be over encrypted channels.

Create the Certificate and Key
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The SSL connections to your service will use `public-key cryptography`_ to
provide secure communication between your Tryton system and the computer
accessing it.  For this to work you need to get, or generate, a public
certificate and a private key.  At this point we will also download some
`Diffie-Hellman`_ parameters as well for use by your computer when setting up
encrypted channels.

The first thing to do is create a directory to put these files in, so create
a directory called ``ssl`` inside your ``nginx-config`` directory, and
ensure that it is only readable and writable by your user e.g.:

.. code-block:: bash

    mkdir nginx-config/ssl
    chmod 0700 nginx-config/ssl

There are quite a few different ways of obtaining a certificate for your server
a few of them are listed here:

* Self-Signed Certificate:
  You can generate a self-signed certificate by using the ``openssl`` command.
  Ensure you have installed the package that provides the ``openssl`` command
  on your system, then run:

  .. code-block:: bash

      cd ssl
      openssl req -x509 -newkey rsa:4096 -keyout privkey.pem -out fullchain.pem -days 365 -nodes

  .. note::

      When running this command it will prompt you to enter some information
      about the server and service that the certificate is for.  This
      information will be part of the certificate that is generated, so
      fill it in as best as you can, ensuring that the commonName is set to
      your computer's name.

* Use the Snakeoil certificate (Debian/Ubuntu only):
  If you are running Docker on Debian or Ubuntu, then you can use the
  snakeoil certificate and private key that are provided by the ``ssl-cert``
  package to provide a self-signed certificate without having to manually
  generate it yourself.  Ensure the package is installed by running:

  .. code-block:: bash

      sudo apt-get install --yes ssl-cert

  Then copy the snakeoil certificate and key to the ``ssl`` directory.

  .. code-block:: bash

      cp /etc/ssl/certs/ssl-cert-snakeoil.pem nginx-config/ssl/fullchain.pem
      sudo cp /etc/ssl/private/ssl-cert-snakeoil.key nginx-config/ssl/privkey.pem

* LetsEncrypt:
  If your computer is accessible from the Internet, then the best option will
  probably be to use the LetsEncrypt_ service to generate your certificate.
  Once you have created your certificate and private key then you should copy
  the ``fullchain.pem`` and ``privkey.pem`` files to the ``ssl`` directory.

* Buy a certificate from a Certificate Authority:
  If you really wanted to you could also buy a certificate from a
  `Certificate Authority`_.  This is only listed as it's another option,
  however if buying a certificate would work for you then so would using
  LetsEncrypt_, so save yourself some money and do that instead.

.. note::

    If you generated a self-signed certificate, or used the snakeoil
    certificate, then you will need to configure the client to allow
    connections to your Tryton system.  This is because the certificate has
    not been signed by a recognised `Certificate Authority`_ (it is self
    signed).

    In this case, when using the web client, you will get a warning from your
    browser the first time you connect.  You can either configure your browser
    to not show this message again, or install the ``fullchain.pem`` 
    certificate within the browser.

    When using the Desktop client you will need to put the contents of the
    ``fullchain.pem`` file in the ``ca_certs`` file in the Desktop client's
    config directory (``~/.config/tryton/5.4/``, or if you are using Windows
    ``%APP_DATA%\.config\tryton\5.4\``).  You may also need to remove the
    entry for the server from the ``known_hosts`` file if you have
    unsuccessfully tried to connect to this server before, or have updated
    the server's certificate.

The other file that you need to create is the ``dhparam.pem`` file.
The contents for this file is available at
https://ssl-config.mozilla.org/ffdhe2048.txt,
so open the link in your browser and copy its contents into the 
``nginx-config/ssl/dhparam.pem`` file.

Modify the ``docker-compose.yaml`` File
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Add the https port to the nginx service, and remove the "127.0.0.1:" from the
start of the http port:

.. code-block::

    version: "3.5"

    services:
        nginx:
            ...
            ports:
              - "80:80"
              - "443:443"
            ...

Update the Nginx Configuration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You need to add an ``ssl.conf`` configuration file to the ``nginx-config``
directory, and update the ``tryton.conf`` file to ensure all connections are
encrypted:

* ``ssl.conf``:

    .. code-block::

        #
        # conf.d/ssl.conf - ssl configuration
        #

        # Intermediate configuration - see https://ssl-config.mozilla.org/#server=nginx&server-version=1.17.0&config=intermediate
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256:DHE-RSA-AES256-GCM-SHA384;
        ssl_prefer_server_ciphers off;

        # ssl session settings
        ssl_session_timeout 1d;
        ssl_session_cache shared:SSL:10m;
        ssl_session_tickets off;

        # Diffie-Hellman parameters
        ssl_dhparam /etc/nginx/conf.d/ssl/dhparam.pem;

        # HSTS (63072000 seconds ~= 2 years)
        add_header Strict-Transport-Security "max-age=63072000" always;

        # OCSP Stapling - fetch OCSP records from URL in ssl_certificate and cache them
        ssl_stapling on;
        ssl_stapling_verify on;

        resolver 127.0.0.11;

* ``tryton.conf``:

    .. code-block::

        #
        # conf.d/tryton.conf - tryton site file
        #

        upstream tryton {
            server tryton:8000;
        }

        server {
            server_name localhost;
            listen 80;

            return 301 https://$server_name$request_uri;
        }

        server {
            server_name localhost;
            listen 443 ssl http2;

            ssl_certificate /etc/nginx/conf.d/ssl/fullchain.pem;
            ssl_certificate_key /etc/nginx/conf.d/ssl/privkey.pem;

            root /var/www/static/tryton;

            location / {
                if ($request_method = GET) {
                    rewrite ^ /index.html last;
                }

                proxy_pass http://tryton;

                proxy_set_header Host $http_host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
                proxy_set_header X-Forwarded-Host $server_name;

                proxy_read_timeout 1200s;

                client_max_body_size 0;
            }

            location ~ ^/(bower_components|dist|images|index.html|locale)/ {
                expires max;
            }
        }


.. include:: /common/global.rst

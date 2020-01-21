Quick Install Guide
===================

There are a few different ways of getting Tryton installed on your system.
The aim of the quick install guide is to get you up and running with Tryton
on a local system with the minimum of fuss.  It uses docker to run the
official tryton docker image, and is suitable for trying out Tryton on your
local computer and network.  For more advanced setups, and for accessing
Tryton from external networks you can look at the 
:ref:`administration/installation/database/index:Database Installation`,
:ref:`administration/installation/server/index:Server Installation`, and
:ref:`administration/installation/client/index:Client Installation`
instructions.


Install Docker
--------------

To be able to run Tryton using Docker you first need to install Docker on your
system.  How you do this will depend on the Operating System or distribution
that you are running.  The best source of information for this is the
`official Docker Documentation`_, and the installation guides for each
different operating system and distribution:

* `Docker Desktop for Windows 10`_
* `Docker Desktop for macOS`_
* Linux:

  * `Docker Engine - Community for CentOS`_
  * `Docker Engine - Community for Debian`_
  * `Docker Engine - Community for Fedora`_
  * `Docker Engine - Community for Ubuntu`_

.. note::

    If you have put your user in the ``docker`` group you may not need to use
    ``sudo`` to run the commands in the following examples, but take care
    because the ``docker`` group grants privileges that are equivalent to the
    ``root`` user, and so can have an impact on the security of your system.


Create Volumes for your Data
----------------------------

.. include:: /common/installation/docker-create-volumes.rst


Start the Database
------------------

Once you have got Docker installed and setup you are then ready to start up
the containers that you need for a Tryton system.  The first thing to do is
to start up the PostgreSQL database server:

.. code-block:: bash

    export POSTGRES_PASSWORD=$( \
        cat /dev/urandom | \
        tr -dc 'a-zA-Z0-9-_' | \
        head -c 16 )
    echo "POSTGRES_PASSWORD (save this somewhere safe): ${POSTGRES_PASSWORD}"
    sudo docker run \
        --name tryton-postgres \
        --env PGDATA=/var/lib/postgresql/data/pgdata \
        --env POSTGRES_DB=tryton \
        --env POSTGRES_PASSWORD=${POSTGRES_PASSWORD} \
        --mount source=tryton-postgres-data,target=/var/lib/postgresql/data \
        --detach \
        postgres:12

.. note::

    You should make sure you make a note of the ``POSTGRES_PASSWORD``.  If you
    shutdown your Tryton system then you will need to make sure the password
    is defined in the environment before trying to start your Tryton system
    back up.

    .. code-block:: bash

        export POSTGRES_PASSWORD="replace this text with the POSTGRES_PASSWORD"

.. note::

    This should automatically download the postgres database server image from
    docker if you haven't got it on your system.


Initialise the Database
-----------------------

After the database server is up and running, you can use the 
:ref:`administration/services/trytond-admin:trytond-admin` tool to 
initialise it ready for use by the Tryton server:

.. code-block:: bash

    sudo docker run \
        --link tryton-postgres:postgres \
        --interactive --tty --rm \
        tryton/tryton:5.4 \
        trytond-admin -d tryton --all

When running this command, after a short while, you will be prompted to enter
the email address and password for the Tryton ``admin`` user.


Start the Tryton Server
-----------------------

With the database setup and ready, you can now start the Tryton server:

.. code-block:: bash

    sudo docker run \
        --name tryton \
        --publish 127.0.0.1:8000:8000 \
        --link tryton-postgres:postgres \
        --mount source=tryton-data,target=/var/lib/trytond/db \
        --detach \
        tryton/tryton:5.4


Connect to the Tryton Server
----------------------------

.. include:: /common/installation/connect-tryton.rst


Next Steps
----------

Although you will now have a running Tryton system, which is perfectly usable
as it is, there are a few things that you should probably consider looking
into:

* You will want to have a look through the available
  :ref:`administration/system/modules:Modules`,
  so you can get a good idea of what modules you need to activate for the
  functionality that you require.

* You may want to use ``docker-compose`` to manage your setup, it makes
  managing and controlling your setup easier, if so take a look at the
  :ref:`administration/installation/docker-compose/index:Docker Compose Install Guide`
  instructions.  You can use these instructions at any point in the future to
  update your setup so it can be managed using Docker Compose.

* If you decide to use just docker to run Tryton then you will probably want
  to become more familiar with it, so that you know how to manage docker
  containers using the `docker container command`_.

* Backing up your data is important, and this setup places your data in two
  docker volumes (``tryton-postgres-data`` and ``tryton-data``).
  The `docker volume inspect command`_ allows you to find where this data is
  stored on your system.  The
  :ref:`administration/system/data/index:Data Management` section contains
  further information on what data from you system is stored where, and how
  to back it up.

* If you need to access your Tryton system from different computers, then there
  are a couple of options.

  You can run you Tryton system behind a reverse proxy such as Nginx_, but be
  sure to setup ssl/https connections to it.  This can be easier to setup and
  manage if you are using
  :ref:`Docker Compose <administration/installation/docker-compose/index:Docker Compose Install Guide>`,
  and there are
  :ref:`specific instructions <administration/installation/docker-compose/proxy:Reverse Proxy>`
  for this.

  A simpler option is to allow connection to your Tryton system from anywhere
  by changing the line ``--publish 127.0.0.1:8000:8000`` to
  ``--publish 8000:8000`` when starting your Tryton system.

  .. warning::

      If you do not configure your Tryton system to use
      :ref:`administration/configuration/options:ssl`, any connections to it
      will not be secure.  Other people will be able to intercept and view any
      data, including things like login passwords and other sensitive
      information, that get sent to and from your Tryton system.

      Never do this without ssl enabled if your system is available across the
      internet, it really is a very bad idea.


.. include:: /common/global.rst

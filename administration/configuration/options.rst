Configuration Options
=====================

The Tryton server, and it's tools and services, are configured by setting
configuration options.  The available configuration options are listed here.


Sections
--------

The configuration file is split up into different sections.  Each section
contains configuration options that control the behaviour of a different
part of Tryton.


web
^^^

The web section is used to configure the networking and web settings used
by the server and services.

listen
    This configuration option is used to define the host, or ip address, and
    port that the server should listen on.

    By default, when started, the server listens on ``localhost:8000``.

hostname
    This is the hostname of the server that the ``trytond`` service is running
    on.

    If this value is not specified, then it defaults to the fully qualified
    domain name of the local host.

root
    This allows you to configure the path that is used when tryton serves any
    http GET requests.

    By default this is set to the ``www`` directory inside the home directory
    of the user that is running ``trytond``.

num_proxies
    This allows you to specify the number of proxy servers that are in front
    of the trytond server.  When Tryton is running behind proxy servers it
    may see the request as coming from the server rather than the real client.
    The num_proxies configuration allows it to compensate for this.

    .. caution::

        This should only be applied if Tryton is actually behind a proxy, and
        should be carefully set with the correct number of proxies that are
        chained in front of it.  Not setting this value correctly can be a
        security issue as Tryton may end up trusting headers from the client
        instead of the proxy.

    The default number of proxies is ``0``.

cache_timeout
    This is the cache_timeout value, in seconds, that is used in HTTP headers.

    The cache timeout defaults to ``43200`` seconds (12 hours).

cors
    This option allow you to specify a list of origins that are allowed for
    `Cross-Origin Resource Sharing`_.


database
^^^^^^^^

The database section allows you to configure the settings and connections to
the database.

uri
    This is the uri used to connect to the SQL database.  The URI follows
    the RFC-3986_ specification, and normally is of the form:

    .. ::

        database://username:password@host:port/

    Connections to PostgreSQL databases can be done over TCP/IP and Unix
    domain sockets, here are a few examples.

    .. code:: ini

        # Connect to a local PostgreSQL database over tcp/ip
        uri = postgresql://user:password@localhost:5432/

    .. code:: ini

        # Connect to a local PostgreSQL database using a socket
        uri = postgresql:///?host=/var/lib/postgresql

    SQLite databases can be connected to using:

    .. code:: ini

        # Connection to an SQLite database
        uri = sqlite:///path/to/tryton/db.sqlite

path
    This is the path to the directory where Tryton stores data files such as
    attachments, and is where any sqlite databases are stored.

    The default path is the ``db`` directory inside the home directory of the
    user that is running ``trytond``.

    .. important::

        The user that is running ``trytond`` must have write access to the
        path directory, otherwise Tryton will not work correctly.

class
    The class setting allows you to specify an alternative class to use when
    saving and retrieving data files.

    By default the class that is used is Tryton's build in ``FileStore`` class
    which stores files inside the directory specified by the ``path`` option
    above.

list
    This indicates whether, when queried, the server is allowed to return a
    list of available databases it can connect to.  Set this to ``False`` to
    stop the server from listing it's available databases.

    Defaults to ``True``.

retry
    This specifies the number of retries to attempt when there is a problem
    performing a database operation.

    The default number of retries is ``5``.

language
    This is the language used on the database, and is the main language any
    translations are against.

    The default language is ``en``.

minconn
    This is the minimum number of connections that should be keep open to the
    database.

    The default minimum number of connections to the database is ``1``.

maxconn
    This is the maximum number of connections that should be opened to the
    database.

    The default maximum number of connections to the database is ``64``.

timeout
    This is the length of time, in seconds, that a database connection will
    remain unused and open before it is closed.

    This defaults to ``1800`` seconds (30 minutes).


request
^^^^^^^

The configuration options in the request section allow you to configure the
maximum size of requests that the server will handle.

max_size
    This is the maximum size of a request from an unauthenticated user.  Set
    this to ``0`` to allow requests of any size.

    The default maximum size of an unauthenticated request is 2MB.


max_size_authenticated
    This is the maximum size of a request from an authenticated user.  Set
    this to ``0`` to allow requests of any size.

    The default maximum size of an authenticated request is 2GB.


cache
^^^^^

The settings in this section allow you to adjust the settings that relate to
the various caches used by the Tryton services.

.. note::

    Changing these can improve the performance of your server at the expense
    of greater memory usage, but this trade-off is very dependant on the
    specific load on your server.

.. tip::

    Normally it is best to leave these cache settings on the default values,
    this will provide good performance without excessive memory usage for a
    large range of usage scenarios.

class
    This is the name of an alternative class to use for caching data instead
    of using Tryton's in memory cache.

    If this is not specified then by default Tryton's in memory cache is used.

model
    This is the number of different models that are kept in the cache for each
    transaction.

    This defaults to ``200`` models.    

record
    This is the default number of records that are kept in the record caches.

    .. note::

        Modules can override this for specific operations

    This defaults to ``2000`` records.

field
    For fields are loaded in an ``eager`` manner this specifies how many fields
    get loaded.

    This defaults to ``100`` fields.

clean_timeout
    Once the cache has been cleaned this is the minimum time that should elapse
    before the cache is cleaned again.  If this is set to ``0`` then cache
    synchronisation between processes will be done using channels, if the
    back-end supports them.

    By default this is set to ``300`` seconds.


queue
^^^^^

This section is used to configure the behaviour of the
:ref:`administration/system/queue:Task Queue` and the
:ref:`administration/services/trytond-worker:trytond-worker` processes.

worker
    This option is used to enable the asynchronous processing of tasks.  If
    this value is set to ``True`` then any tasks designed to use the task queue
    will be processed by a separate worker process.

    The default value for this option is ``False``.


table
^^^^^

This section allows you to override the default names that are generated for
tables in the database.

.. note::

    Normally you will not need to adjust the table names.
    This configuration option is for the times when you want to use a database
    that limits the length of table names.

.. code:: ini

    [table]
    ir.action.act_window.domain = ir_window_domain
    ir.model.field.access = ir_field_access


ssl
^^^

These are the SSL_ settings, these are required to allow direct SSL connections
to the server.

privatekey
    This option allows you to set the path to the server's private key.

    .. note::

        Providing a value for the private key will make the server attempt to
        use SSL for all network protocols.

certificate
    This is the path to the server's certificate, and is required to be able to
    use SSL connections.


email
^^^^^

The settings in the email section allow you to configure how Tryton sends
emails out.

uri
    This is the URI for the SMTP server that should be used to send emails.
    The URI follows the SMTP-URL_ specification, with the exception of the
    protocol which is is extended to allow it support SMTP over SSL
    (use ``smtps``) and STMP with STARTTLS (use ``smtp_tls``) connections.

    You can also configure some additional parameters in the URI.

    local_hostname
        This is used as the fully qualified domain name of the local
        host in the ``HELO``/``EHLO`` commands.  If this parameter is not
        specified then it defaults to the local host's fully qualified domain
        name.

    timeout
        This is the number of seconds before a blocking operation will give
        up and raise a ``socket.timeout``.  If this parameter is not specified
        then the default timeout for the socket will be used.

from
    This is the from address that is used on emails that are sent by Tryton.


session
^^^^^^^

The settings in this section control how users authenticate and login to the
system, and when they get logged out.

authentications
    This is a comma separated list of methods to use for authenticating a
    user to the system.  Extra modules can add additional authentication
    methods.

    The available authentication methods are:

    password
        This authentication method checks a password entered by the user
        against a previously stored and encrypted version of the password.

    The default authentication method is ``password``.

max_age
    This is the time in seconds that a session is valid for.

    The default max age is ``2592000`` seconds (30 days).

timeout
    This is the number of seconds without activity before a session is no
    longer considered to be fresh.  It is also used with the max_attempt
    options to limit the login attempts in a set period of time.

    The default timeout is ``300`` seconds (5 minutes).

max_attempt
    This is the maximum number of authentication attempts that can be performed
    against a user account within *timeout* seconds.  If any more
    authentication attempts are made then the server simply responds with
    *Too Many Requests*.

    The maximum number of attempts is by default ``5``.

max_attempt_ip_network
    This is the maximum number of authentication attempts, from the same
    network, that can be performed against all user account within *timeout*
    seconds.  If any more authentication attempts are made from that network
    then the server simply responds with *Too Many Requests*.

    The maximum number of attempts from one network is by default ``300``.

ip_network_4
    This option is used with the ``max_attempt_ip_network`` option above.
    It should be set to the length of the network part of the IPv4 address, in
    bits.

    By default this is ``32`` bits, which means that each different IPv4
    address is considered to be a separate network for the
    ``max_attempt_ip_network`` limiting.

ip_network_6
    This option is used with the ``max_attempt_ip_network`` option above.
    It should be set to the length of the network part of the IPv6 address, in
    bits.

    By default this is ``56`` bits, which is the portion of the address that
    it is recommended should issued to a single home site.


password
^^^^^^^^

These settings allow you to help ensure that user passwords are more secure,
and setup how long before a password reset expires.

length
    This is the minimum acceptable length for a password.  Passwords that are
    shorter than this are considered to be too insecure.

    The default minimum password length is ``8`` characters.

forbidden
    The forbidden option allows you to specify a file that lists passwords that
    are unacceptable for use with the system.  The file should contain one
    forbidden password per line.

entropy
    This is minimum ratio of characters to non-repeating characters that is
    allowed.

    For example:

    ==========  ==============  ========================  ===============
     Password    Num of Chars    Num of Different Chars        Ratio
    ==========  ==============  ========================  ===============
     abcdEFGH               8                         8        1 (8 / 8)
     Password               8                         7    0.875 (7 / 8)
     TestTest               8                         4      0.5 (4 / 8)
    ==========  ==============  ========================  ===============

    This defaults to ``0.75``.

reset_timeout
    This is the time in seconds until a password reset expires, and will then
    need to be re-issued.

    This defaults to ``86400`` seconds (24 hours).

passlib
    This configuration option allows you to specify the location of an INI file
    that contains the configuration settings for the PassLib_ CryptContext_.
    This is the library that Tryton uses to encrypt the user passwords before
    they are stored in the database.

    If the passlib option is not set then by default Tryton will use the
    ``bcrypt`` algorithm if available, or ``pbkdf2_sha512`` if it is not.


attachment
^^^^^^^^^^

These settings control how attachments are handled by the system.

filestore
    This option allows you to decide whether attachments get saved in the
    database, or in the file store with other data files.  To use the database
    for attachments set this to ``False``.

    By default this option is set to ``True`` and attachments are stored in the
    file store.

store_prefix
    This option allows you to add a prefix to use with the file store.

    By default no prefix is set for attachments that are stored in the file
    store.


bus
^^^

The settings in this section deal with the bus and the communication channels
that it provides.

allow_subscribe
    This must be set to ``True`` to allow clients ta subscribe to channels on
    the bus.

    The default value is ``False`` which stops clients from subscribing to the
    bus.

url_host
    Setting this configuration option ensures that all requests to the bus are
    redirected to the to the specified host URL.

long_polling_timeout
    This is the time in seconds that a connection to a client is kept open
    when using the long polling for bus messages.

    The default long polling timeout is ``300`` seconds (5 minutes).

cache_timeout
    This is the number of seconds that a message should be kept by the queue
    before it is discarded.

    This defaults to ``300`` seconds (5 minutes).

select_timeout
    This is the timeout to use with the select system call used when listening
    on a channel.

    By default this is set to ``5`` seconds.

class
    This is the name of an alternative class to use for the bus instead
    of using Tryton's long polling bus.

    If this is not specified then by default Tryton's long polling bus is used.


html
^^^^

This section allows you to configure the settings for the html text editor.

src
    This should be set to the url that points to the TinyMCE_ text editor.

    This defaults to ``https://cloud.tinymce.com/stable/tinymce.min.js``.

plugins
    This is a space separated list of plugins for the TinyMCE editor to load.

    To override the plugins for a specific model use a configuration option of
    ``plugins-<model>``.  The plugins for a specific field can be overridden
    using a ``plugins-<model>-<field>`` configuration option.

    .. code:: ini

        [html]
        plugins = autolink
        plugins-ir.model = wordcount
        plugins-ir.model-example_field = emoticons

    By default no plugins are set.

css
    This is a JSON list of CSS files for the TinyMCE editor to load.

    To override the css files for a specific model use a configuration option
    of ``css-<model>``.  The css files for a specific field can be overridden
    using a ``css-<model>-<field>`` configuration option.

    By default no CSS files are specified.

class
    This is the body class to use with the TinyMCE editor.

    This can be overridden for a specific model, to do this use a
    configuration option of ``class-<model>``.  To override this setting for
    a specific field use a configuration option of ``class-<model>-<field>``.

    By default no body class is used.


.. include:: /common/global.rst

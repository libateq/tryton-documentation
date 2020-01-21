Logging
=======

While running, the Tryton
:ref:`administration/services/index:Tools and Services` output log messages
in order to provide an audit trail and log of the events that have happened
to the system.  The output location and amount of log messages that Tryton
generates can be configured in detail by setting the ``--logconf`` parameter.


Default Logging
---------------

By default, if no log configuration file is specified, Tryton writes only
``ERROR`` and ``CRITICAL`` messages to standard output.  Additional log
messages will be output for each ``--verbose`` flag that is set.
One ``--verbose`` flag enables ``WARNING`` messages as well, with two
``--verbose`` flags set ``INFO`` messages will also be included, and three
``--verbose`` flags will enable all of the previous log messages and ``DEBUG``
messages.


Configuration File
------------------

If you want to more control over what log messages are generated, and where
they are output to, then you will need to create a logging configuration file.

.. note::

    A complete guide to the logging `configuration file format`_ can be found
    in the Python_ documentation.    

The configuration file must contain sections called ``[loggers]``,
``[handlers]`` and ``[formatters]``.  Each of these sections should have a
``keys`` option that lists the names of the entities for that type.  For each
entity there should be another section in the file which is used to
configure the entity.  The entity section names are comprised of the type of
the entity followed by an underscore and the entity name.  So the root
logger should be listed in the ``[loggers]`` ``keys`` and is configured in a
section called ``[logger_root]``.

Some of the options that can be used when configuring logger entities are:

handlers
    This is a list of the handlers used by the logger.

level
    This is the level at which the logger will log messages.  Any messages
    that are at a lower level than this will be filtered out and will not be
    seen by the handlers that the logger uses.

The options that are available to configure handler entities are dependent on
the class of the handler, some of the common options are:

class
    The class defines how the log handler works, and therefore also defines
    where the log messages will be sent.

formatter
    This is the formatter to use with the log handler, and should be one of
    the formatters from the ``keys`` in the ``formatters`` section.

level
    This is the level at which the log handler will log messages.  Any messages
    that are at a lower level than this will be filtered out.

args
    These are the arguments to the handler when it is created.

When configuring formatters the main option of use is:

format
    This specifies what things are included in the message that is logged.
    This can include things like the time of the event (``%(asctime)s``), the
    log level of the message (``%(levelname)s``), and the actual message to
    log (``%(message)s``).


Example Config Files
--------------------

Here are a few example configuration files to give you an idea of some of the
logging options that are available.

To send the ``INFO``, and above, log messages to syslog (assuming you have
syslog running):

.. code:: ini

    [loggers]
    keys=root

    [logger_root]
    handlers=syslog
    level=INFO

    [handlers]
    keys=syslog

    [handler_syslog]
    class=SysLogHandler
    formatter=basic
    args=('/dev/syslog', 'local6')

    [formatters]
    keys=basic

    [formatter_basic]
    format=%(asctime)s:%(name)s:%(levelname)s: %(message)s

To log to ``INFO`` and above messages to the console, and ``DEBUG`` and higher
messages to a file:

.. code:: ini

    [loggers]
    keys=root

    [logger_root]
    handlers=screen,file
    level=NOTSET

    [handlers]
    keys=screen,file

    [handler_screen]
    class=StreamHandler
    formatter=simple
    level=INFO
    args=(sys.stdout,)

    [handler_file]
    class=handlers.TimedRotatingFileHandler
    interval=midnight
    backupCount=5
    formatter=complex
    level=DEBUG
    args=('logs/tryton.log',)

    [formatters]
    keys=simple,complex

    [formatter_simple]
    format=%(asctime)s %(name)s %(levelname)s: %(message)s

    [formatter_complex]
    format=%(asctime)s %(name)s %(levelname)s %(module)s : %(lineno)d - %(message)s


.. include:: /common/global.rst

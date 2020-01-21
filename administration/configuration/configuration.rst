Configuring the Server
======================

There are two main ways of setting the configuration options for the server and
other tools and services, either in one or more configuration files, or using
environment variables.

The available configuration options are listed in the
:ref:`administration/configuration/options:Configuration Options` section.


Configuration Files
-------------------

Configuration options can be set using one or more configuration files.
These files follow a simple INI file format with one or more sections each
containing the options and their values.

A section is started with a ``[section]`` header, and then is followed by the
``option = value`` entries.  Leading and trailing white space is removed from
the ``option`` and ``value``.  Comments can be included on their own line
preceded by a ``#`` or ``;`` symbol.

For example:

.. code:: ini 

    # Set the port the server will listen on
    [web]
    listen = localhost:8765


Environment
-----------

Tryton configuration options can also be set using environment variables.
This is especially useful when running Tryton inside a Docker container.

The environment variables should be named ``TRYTOND_SECTION__KEY``, with
``SECTION`` and ``KEY`` replaced with the section and configuration option
name respectively.

For example:

.. code:: bash

    # Set the port the server will listen on
    TRYTOND_WEB__LISTEN = localhost:8765

.. note::

    Take care to ensure that you use a double underscore ``__`` between the
    ``SECTION`` and ``KEY``.


.. include:: /common/global.rst


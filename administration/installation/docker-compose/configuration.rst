Configuration
=============

Tryton is fully compatible with being configured and used inside Docker
containers.  All of its
:ref:`administration/configuration/options:Configuration Options`
can be set using environment variables, although they all have sensible
default values.  See the
:ref:`administration/configuration/index:Configuration` section for more
detail on this.


Update the ``docker-compose.yaml`` File
-----------------------------------------

The best way of changing the configuration for your Docker services is to use
environment variables to set the values of the configuration options.  For
example, to change the minimum length of passwords you would set the ``length``
option in the ``password`` section using the ``TRYTOND_PASSWORD__LENGTH``
environment variable:


.. code-block::

    version: "3.5"

    services:
        tryton:
            ...
            environment:
                ...
              - TRYTOND_PASSWORD__LENGTH=12
                ...


.. note::

    If you change the environment for one of the Tryton services you almost
    always will want to change it for the other Tryton services (except for
    tryton-postgres service), so they are all running with the same
    configuration.


.. include:: /common/global.rst

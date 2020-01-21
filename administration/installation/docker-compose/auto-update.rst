Automatic Update Service
========================

Normally if an updated version of Tryton is released you will need to run the
:ref:`administration/services/trytond-admin:trytond-admin` tool to upgrade
your system so it works with the new version.  It is, however, possible to
setup the system to automatically run this command when a new Docker Image is
used.


Update the ``docker-compose.yaml`` File
---------------------------------------

To enable automatic system initialisation and updating you need to add the
following service between the ``...`` markers to the ``services`` section of
the ``docker-compose.yaml`` file:

.. code-block::

    version: "3.5"

    services:
        ...
        tryton-update:
            image: tryton/tryton:5.4
            command: sh -c "trytond-admin --database=tryton --all --activate-dependencies --email=${ADMIN_EMAIL_ADDRESS} --verbose && tail -f /dev/null"
            restart: "no"
            environment:
              - DB_HOSTNAME=tryton-postgres
              - DB_PASSWORD=${POSTGRES_PASSWORD}
              - TRYTONPASSFILE=/run/secrets/initial-admin-password
            secrets:
              - source: initial-admin-password
                target: initial-admin-password
            volumes:
              - tryton-data:/var/lib/trytond/db
            depends_on:
              - tryton-postgres
        ...

You also need to add a ``secrets`` section, if your file does not have one yet,
at the same indent level as the ``services`` section but below it at the bottom
of the file, and then add the ``initial-admin-password`` item to it:

.. code-block::

    version: "3.5"

    ...

    secrets:
        initial-admin-password:
            file: ${ADMIN_INITIAL_PASSWORD_FILE:-/dev/null}


Update the ``.env`` File
------------------------

The service and secret that were added to the ``docker-compose.yaml`` file used
two new variables which are defined in the ``.env`` file:

.. code-block::

    ADMIN_EMAIL_ADDRESS=admin@email.address
    ADMIN_INITIAL_PASSWORD_FILE=/path/to/a/file/with/the/initial/admin/password

.. tip::

    The ``ADMIN_INITIAL_PASSWORD_FILE`` variable is only needed if the update
    service is running on a system that has not yet had it's database
    initialised.  Once the database has been initialised this variable and the
    file it refers to is not needed anymore.
    
.. warning::

    Each time the update service runs it will reset the ``admin`` users email
    address to the one defined in the ``ADMIN_EMAIL_ADDRESS`` variable.


Start the Service
-----------------

The automatic update service can be started by running the command:

.. code-block:: bash

    sudo docker-compose up -d

.. warning::

    If you are using the automatic update service with a freshly installed
    system that has not yet had the database initialised, then you must allow
    time for the full database initialisation process to finish before trying
    to connect to your Tryton system.

    If you do not do this the initialisation process may not complete
    successfully and you may need to clear out the docker volume that contains
    the database data and restart the system.


.. include:: /common/global.rst

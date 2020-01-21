Cron Service
============

In order for
:ref:`administration/system/scheduled-actions:Scheduled Actions`
to run, you will need to be running the 
:ref:`administration/services/trytond-cron:trytond-cron` service.


Update the ``docker-compose.yaml`` File
---------------------------------------

You will need to add the service definition to your ``docker-compose.yaml``
file.  This should be added to the ``services`` part of the file, and in
this example it is between the two ``...`` markers:

.. code-block::

    version: "3.5"

    services:
        ...
        tryton-cron:
            image: tryton/tryton:5.4
            command: trytond-cron --database=tryton
            restart: always
            environment:
              - DB_HOSTNAME=tryton-postgres
              - DB_PASSWORD=${POSTGRES_PASSWORD}
            volumes:
              - tryton-data:/var/lib/trytond/db
            depends_on:
              - tryton-postgres
        ...


Start the Service
-----------------

Now that the ``tryton-cron`` service has been added to your
``docker-compose.yaml`` file it will be started and stopped at the same time
as your other Tryton services.  To start it now run:

.. code-block:: bash

    sudo docker-compose up -d


.. include:: /common/global.rst

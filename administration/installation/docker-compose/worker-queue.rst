Task Queue and Worker Service
=============================

In Tryton, some tasks can be run in the background, meaning that you don't have
to wait for them to complete before you can carry on working on other things.


Update the ``docker-compose.yaml`` File
---------------------------------------

To enable this functionality you need to 
:ref:`configure <administration/installation/docker-compose/configuration:Configuration>`
the :ref:`administration/system/queue:Task Queue` and run some
:ref:`administration/services/trytond-worker:trytond-worker` processes,
this is done by adding the part between the ``...`` markers to the ``services``
section of the ``docker-compose.yaml`` file:

.. code-block::

    version: "3.5"

    services:
        ...
        tryton-worker:
            image: tryton/tryton:5.4
            command: trytond-worker --database=tryton
            restart: always
            environment:
              - DB_HOSTNAME=tryton-postgres
              - DB_PASSWORD=${POSTGRES_PASSWORD}
              - TRYTOND_QUEUE__WORKER=True
            volumes:
              - tryton-data:/var/lib/trytond/db
            depends_on:
              - tryton-postgres
        ...


All of the other Tryton services also need to know that the queue is available,
so they are aware that they can add things to the queue.  This means that you
need to let them know by adding the ``TRYTOND_QUEUE__WORKER`` environment
variable to each of the other tryton services defined in your
``docker-compose.yaml`` file (apart from the ``tryton-postgres`` one).


Start the Service
-----------------

Now that the ``tryton-worker`` service has been added to your
``docker-compose.yaml`` file it will be started and stopped at the same time
as your other Tryton services.  To start it now run:

.. code-block:: bash

    sudo docker-compose up -d


.. include:: /common/global.rst

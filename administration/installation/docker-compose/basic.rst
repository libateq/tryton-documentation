Basic Setup
===========

In order to keep things nicely organised the first thing you should do is
create a directory to store all your Tryton deployment's configuration and
setup files in.  These examples use a directory called ``tryton-deployment``,
but you can call it whatever you like:

.. code-block:: bash

    mkdir tryton-deployment


Create the ``docker-compose.yaml`` File
---------------------------------------

The first file to create is ``docker-compose.yaml``.  This is a YAML_ file that
defines the services and other resources that will be needed for your Tryton
system.

A basic ``docker-compose.yaml`` file for a Tryton system defines the PostgreSQL
database and Tryton server services.  These services are essential for a
functioning Tryton system:

.. code-block::

    version: "3.5"

    services:
        tryton:
            image: tryton/tryton:5.4
            restart: always
            environment:
              - DB_HOSTNAME=tryton-postgres
              - DB_PASSWORD=${POSTGRES_PASSWORD}
            volumes:
              - tryton-data:/var/lib/trytond/db
            ports:
              - "127.0.0.1:8000:8000"
            depends_on:
              - tryton-postgres

        tryton-postgres:
            image: postgres:12
            restart: always
            environment:
              - PGDATA=/var/lib/postgresql/data/pgdata
              - POSTGRES_DB=tryton
              - POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
            volumes:
              - tryton-postgres-data:/var/lib/postgresql/data
            expose:
              - "5432"

    volumes:
        tryton-data:
            external: True

        tryton-postgres-data:
            external: True


Create the ``.env`` File
------------------------

Another file that you will need to create is the ``.env`` file.  This contains
the environment variables used in the ``docker-compose.yaml`` file.  It is
important that this file is created in the same directory as the
``docker-compose.yaml`` file.

In the ``docker-compose.yaml`` file created above there is a variable called
``POSTGRES_PASSWORD``.  It needs to be setup in the ``.env`` file so it
is available to Docker Compose, so create a ``.env`` containing:

.. code-block::

    POSTGRES_PASSWORD=_a_strong_randomly_generated_password_

.. note::

    If you followed the
    :ref:`administration/installation/quick-install:Quick Install Guide`
    then you should use the ``POSTGRES_PASSWORD`` password that got
    generated when you started the database.

.. warning::

    Take care to ensure that the ``.env`` file is only readable by the user
    running the ``docker-compose`` commands because it normally contains
    sensitive information such as passwords.


Create the Docker Volumes
-------------------------

Before you can start the services for your Tryton system you need to create
the Docker volumes.

.. note::
    If you followed the 
    :ref:`administration/installation/quick-install:Quick Install Guide`
    then you will have already created the Docker volumes that are required
    so you should skip this step.

.. include:: /common/installation/docker-create-volumes.rst


Start the Services
------------------

Now that the ``docker-compose.yaml`` and the ``.env`` files have been created
and the docker volumes have been setup you should be ready to start the
services that make up your tryton system:

.. code-block:: bash

    sudo docker-compose up -d


Initialise the Database
-----------------------

With your Tryton services now running you can use the 
:ref:`administration/services/trytond-admin:trytond-admin` tool to initialise
the database.

.. note::

    If you followed the 
    :ref:`administration/installation/quick-install:Quick Install Guide`
    then this will have already been done so you should skip this step.

.. note::

    You can also skip this step if you are using the
    :ref:`administration/installation/docker-compose/auto-update:Automatic Update Service`
    as this process will happen automatically.

The database can be initialised by running the following Docker Compose
command:

.. code-block::

    sudo docker-compose exec tryton trytond-admin -d tryton --all


Connect to Your System
----------------------

.. include:: /common/installation/connect-tryton.rst


Manage Your Services
--------------------

Here is a quick overview of a few useful ``docker-compose`` commands that can
be used to help you manage your Tryton system, more information is
available in the `official Docker Compose Documentation`_.

* Start, or update, all services:

  .. code-block:: bash

      sudo docker-compose up -d

* Start, or update, specific services:

  .. code-block:: bash

      sudo docker-compose up -d SERVICE_NAME...

* Stop all services:

  .. code-block:: bash

      sudo docker-compose down

* Stop and remove specific services:

  .. code-block:: bash

      sudo docker-compose rm --stop SERVICE_NAME...

* List service status:

  .. code-block:: bash

      sudo docker-compose ps

* View service logs:

  .. code-block:: bash

      sudo docker-compose logs SERVICE_NAME...


Next Steps
----------

Now that you have a working Tryton system you will probably want to:

* have a look through the available
  :ref:`administration/system/modules:Modules`,
  so you can get a good idea of what modules you need to activate for the     
  functionality that you require.

* add additional services to your Tryton system:

    * :ref:`administration/installation/docker-compose/cron:Cron Service`
    * :ref:`administration/installation/docker-compose/worker-queue:Task Queue and Worker Service`
    * :ref:`administration/installation/docker-compose/auto-update:Automatic Update Service`

* back up your data, this is very important, and this setup places your data
  in two docker volumes (``tryton-postgres-data`` and ``tryton-data``).
  The :ref:`administration/system/data/index:Data Management` section contains
  further information on what data is stored where, and on how you can back it
  up.

* allow access to your Tryton system from different computers.  This basic
  setup only allows connections from the computer the Tryton system is running
  on, but this can easily be changed.

  One option, which can enhance the security and performance of your
  Tryton system is to run it behind a
  :ref:`administration/installation/docker-compose/proxy:Reverse Proxy` such
  as Nginx_ and
  :ref:`administration/installation/docker-compose/proxy:Allow Secure Remote Connections`
  to it.

  A simpler option is to change the ``tryton`` service's ``ports`` value to
  ``8000:8000`` you will then be able to access your Tryton system from other
  computers, however:

  .. warning::

      If you do not configure your Tryton system to use
      :ref:`administration/configuration/options:ssl`, any connections to it
      will not be secure.  Other people will be able to intercept and view any
      data, including things like login passwords and other sensitive
      information, that get sent to and from your Tryton system.

      Never do this without ssl enabled if your system is available across the
      internet, unless you really know what you are doing, and if you really
      know what you are doing, then why are you reading this guide?


.. include:: /common/global.rst

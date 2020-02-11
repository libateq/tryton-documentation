PostgreSQL
==========

PostgreSQL_ is a powerful open source object-relational database system with
over 30 years of active development.  In that time it has earned a strong
reputation for reliability, feature robustness and performance.

If you are running a production Tryton server, then it is also the database
that you will probably want to be using.  PostgreSQL fully supports all of the
features that are used by Tryton, and it is also one of the databases that all
builds of Tryton are tested against.

The PostgreSQL database server is packaged for a wide range of different
operating systems and distributions, and the excellent `PostgreSQL
Documentation`_ is detailed and comprehensive.


Installation
------------

As Tryton has a clean three-tier
:ref:`administration/introduction/architecture:Architecture` you do not have
to install PostgreSQL on the same machine as the Tryton server software.
However, in most cases it is easier and more performant to have PostgreSQL and
the Tryton server running on the same computer.

Installation is normally quite straight forwards, and the
`PostgreSQL Downloads`_ page provides links to pre-built binary packages
for a number of different operating systems.  If you want to install PostgreSQL
from source then there are chapters that cover that process in the `PostgreSQL
Documentation`_.


Setup a Database
----------------

Once you have PostgreSQL running on your chosen system you then need to create
a database on it for use with Tryton.  Often you will also want to create a new
role (also called a user) for Tryton to use when connecting to the database
server.

Creating a Database User
^^^^^^^^^^^^^^^^^^^^^^^^

A new database user can be created with the ``createuser`` program from the
command line:

.. code-block:: bash

    sudo -u postgres createuser tryton

If the PostgreSQL database server is running on a remote machine you will need
to also provide additional connection information to the command, see the
`PostgreSQL Documentation`_ for more information.

You can also use the ``CREATE ROLE`` SQL command if you are already connected
to the database with the ``psql`` command:

.. code-block:: sql

    CREATE ROLE tryton;

Creating a Database
^^^^^^^^^^^^^^^^^^^

The Tryton server stores most of it's information in a database.  Before the
database can be initialised for use with Tryton it must be created.  The
``createdb`` program can be used to create a new PostgreSQL database:

.. code-block:: bash

    sudo -u postgres createdb --owner=tryton --encoding=UTF8 tryton

This example command creates a new database on the local PostgreSQL server
called ``tryton`` that is owned by the ``tryton`` user created in the previous
section.  It is also setup to use ``UTF-8`` as the encoding when storing text,
this is especially important as the Tryton server requires this.

There are also other options that can be specified when creating a new
database, these are described in detail in the `PostgreSQL Documentation`_.

If you are already connected to a database with the ``psql`` command then the
equivalent SQL command would be:

.. code-block:: sql

    CREATE DATABASE tryton OWNER tryton ENCODING UTF8;

Initialising the Database
^^^^^^^^^^^^^^^^^^^^^^^^^

Before the Tryton server can use the database it needs to be initialised.
The :ref:`administration/services/trytond-admin:trytond-admin` command is used
when :ref:`administration/services/trytond-admin:initialising a database`,
and making it ready for use.


.. include:: /common/global.rst

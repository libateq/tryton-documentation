Docker Compose Install Guide
============================

Docker compose is a tool that is designed for defining and running
multi-container applications.  It is ideal for running a Tryton system,
as it lets you define the full range of services that are required, and
manage them together.

When using Docker Compose you define the services and configuration for your
application in a ``docker-compose.yaml`` file, and use a ``.env`` file to
define the environment that it is run in.

These instructions are compatible with the
:ref:`administration/installation/quick-install:Quick Install Guide`.
So if you have already setup a system following those instructions you can then
use these instructions to manage and run it under Docker Compose.


.. toctree::
    :maxdepth: 2

    install
    basic
    configuration
    cron
    worker-queue
    auto-update
    proxy
    modules


.. include:: /common/global.rst

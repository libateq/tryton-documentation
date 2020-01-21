Installation
============

Before you can start using Tryton, you will need to get it installed.  Tryton
has a three-tier :ref:`administration/introduction/architecture:Architecture`,
this means there are several components that need to be installed to get a
working system.

A minimal installation that you can use to explore, test and evaluate Tryton
can be quickly setup using the official Docker image.  This process is
described in the quick install guide.

If, after following the quick install guide, you want to use Docker Compose to
manage the system you have setup, then this can be done by following the Docker
Compose Installation instructions.

.. toctree::
    :maxdepth: 2

    quick-install
    docker-compose/index


There is detailed information that covers installing each of the different
parts of Tryton in the following sections.

.. toctree::
    :maxdepth: 2

    database/index
    server/index
    modules
    client/index


.. include:: /common/global.rst

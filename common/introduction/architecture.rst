Architecture
============

Tryton is designed as a multi tier application in which each of the layers
(or tiers) is separate and performs a specific role. By separating the
application into these separate parts, and providing a well defined way for
each of these parts to communicate, it allows considerable flexibility in how
Tryton is deployed.  This means there is the possibility of using different
databases or clients with a Tryton server.


Tiers
-----

As is common with three-tier software applications, Tryton is split up into
a data tier, a logic tier and a presentation tier.  The data tier is
where the data in a Tryton system is stored, and is provided by an SQL
database.  The logic tier controls the application's functionality, and is
provided by the ``trytond`` server.  Finally there is the presentation tier
which provides the user interface and is supplied by one of the Tryton
clients.


Database
^^^^^^^^

TODO: Document the database tier - normally postgresql


Server
^^^^^^

TODO: Document the Tryton tier - server and modules


Modules
"""""""

Tryton is designed to be flexible, the server's functionality can be changed
and extended in a modular way.  This advanced modularity allows it to be
easily adapted to many different uses.

In fact Tryton can be used as a platform for the development of solutions other
than business ERPs.  One prominent example is `GNU Health`_ which is a free
Health and Hospital Information system based on Tryton.


Client
^^^^^^

TODO: Document the client tier - tryton and sao


.. include:: /common/global.rst

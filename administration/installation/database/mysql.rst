MySQL / MariaDB
===============

MySQL_ is an open-source relational database management system, and is commonly
used as a component of Linux web application software stacks and database
driven web applications such as Wordpress.  It was forked in 2010 due to
concerns over Oracle's acquisition of Sun Microsystems, who at the time owned
MySQL.  The fork, called MariaDB_, aims to provide high compatibility with
MySQL so it can be used as a drop in replacement when desired.


Depreciation
------------

Originally a core backend for Tryton, MySQL was removed from Tryton version 4.8
and later by issue7017_.  This was because the binding that was being used did
not support Python 3.

This backend is still available in the `Sandbox trytond-mysql repostitory`_
but as it stands is unlikely to work with current versions of Tryton because
of the reasons it was dropped in the first place and the fact that it has been
unmaintained since it was removed.


.. include:: /common/global.rst

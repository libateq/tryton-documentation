Oracle
======

Oracle is a proprietary multi-model_ database management system produced by the
`Oracle Corporation`_.  It is commonly found as parts of systems that run
data warehousing and mixed database workloads, and is used by companies in the
market for mid-range database systems.  It can be installed on site, in the
cloud or in a hybrid cloud environment.


Third-Party Extension
---------------------

Back in 2015 there was some work done by B2CK_ to develop an Oracle database
backend for Tryton using cx_Oracle_.  The `trytond_backend_oracle`_ repository
contains the work that was done, which was created alongside the Tryton
development branch in the run up to the release of version 3.8 of Tryton.
Although complete, no release against a stable version of Tryton was done, and
this backend is probably of more of interest to developers who may be
considering writing a database backend for Tryton.  It is good to note that
some of the issues (e.g. issue4809_, issue4814_, issue4881_) that were
encountered during the development of this backend have helped to improve
Tryton.

As most companies that deploy Tryton use
:ref:`administration/installation/database/postgresql:PostgreSQL` as the
database backend there appears to be little demand for maintaining this
third-party extension.


.. include:: /common/global.rst

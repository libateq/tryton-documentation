Linux OS Distribution
=====================

Third-party volunteers have packaged Tryton for a wide range of different Linux
distributions.  These packages provide simple installation and better
integration with the operating system, but many are quite out of date, and for
others there is often quite a delay before new versions of Tryton make it into
the distributions.

.. tip::

    As many of the packages in some of the distributions are old, and some are
    no longer supported, you will probably be better off installing Tryton in
    a Python virtual environment from the
    :ref:`administration/installation/server/pip:Python Packages`.
    This will then allow you to install an upto date stable and supported
    version of Tryton.


Arch Linux
----------

TODO


Debian
------

Due to the different release policies of Tryton and Debian_ only the `current
Long Term Release <Tryton Release Process_>`_ is included in the main Debian
repository.  However, the `Tryton Debian Supporters`_, who maintain and
package the releases for Debian, also have a `Tryton Debian APT Repository`_
where they make other (normally older) releases available.

Installation from the Main Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The Tryton server and desktop client can be installed from the main Debian
repository in the same way as you would install other software, e.g.:

.. code-block:: bash

    sudo apt-get install tryton-client tryton-server tryton-modules-all

.. note::

    This will also install
    :ref:`administration/installation/database/postgresql:PostgreSQL`
    on your system if it is not already installed because the ``tryton-server``
    package *recommends* ``postgresql``.

Installation from the Tryton Debian Apt Repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Installation from the `Tryton Debian APT Repository`_ is similar to installing
from the main Debian repository, except you must first add the repository to
your system's apt sources.

In the ``sources.list`` entry you will need to specify which Debian-Tryton
distribution you want to use.  This should be the codename of the Debian
release on your system, followed by a dash (``-``), and then the series of
Tryton that you want to use, e.g. ``buster-5.0``.  There is a list of available
`Debian-Tryton distributions`_ on the repository server.

So firstly add the repository to the apt sources:

.. code-block:: bash

    TRYTON_SERIES="5.0"  # Change this number to the tryton series to install
    source /etc/os-release
    echo "deb http://debian.m9s.biz/debian/ ${VERSION_CODENAME}-${TRYTON_SERIES} main" | \
        sudo tee "/etc/apt/sources.list.d/tryton-${TRYTON_SERIES}.list"

You will now need to download and add the key for the repository to apt:

.. code-block:: bash

    curl http://debian.m9s.biz/debian/debian.tryton.org-archive.gpg | \
        sudo apt-key add -

Now you can update apt's list of packages:

.. code-block:: bash

    sudo apt-get update

And finally install the Tryton server, modules and desktop client:

.. code-block:: bash

    sudo apt-get install tryton-client tryton-server tryton-modules-all

.. note::

    This command will also install
    :ref:`administration/installation/database/postgresql:PostgreSQL`
    on your system if it is not already installed because the ``tryton-server``
    package *recommends* ``postgresql``.

Installation of the Tryton Web Client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You only need to install the Tryton web client if you want to be able to access
your Tryton system using a web browser.  If this is the case then you will
almost certainly need to build and install the Tryton web client manually.
It was available for Tryton version 4.6 and earlier in the Tryton Debian APT
Repository in a package called ``tryton-sao``, but due to unmet dependencies
it is not packaged for any newer version and is not available in any of the
main Debian repositories.

.. include:: /common/installation/server-web-client.rst

Database Setup
^^^^^^^^^^^^^^

.. include:: /common/installation/server-database-setup.rst


Fedora
------

TODO


Gentoo
------

TODO


OpenBSD
-------

TODO


Ubuntu
------

The packages for Ubuntu are taken from the main Debian release, and thus are
provided by the `Tryton Debian Supporters`_.  This means that the version of
Tryton that is available is limited to the `current Long Term Release
<Tryton Release Process>`_ that was available at the time your Ubuntu
distribution was released.

Installation
^^^^^^^^^^^^

Installation of the Tryton server, modules and desktop client from the Ubuntu
repository is done in the same way as other software, and in the same way as
on Debian:

.. code-block:: bash

    sudo apt-get install tryton-client tryton-server tryton-modules-all

.. note::

    Running this command will also install
    :ref:`administration/installation/database/postgresql:PostgreSQL`
    on your system if it is not already installed because the ``tryton-server``
    package *recommends* ``postgresql``.

Installation of the Tryton Web Client
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to be able to access your system from your web browser, instead of
the Tryton desktop client, then you will need to manually build and install the
Tryton web client on your system.

.. include:: /common/installation/server-web-client.rst

Database Setup
^^^^^^^^^^^^^^

.. include:: /common/installation/server-database-setup.rst


NetBSD
------

TODO


.. include:: /common/global.rst

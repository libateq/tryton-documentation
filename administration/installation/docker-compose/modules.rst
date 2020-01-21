Module Installation
===================

All the standard core modules are pre-installed on the standard Tryton Docker
image.  However there are lots of additional third party modules available
which you many want to use.

Adding additional modules to a Tryton system that uses Docker is normally
done by extending the standard Tryton Docker image.  The new image, containing
the extra modules, is then used instead of the standard image.

.. note::

    Although this topic borders on Tryton development, which is outside the
    scope of this manual, it is useful for Administrators who have identified
    existing third party modules that they wish to use with their system.


Create a Dockerfile
-------------------

You need to define the steps that are required to create the new Docker image.
This is done by creating a ``Dockerfile``, normally in a new directory, along
with any additional files that are referenced by it.

.. code-block:: bash

    mkdir tryton-extra-module
    cd tryton-extra-module
    touch Dockerfile

Use Modules From PyPI
^^^^^^^^^^^^^^^^^^^^^

If the modules that you want to install are available on PyPI_ then you can
install them directly from there.  Your ``Dockerfile`` will need to look
something like this:

.. code-block::

    FROM tryton/tryton:5.4
    USER root
    RUN pip3 install \
            trytond_account_personal && \
        rm -rf /root/.cache
    USER trytond

.. tip::

    You can install as many additional modules as you like by updating the
    ``pip3`` command e.g.:

    .. code-block::

        RUN pip3 install \
                module1 \
                module2 \
                module3 && \
            rm -rf /root/.cache

Use Modules From Source Packages
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

If you want to install some modules that are not available on PyPI_, or you
have other modules that you want to install from source packages then this is
possible.

You first need to put the source packages in the same directory as your
``Dockerfile``.  Here in this example, we are downloading a source package, but
how you get the source package is not important:

.. code-block:: bash

    curl --output trytond_account_personal-5.4.0.tar.gz \
        https://files.pythonhosted.org/packages/21/a6/790a379d07f00509e96be1987ac2f2f3d2a35b18b9c00a3399401ef2db4d/trytond_account_personal-5.4.0.tar.gz

Now you need to setup your ``Dockerfile``:

.. code-block:: bash

    FROM tryton/tryton:5.4
    USER root
    COPY *.tar.gz /dist/
    RUN pip3 install /dist/* && \
        rm -rf /dist && \
        rm -rf /root/.cache
    USER trytond

.. tip::

    You can install as many modules you like this way, just place them all in
    the same directory as the ``Dockerfile``, and as long as they have the
    ``.tar.gz`` extension they will get installed.


Build the Docker Image
----------------------

With the ``Dockerfile`` and any other files in place you can now build the
new Docker image:

.. code-block::

    sudo docker build --tag=tryton-personal:5.4 .


Update the ``docker-compose.yaml`` File
---------------------------------------

You should now update your ``docker-compose.yaml`` file to use the new image
instead of the standard Tryton Docker image.  To do this change all the lines
that read:

.. code-block::

    image: tryton/tryton:5.4

to:

.. code-block::

    image: tryton-personal:5.4


Restart the Services
--------------------

Due to the changes that we have made to the Tryton services we will need to
recreate them, so they start using the new Docker image.  This is done by
running:

.. code-block:: bash

    sudo docker-compose up -d


Update your System
------------------

Now the new modules have been installed in your Tryton system it needs to be
updated so it recognises that they are available for activation.  This is done
by running the :ref:`administration/services/trytond-admin:trytond-admin` tool:

.. code-block:: bash

    sudo docker-compose exec tryton trytond-admin -d tryton --all

.. note::

    If you are using the 
    :ref:`administration/installation/docker-compose/auto-update:Automatic Update Service`
    then you should not need to run this step as it should happen automatically
    when the services are restarted.


.. include:: /common/global.rst

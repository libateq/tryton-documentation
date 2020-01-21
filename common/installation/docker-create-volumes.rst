In Docker when a container is removed any changes to it's state that are not
stored in persistent storage are lost.  By creating some volumes for the
data we can save the data you enter into your Tryton system, even when the
containers that make up your system are removed:

.. code-block:: bash

    sudo docker volume create tryton-data
    sudo docker volume create tryton-postgres-data

.. note::

    You can find the location where the data in these volumes is stored by
    running:

    .. code-block:: bash

        sudo docker volume inspect tryton-data | grep Mountpoint
        sudo docker volume inspect tryton-postgres-data | grep Mountpoint

    Data stored here can be backed up in the same way as you would normally
    backup data from your system, although you will probably want to
    stop the tryton and postgres services before backing these up, so you
    can be sure the data in the backups is in a consistent state.

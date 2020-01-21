Access Management
=================

In Tryton access to the system and it's models, fields, buttons, actions, menu
items, and sets of records can all be configured and controlled.
Once the user has logged in to the system the modules that have been activated
on the system will provide good default access rules, but these can be changed
and added to as required.

Access into a Tryton system is controlled based on the identity of the person
who is using it.  A user must login to a Tryton system in order to be able to
use it.

.. toctree::
    :maxdepth: 2

    users

Once a user has logged onto Tryton, their ability to access the different
parts of the system is controlled based on what groups they are in.

.. toctree::
    :maxdepth: 2

    groups

The different areas of the system where access can be controlled are covered
in the following sections.  In each case access can be granted based on group
membership.  Normally if there are no restrictions defined on an item then
access is unrestricted.

.. toctree::
    :maxdepth: 1

    models
    fields
    buttons
    rules
    menus
    actions


.. include:: /common/global.rst

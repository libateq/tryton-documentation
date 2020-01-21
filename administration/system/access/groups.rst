Group Access Management
=======================

Groups provide the basis on which most access control in Tryton is performed.
Extra groups are often added to the system when new modules are installed.
These standard groups are designed to provide access to components and
functionality provided by the modules that create them.

Some groups may give full access to certain things, whereas others may only
allow read-only access.  A user can belong to as many groups as required,
so they can have access to the parts of the system that they need.

.. tryton:view: /images/res_group_form.png


Creating and Updating Groups
----------------------------

Groups can be accessed through the :tryton:menu:`res.menu_group_form`
menu item.  When the groups view is opened, a list of the currently
available groups will appear, from here groups can be added, removed or
changed.

New groups can be created and added to the system by clicking on the
:tryton:toolbar:`new` button on the toolbar.  These groups can then be
configured to allow specific access to their members.

.. hint::

    It is not normally a good idea to modify the permissions on the
    standard predefined groups.  If you want to restrict the access a certain
    group of users have, then it is better to :tryton:toolbar:`clone` the
    group and change the settings on the new group.  You can then put the
    users in this new group instead of the original one.

Group Members
^^^^^^^^^^^^^

When you :tryton:toolbar:`switch` to the detailed view of a group you will
be able to see a list of the members of the group.  From here you can add and
remove users from the group.

Access Permissions
^^^^^^^^^^^^^^^^^^

To view and update the access permissions that users of the group have you
need to change the settings under on Access Permissions page.  If a user
tries to access things that they do not have permission for then an error
message is displayed.

**Access Model**
  This allows you to see and change the specific access permissions that
  members of the group have to
  :ref:`administration/system/access/models:Models` and
  :ref:`administration/system/access/fields:Fields`.
  
**Rules**
  The :ref:`administration/system/access/rules:Record Rules` allow you to setup
  the level of access that members of the group have to different sets of
  records.
  Only record rules that are not global, or default, can be associated with
  groups.

**Button**
  The :ref:`administration/system/access/buttons:Buttons` access permissions
  allow you to configure which buttons members of a group are allowed to
  use.

**Access Menu**
  The :ref:`administration/system/access/menus:Menus` that are visible to
  members of the group can be setup on this page.


.. include:: /common/global.rst

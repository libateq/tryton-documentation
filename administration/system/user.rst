User Management
===============

Users can be added, changed or deactivated using the view that gets opened
from the :tryton:menu:`res.menu_user_form` menu item.  When you open this you
will see the list of users that currently exist on the system.  Detailed
information about each user can be viewed and changed by switching from
list view to form view using the :tryton:toolbar:`switch` button on the
toolbar.  New users can be created by using the :tryton:toolbar:`new`
button on the toolbar.

.. tryton:view:: res.user_view_form /images/res_user.png

    Screenshot of the users form.

.. note::

    Any changes that you make to a user's record do not take full effect until
    the next time that the user connects to the system, or changes their
    preferences.

.. hint::

    If an employee has left, or no longer needs access to the system the best
    thing to do is to untick the :tryton:field:`~res.user.active` field to
    deactivate them.  This will stop them from logging in and will also remove
    their user record from normal use and hide it.  It can still be
    accessed by clicking on the :tryton:toolbar:`show inactive records`
    button when filtering for records, so you can still access it if you
    ever need to in the future.

Some of the fields in the user view are used for user administration
and management and other fields hold information and settings that the
user can change via their :tryton:toolbar:`user preferences`.

A few of the fields allow you to manage a users access to the system.
See the :ref:`administration/system/access/index:Access Management` section
for information on how access is controlled in a Tryton system.


Properties
----------

The main fields that are used to manage users, and which cannot be changed
by the user themselves are:

:tryton:field:`~res.user.login`
  This is the login name used when logging into Tryton.
  The :ref:`administration/system/access/users:User Access Management` section
  contains more details on this field.

  .. caution::

      This field is case sensitive, so the system considers '``admin``' and
      '``Admin``' to be different users.

:tryton:field:`~res.user.groups`
  This is a list of the groups that the user belongs to.
  More information about this field can be found in the
  :ref:`administration/system/access/groups:Group Access Management` section.


Preferences
-----------

There are fields that contain information about the user which both the
user and administrator can alter.  These settings can be accessed by the
user via the :tryton:toolbar:`user preferences` menu item in the client.

Some of the available settings of note are:

:tryton:field:`~res.user.password`
  This is the user's password.
  See the :ref:`administration/system/access/users:User Access Management`
  section for detailed information about this field.

:tryton:field:`~res.user.menu`
  This is the action that gets run to provide the main menu that is
  normally displayed on the left hand side of the screen when the user has
  logged in.

  .. hint::

      Normally there is only one menu available for use here.  To mark other
      menus for use, open up the :tryton:menu:`ir.menu_act_action` and
      set the appropriate records :tryton:field:`~ir.action.usage` field to
      '``menu``'.

:tryton:field:`~res.user.actions`
  These are a list of the actions that will be run when the user logs into
  the system.  This is very useful for opening views that you know you will
  always want to use straight away after logging in.

:tryton:field:`~res.user.applications`
  This provides a list of applications that have either requested, or
  currently have, access to the system as this user.  Once an application
  has requested access to the system it will appear in this list, and this must
  be validated by the user before the application can then access any data
  stored in the system.

:tryton:field:`~res.user.language`
  The language that the client, and other translatable fields will appear
  in.

  .. note::

      The language will need to have been set as
      :tryton:field:`~ir.lang.translatable`, see the
      :ref:`administration/system/localisation:Localisation` section for more
      information.


.. include:: /common/global.rst

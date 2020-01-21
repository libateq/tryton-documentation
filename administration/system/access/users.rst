User Access Management
======================

Every person that uses the system will have a user record.  This contains
information about the user and is used to store the user's settings and
preferences.  The :ref:`administration/system/user:User Management` section
contains detailed information on creating and setting up users.


Access Controls
---------------

There are several fields that control a users access to the system.

:tryton:field:`~res.user.login`
  This is the login name for the user, they will need this, and their
  password to log into Tryton.

  .. caution::

      This field is case sensitive, so the system considers '``admin``' and
      '``Admin``' to be different users.

:tryton:field:`~res.user.password`
  This is the user's password, and along with the login it is normally
  required when logging into Tryton.

  .. note::

      Unlike the other fields that control a users access to the system
      this field is part of the users preferences, and so this means that the
      user can change their own password whenever they need to.

  .. note::

      Due to the fact that the password is stored securely on the server and
      is never sent to the client, the show button does not actually show you
      the user's existing password.
      It is intended to be used to help you check you have entered a new
      password in correctly.

  .. tip::

      If the user has forgotten their password use the
      :tryton:button:`res.user.reset_password` button to email a temporary
      password to them, they can then set their own secure password.

:tryton:field:`~res.user.groups`
  These are the groups that the user belongs to and are used for 
  :ref:`administration/system/access/groups:Group Access Management`.
  This is one of the main ways of managing a user's access to different parts
  of the system.


How Access is Controlled
------------------------

A user's access to a Tryton system is controlled by the login process.
In order to be able to use the system a user must have a user record on the
system.  When the user tries to login, the login and password that they enter
are checked against those stored in the system.  If the details the user
supplied match those stored in the system then the user is allowed in.

Once the user has logged in then further access to the system is controlled
by the :ref:`administration/system/access/groups:Group Access Management`
settings.

.. tip::

    When users should no longer have access to the system the best thing
    to do is to deactivate the user's record. This is done by unticking the
    :tryton:field:`~res.user.active` field.
    Once saved the user record will then be hidden from view and the user will
    no longer be able to log in.  If you need to access the user's record in
    future then this is still possible by clicking on the
    :tryton:toolbar:`show inactive records` button and filtering for it.


.. include:: /common/global.rst

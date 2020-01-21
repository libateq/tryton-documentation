Buttons
=======

Tryton allows you to configure which buttons a user is allowed to use.  As
with the other access control mechanisms, the settings that control which 
buttons are available work based on what groups a user belongs to.

The access to buttons can be managed by opening the
:tryton:menu:`ir.menu_model_button_form` menu item.  This form shows the
list of available buttons, and if you :tryton:toolbar:`switch` to form view
you can see detailed information about each button.

It is possible to setup buttons so that multiple users must click on them
before the button performs it's operation.  This is done by configuring the
:tryton:field:`~ir.model.button.rules` and
:tryton:field:`~ir.model.button.reset_by` fields.


Access Controls
---------------

The button fields that are used to control who can use the button are:

:tryton:field:`~ir.model.button.groups`
  This is a list of groups that are associated with the button.  To use the
  button the user can be a member of any of these groups.

  .. note::

      If no group is defined for a button, then the ``write`` permission
      for the model the button belongs to is checked instead.

:tryton:field:`~ir.model.button.rules`
  The button rules are a list of additional rules that are applied to
  button use.  These provide you with a flexible way of setting up buttons
  so that they require multiple users, perhaps from different groups, to
  click on them.  The operation the button performs will only happen once
  all the button's rules are satisfied.

:tryton:field:`~ir.model.button.reset_by`
  This field works with the :tryton:field:`~ir.model.button.rules` field.
  When a button listed here is clicked on, then any previous clicks towards
  this button's rules are reset and will need to be done again.

  .. tip::

      This is useful when there is a button can put a document back into a
      state where it can be altered.  By resetting the clicks on a button that
      would confirm or validate the document any alterations to the
      document will then have to go through the full normal verification
      process.


How Access is Controlled
------------------------

A user is granted permission to use a button if:

* they are a member of one of the groups that are associated with the
  button, or
* there is a record for the button that does not have any groups
  associated with it and the user also has the ``write`` permission to the
  model that the button belongs to.

The button's operation will be performed if:

* there are no rules defined for the button, or
* all the button's rules have now been satisfied by taking into account this
  button click and all previous button clicks that have not been reset.

.. note::

    Buttons that a user does not have permission to use are marked as
    read-only in the client.


.. include:: /common/global.rst

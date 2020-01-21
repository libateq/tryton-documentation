Actions
=======

Access to actions in Tryton is controlled based on the groups that the user
is a member of.  This works in a similar way to other access controls in
Tryton.  A user can only see and start actions that they have permission to
use.  Any attempt to access an action that the user does not have access to
will result in an error message being displayed to the user.


Access Controls
---------------

The field that is used to control access to an action is the action's 
:tryton:field:`~ir.action.groups` field.  Using this field you can control
which groups of users can see and start an action.  Each different type of
action has a :tryton:field:`~ir.action.groups` field which is normally found
on the Groups page on the action's view.


How Access is Controlled
------------------------

Actions can be seen and launched by a user if:

* there are no groups listed in the action's :tryton:field:`~ir.action.groups`
  field, or
* the user is a member of one of the groups listed in the action's
  :tryton:field:`~ir.action.groups` field.

.. note::

    The access controls for wizards are slightly more restrictive than other
    types of action.  See the notes about
    :ref:`administration/system/access/actions:Wizards` for more information.


Types of Action
---------------

There are several different types of actions in Tryton.

Windows
^^^^^^^

Access to :ref:`Window <administration/system/core/actions:Windows>` actions can be
configured by opening the :tryton:menu:`ir.menu_action_act_window` menu item.
The :tryton:field:`~ir.action.act_window.groups` field is used to configure
which groups are allowed to open the window.

Reports
^^^^^^^

The :ref:`administration/system/core/actions:Reports` that users can see and
open are controlled by opening the :tryton:menu:`ir.menu_action_report_form`
menu item.  For each report you can set the
:tryton:field:`~ir.action.report.groups` that are allowed to open the report.

Wizards
^^^^^^^

Access to :ref:`administration/system/core/actions:Wizards` that are used to
gather data from a user and perform a task can be controlled by opening the
:tryton:menu:`ir.menu_action_wizard` menu item.  You can set the groups allowed
to use the wizard by adding and removing groups from the
:tryton:field:`~ir.action.wizard.groups` field.

.. note::

    If no groups are set for a wizard action then it is the associated model's
    ``write`` permission that determines whether the user can run the wizard
    or not.

.. note::

    The ``read`` permission for the model associated with the wizard is always
    checked before running the wizard to ensure that the user has permission to
    see the data in the model.  Users without the ``read`` permission to the
    model will not be able to run the wizard.

URLs
^^^^

The :ref:`URL <administration/system/core/actions:URLs>` actions that a user can see
and open are controlled from the view that is opened from the
:tryton:menu:`ir.menu_action_url` menu item.  Each url has a
:tryton:field:`~ir.action.url.groups` field that can be used to control which
groups of users can see and use the url action.


.. include:: /common/global.rst

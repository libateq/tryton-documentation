Triggers
========

Tryton can be setup to run a method when an event happens to a record.  For
example, you can setup a trigger to run a method when a new user is created,
or when a user changes their email address.  You can also add conditions to the
triggers, so the events will only happen for certain records, or will only
happen some of the time.  The methods that can be triggered by an event will
depend on the modules that have been activated on your system, and the
methods those modules provide.


Managing Triggers
-----------------

Triggers are accessed by opening the :tryton:menu:`ir.menu_trigger_form` menu
item.  When this view is opened then a list of the currently active triggers
is displayed.  The :tryton:toolbar:`switch` button will allow you to see the
detailed information about each trigger.

New triggers can be added using the :tryton:toolbar:`new` button on the
toolbar, and records can be changed and saved as normal.

.. tryton:view:: ir.trigger_view_form /images/ir_trigger.png

    Screenshot of the Trigger form.


Properties
----------

Triggers have some general properties, these are:

:tryton:field:`~ir.trigger.name`
  The name for the trigger.

  .. tip::

      It is a good idea to give it a name that describes what the trigger
      is for, or what it does, to make it easier to find and manage the
      triggers in future.

:tryton:field:`~ir.trigger.model`
  This is the model that is associated with the trigger.  Events on records
  in this model can trigger running the method.

:tryton:field:`~ir.trigger.action_model`
  The action model is the model that contains the method that gets run if
  the trigger is activated.

:tryton:field:`~ir.trigger.action_function`
  This is the name of the method that gets run when the trigger is activated.


Events
------

Triggers can be activated when events happen to records in their associated
model:

:tryton:field:`~ir.trigger.on_create`
  Triggers with this field ticked can be activated when new records are
  created.

:tryton:field:`~ir.trigger.on_write`
  When records are changed, then triggers with this field ticked can be
  activated.

:tryton:field:`~ir.trigger.on_delete`
  If this field is checked, then deleting records can cause the trigger to
  be activated.

Triggers can also be activated at regular intervals:

:tryton:field:`~ir.trigger.on_time`
  This field allows the trigger to be activated using the
  :ref:`Run On Time Triggers <administration/system/scheduled-actions:Available Methods>`
  :ref:`Scheduled Action <administration/system/scheduled-actions:Scheduled Actions>`.

  .. important::

      Triggers that are activated using the :tryton:field:`~ir.trigger.on_time`
      field will only run if the system has been correctly setup to run
      scheduled actions, and the **Run On Time Triggers** method is called from
      an active scheduled action.


Conditions
----------

You can specify some limitations to the records that can activate a trigger,
and how often a trigger can run:

:tryton:field:`~ir.trigger.condition`
  This is a :ref:`administration/reference/pyson:PYSON` statement that gets
  evaluated for each record that the trigger has been activated for.
  The trigger's method is only run for records whose condition evaluates to
  ``True``,  and if the trigger was activated because a record has been
  changed, then the condition must also have been ``False`` before the record
  was changed.

  .. tip::

      To always run the method set the condition to ``True``.

:tryton:field:`~ir.trigger.limit_number`
  This field is used to limit the number of times that the method will be run
  for a record.  Set this to 0 if you don't want to limit the number of calls
  to the method.

  .. tip::

      If you wanted to only call the method the first time a record was
      changed, then you would set this to 1 for the trigger.

:tryton:field:`~ir.trigger.minimum_time_delay`
  You can use this field to set a period of time during which any further
  events will not activate the trigger for the record.  If this field is left
  blank then there will be no delay period.

  .. tip::

      This can be useful in cases where the method notifies the user of some
      event.  If lots of separate changes are being made to a record in a short
      space of time, then you can use this so you don't spam the user with
      lots of notifications.


.. include:: /common/global.rst

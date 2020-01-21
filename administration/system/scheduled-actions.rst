Scheduled Actions
=================

You can setup Tryton to run methods at regular intervals.  The methods that
modules setup for use with the scheduler are commonly used for automating tasks
that can be run without user intervention and that need to be run regularly on
set days, or at set times.  The methods that can be scheduled depend on the
modules that have been activated on your system.

The method scheduler is sometimes referred to as cron.  This name is derived
from the Greek word for time, chronos, and takes it's name, more directly, from
the time based job scheduler commonly used on Unix like computer systems.


Cron Service
------------

In order for the scheduled actions to run you need to configure and run the
:ref:`administration/services/trytond-cron:trytond-cron` service.

.. important::

    If this service is not running no scheduled actions will be run.


Managing Scheduled Actions
--------------------------

Scheduled actions are managed from the view that is opened from
:tryton:menu:`ir.menu_cron_form`.  When this view is opened it shows a list of
the methods that are currently scheduled to be run by the system.  By using the
:tryton:toolbar:`switch` button on the toolbar you can swap views to see
detailed information about each scheduled action.

.. tryton:view:: ir.cron_view_form /images/ir_cron.png

    Screenshot of a Scheduled Action.

New scheduled actions can be created as normal by using the
:tryton:toolbar:`new` button from the toolbar.  They can be updated just like
any other records by editing them and then saving the changes.

.. tip::

    If you need to, you can delete scheduled actions by selecting the
    :tryton:toolbar:`delete` menu item.  Often, however, it is better to
    keep the scheduled action and instead just deactivate it.  This is done by
    unticking the :tryton:field:`~ir.cron.active` field.  Doing this will hide
    the scheduled action and stop it from running, but it will still be saved
    on the system, and can then be easily reactivated if required.

Properties
^^^^^^^^^^

Each scheduled action has a set of properties that determine what method
will get run, and when, and how often, this will happen.

:tryton:field:`~ir.cron.method`
  This is the method that the cron service will run.

:tryton:field:`~ir.cron.interval_number`
  This is the length of time that should elapse between successive calls to the
  method.  The :tryton:field:`~ir.cron.interval_type` field determines what
  units this value is in.

:tryton:field:`~ir.cron.interval_type`
  This field allows you to specify the units that the
  :tryton:field:`~ir.cron.interval_number` field is in.

:tryton:field:`~ir.cron.minute`
  This is the number of minutes past the hour at which the method will be run.

:tryton:field:`~ir.cron.hour`
  For tasks that should be run daily, weekly or monthly this allows you to
  define the hour of the time at which the method will be run.

:tryton:field:`~ir.cron.weekday`
  For scheduled actions that are run on a weekly or monthly basis, this can be
  filled in to set the day of the week on which the method should run.

:tryton:field:`~ir.cron.day`
  This field is used to run a method on a particular day of the month.

:tryton:field:`~ir.cron.next_call`
  This field is set to the date and time that the scheduled action will next
  run.  It is automatically set and updated as the scheduled actions happen.


Available Methods
-----------------

The following methods are available to be scheduled:

Run On Time Triggers
    This method is used to check and then activate, if required, any
    :ref:`administration/system/triggers:Triggers` that are set to run
    :tryton:field:`~ir.trigger.on_time`.


.. include:: /common/global.rst

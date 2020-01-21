Task Queue
==========

The task queue allows some tasks to be run automatically in the background.
This means that, for these tasks, you won't have to wait until they have been
completed before you can carry on working on other things.

On a system that has a task queue setup and configured, tasks that have been
designed to use the task queue won't necessarily be run immediately.  Instead
they are added to the task queue ready to be run by a separate worker process.
When a worker is available to handle the task it will then be executed.

If the task queue is not setup, and there are no workers configured to execute
tasks, then the task is run during the normal processing of the operation you
are doing.  This means you will have to wait for the operation to finish before
you can continue working on other things.

.. note::

    Most tasks do not take much time to run, and using a task queue is
    completely optional.  In fact for many systems you will not notice a
    difference between running the system with, or without, a task queue.

Once the task queue has been setup and configured then there are no additional
settings or options that need to be adjusted by the administrator.
The task queue will get used automatically without any user interaction at all.
From a users point of view the system will operate in the same way as before,
with a few minor differences due to some tasks not necessarily happening
immediately.


Setup and Configuration
-----------------------

In order to use the task queue it needs to be setup and configured.  The
configuration for the task queue is done in the
:ref:`administration/configuration/options:queue` section of the
:ref:`administration/configuration/index:Configuration` file.

You also need to be running the
:ref:`administration/services/trytond-worker:trytond-worker` processes that are
used to execute the items on the task queue.


Queueable Tasks
---------------

The following tasks are put onto the task queue when it is available:

* There are no tasks in the available modules that are designed to use the
  task queue.


.. include:: /common/global.rst

Modules
=======

The modules in Tryton provide the main components and functionality that is
available in a Tryton system.  Each module adds, changes or extends existing
parts of the system.  This allows a layered approach to adding business
concepts to a system and enables you to pick and choose the specific things
required by your business.

Many modules add to, change, or enhance components or functionality that is
provided by other modules.  All module dependencies of a module must be
available to be able to use that module.

Adding a module to a system is a three part process.  The module must first
be installed onto the server, then it must be activated inside your Tryton
system, and finally any basic configuration of it is done.

Modules are activated and managed using the menu items found under the
:tryton:menu:`ir.menu_modules` menu.


Installation
------------

Installing a module is covered in the
:ref:`administration/installation/modules:Module Installation` section.
Once the module has been installed, and the list of modules has been
updated, then it can then be activated.


Activation
----------

To activate a new module you need to open the
:tryton:menu:`ir.menu_module_form` menu item.  From here you can filter or
search for the desired modules.

.. tryton:view:: ir.module_view_tree /images/ir_module.png

.. important::

    Before you activate a module on a production system, make sure that you
    understand what the module does.  It can be difficult to completely
    deactivate modules, so just install the modules that you know you need.
    It is a good idea to test out new modules on a test system first.

Each module that has been installed has a state which indicates whether it
is currently active or not, or whether it is marked to be activated or updated.
You can also see a list of a module's dependencies in the 
:tryton:field:`~ir.module.dependencies` field in the modules form.

Clicking on the :tryton:button:`ir.module.activate` button will mark
the module, and it's dependencies, as
:tryton:option:`~ir.module.state.to activate`.

Once the right modules have been marked for activation they can be activated
by clicking on the :tryton:toolbar:`launch action` button on the toolbar,
and then selecting :tryton:wizard:`ir.module.activate_upgrade`.


Configuration
-------------

At the end of the activation process a configuration wizard will run.  This
will help you setup any basic initial configuration that needs to be done for
the modules that you have activated.

Now the modules are activated and configured you will be able to use the new
functionality, behaviour or components that they provide.

The :tryton:menu:`ir.menu_config_wizard_item_form` menu item allows you to
open up a view containing a list of items that are run by the module
configuration wizard.  From here you can see and change the state of the
configuration items.

If you cancelled the configuration wizard, or have updated the configuration
items states and need to run it again, then this can be done by clicking on the
:tryton:toolbar:`launch action` button on the toolbar and from there
running the :tryton:wizard:`ir.module.config_wizard`.


Deactivation
------------

Although Tryton has this functionality, this is not recommended for use
on a production system.  You should always use a test system for any
testing that you want to do.

.. important::

    Avoid deactivating modules on a production system.

The tables in the database where the module's information was stored is
**not** removed when a module is deactivated, it remains in the database
but will no longer be accessible.


.. include:: /common/global.rst

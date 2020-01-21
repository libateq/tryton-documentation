Menus
=====

For each user, the menu items that appear in the main menu can be adjusted.
You can see, and adjust, what menu items are displayed to users of a group from
the :tryton:menu:`ir.menu_menu_list` menu item.  Use the
:tryton:toolbar:`switch` button on the toolbar to change view and see the
detailed information about each menu item.


Access Controls
---------------

Each menu item has a :tryton:field:`~ir.ui.menu.groups` field that is used to
list the groups that should have access to the menu item.  Menu items that a
user is not allowed to access are hidden from the main menu.

.. note::

    Hiding a menu item does not stop a user from running an action, it only
    removes it from the menu.  To stop a user from using the action that it
    triggers you must also restrict the user's access to it's
    :ref:`administration/system/access/actions:Actions`.


How Access is Controlled
------------------------

Menu items are only displayed in the main menu, if:

* there are no groups associated with the menu item, or
* the user is in a group that is listed in the
  :tryton:field:`~ir.ui.menu.groups` field for the menu item.

.. tip::

    Sub menu items are not repositioned in the menu if their parent menu item
    is hidden, so you only need to hide one menu item to remove a whole
    section from the main menu.


.. include:: /common/global.rst

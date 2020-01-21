.. inherit:: inside administration/system/user,//section[title=="Preferences"]/bullet_list/list_item[3]

.. tip::

    You can make the user's dashboard open automatically when they login by
    adding it to the list of actions.


.. inherit:: inside administration/system/user,//section[title=="Preferences"]/bullet_list
    :filter: ./bullet_list/list_item


* :tryton:field:`~res.user.dashboard_layout`:
  This field allows the user to specify the layout of the items on their
  dashboard.  There are two main types of layout:

  * ``Square`` which lays the items out so that they are all an equal size, and
  * ``Stack`` which makes the first item on the dashboard the largest and then
    the other items are all made the same smaller size and are placed along the
    specified edge.

* :tryton:field:`~res.user.dashboard_actions`:
  This is a list of the items that should appear on the users dashboard.

  .. note::

      Only :ref:`administration/system/core/actions:Windows` actions that have
      been marked with ``dashboard`` in the
      :tryton:field:`~ir.action.act_window.usage` field can be used on
      dashboards.

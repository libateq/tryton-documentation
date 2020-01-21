Models
======

Access to information that is stored in Tryton models is controlled based
on the settings found in :tryton:menu:`ir.menu_model_access_form`.  Opening
this view will show you a list of the model access records that define the
access permissions to models that are in currently in use on the system.
You can see more detailed information by clicking on the
:tryton:toolbar:`switch` button on the toolbar.

.. hint::

    Access to a subset of the records stored in a model can be controlled
    using :ref:`administration/system/access/rules:Record Rules` which may
    affect how the settings from the model access records are used.


Access Controls
---------------

The fields that are used to control the access to the model are:

:tryton:field:`~ir.model.access.perm_read`
  This controls whether records in the model can be read and viewed by the
  user.  It also applies when searching for records in the model.

:tryton:field:`~ir.model.access.perm_write`
  The write access to the model is controlled using this field, users
  that do not have this permission cannot change any data stored in the
  model.

:tryton:field:`~ir.model.access.perm_create`
  When records are created this is the access permission that is checked to
  ensure that the user is allowed to add new records to the model.

:tryton:field:`~ir.model.access.perm_delete`
  Access to this permission allows users to remove the records from the
  model.

The :tryton:field:`~ir.model.access.group` field links the access permissions
to users that belong to specific group.  Any model access records that
do have an empty :tryton:field:`~ir.model.access.group` are applied to all
users.


How Access is Controlled
------------------------

A user will be granted an access permission to the model if:

* there are no model access records at all for the model, or
* all the model access records for the model are associated with a group,
  or
* there is a model access record that is not associated with any group that
  grants the access permission, or
* there is a model access record that is associated with a group the user
  is a member of and that grants the access permission.

.. tip::

    To prevent access to a model by default, create an model access record
    that doesn't grant any permissions and don't associate a group with it.
    Also ensure that there are no other model access records with an empty
    :tryton:field:`~ir.model.access.group` field that may be granting
    permissions to the model.  Once you have done this you can then create
    model access records for each group needs access permission to the
    model.


.. include:: /common/global.rst

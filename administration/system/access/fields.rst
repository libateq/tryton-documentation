Fields
======

The data that is stored in the fields from Tryton
:ref:`administration/system/access/models:Models` can be controlled.  Opening
the :tryton:menu:`ir.menu_model_field_access_form` allows you to see and alter
the permissions different groups of users have to the fields.
More detailed information for each field can be seen by clicking on the
:tryton:toolbar:`switch` button on the toolbar.


Access Controls
---------------

Access to fields and models are controlled in a similar way.  Access is
controlled by:

:tryton:field:`~ir.model.field.access.perm_read`
  The ``read`` permission allows you to control which groups of users are
  allowed to look at the information stored in the field.

  .. note::

      Any fields for which the user does not have ``read`` permission are
      automatically removed from any views they appear in.

:tryton:field:`~ir.model.field.access.perm_write`
  This permission controls whether the user is allowed to set or update the
  data in the field.  It is checked whenever a new value is written to the
  field, including when the record is first created.

:tryton:field:`~ir.model.field.access.perm_create`
  This permission is used by the client to control whether records in linked
  models can be created directly from this field.

  .. note::

      The user must also have the ``create`` permission on the linked model in
      order to create the new records when the current record is saved.

:tryton:field:`~ir.model.field.access.perm_delete`
  This permission is also used by the client on fields that link records
  together.  It controls whether records in the linked model can be deleted
  using this field.

  .. note::

      The user must also have the ``delete`` permission on the linked model in
      order to remove the records when the current record is saved.

The :tryton:field:`~ir.model.field.access.group` field links the access
permissions a group of users.  Any field access records that have an empty
:tryton:field:`~ir.model.field.access.group` are applied to all users.


How Access is Controlled
------------------------

A user is granted access permissions to the field if:

* there are no field access records at all for the field, or
* all the field access records for the field are associated with a group,
  or
* there is a field access record that is not associated with any group that
  grants the access permission, or
* there is a field access record that is associated with a group the user
  is a member of and that grants the access permission.

.. tip::

    If you want to prevent access to a field, then create a field access
    record that doesn't grant any permissions and that's not associated with a
    group.  Also ensure that there are no other field access records with an
    empty :tryton:field:`~ir.model.field.access.group` field that may be
    granting permissions to the field.  Once you have done this you can then
    create field access records for each group needs access to the field.


.. include:: /common/global.rst

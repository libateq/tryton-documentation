Record Rules
============

Record rules allow access to be restricted to specific sets of records.
This can be used, for example, to only allow certain groups of users
access to a set of products.

Record rules define the conditions that records must meet for the user to
be granted access to them.  Record rules can be managed by opening the
:tryton:menu:`ir.menu_rule_group_form` menu item.


Access Controls
---------------

Each record rule provides the following settings that affect how access is
granted to sets of records:

:tryton:field:`~ir.rule.group.model`
  This is the model on which the record rule applies.

:tryton:field:`~ir.rule.group.rules`
  These define the domains that select the sets of records that the
  record rule will apply to.

:tryton:field:`~ir.rule.group.perm_read`
  This controls whether records that match the record rule can be read by
  the user.

  .. note::

      Any records that a user does not have permission to ``read`` are
      filtered out of any search results.

:tryton:field:`~ir.rule.group.perm_write`
  The ``write`` permission indicates whether the user will be allowed to
  change the contents of records that match the record rule.

:tryton:field:`~ir.rule.group.perm_create`
  This permission is checked when new records that match the record rules
  are added to the model.

:tryton:field:`~ir.rule.group.perm_delete`
  This is the access permission that controls whether records that match the
  record rule can be removed from the model.

:tryton:field:`~ir.rule.group.global_p`
  This flag is used to make the rule global, so that it is applied to all
  users.

:tryton:field:`~ir.rule.group.default_p`
  This flag is used to make the rule apply to users by default.

:tryton:field:`~ir.rule.group.groups`
  This is the list of groups whose members the record rule will be applied
  to.

  .. note:

      Only record rules that are not global or default can be
      associated with groups.


How Access is Controlled
------------------------

Access is granted to a record if:

* the user belongs to a group that contains a record rule that matches the
  record, and the record rule grants them access, or
* there is a default matching record rule that grants access to the record, or
* there is a global matching record rule that grants access to the record, or
* there is no record rule at all that matches the record.


.. include:: /common/global.rst

Managing Reports
================

The reports that are available on your system can be viewed and modified by
opening the :tryton:menu:`ir.menu_action_report_form` menu item.  Once you
have opened this view you will see a list of the reports that are currently
available on your system.  You can :tryton:toolbar:`switch` to a more detailed
view to see the properties of the reports.

.. tryton:view:: ir.action_report_view_form /images/ir_action_report.png

    Screenshot of the Report form.


Creating and Updating Reports
-----------------------------

Reports can be added to the system, and changed in the same way as any other
record in Tryton.

.. tip::

    Most reports can be deleted from the system when you no longer need them.
    However, instead of deleting reports, it can often be better to deactivate
    them by unticking the :tryton:field:`~ir.action.report.active` field.

    Deactivated reports are not available for use, and are normally hidden.
    You can still access the records for the deactivated reports by using the 
    :tryton:toolbar:`Show Inactive Records` button when filtering.  This
    allows you to reactivate the reports if you ever need to.

.. note::

    Some of the reports are added to the system when you activate modules.
    These standard reports cannot be deleted as they are part of the base
    configuration, but you can deactivate them.

At some point you will probably find that you want to change the template that
is associated with a report.  This is done by:

* finding the report and opening the detailed view of it,
* opening the template contained in the 
  :tryton:field:`~ir.action.report.report_content` field,
* making your modifications to the 
  :ref:`Report Template <administration/system/reports/templates:Report Templates>`,
  and saving the file to somewhere you can find it,
* clearing the :tryton:field:`~ir.action.report.report_content` field,
* using the :tryton:field:`~ir.action.report.report_content` field to select
  your updated template file.


Properties
----------

:tryton:field:`~ir.action.report.name`
    The name of the report, it is normally best to choose a name that makes
    it clear what the report does, or is used for.

:tryton:field:`~ir.action.report.translatable`
    Unticking this field will disable translations for the report.  This is
    useful for reports that it makes no sense to try and translate, and
    can improve system performance for those reports and for other tasks
    related to :ref:`administration/system/localisation:Localisation`.

:tryton:field:`~ir.action.report.single`
    This checkbox allows you to specify whether the template has been designed
    to only handle a single record at a time (ticked), or can work with one
    or more records in one go (unticked).

:tryton:field:`~ir.action.report.direct_print`
    Ticking this field will make the client attempt to automatically print the
    report rather than opening it.

    .. note::

        Sending a report directly to the printer may fail on clients where
        there are no printers available, or on clients that do not support
        sending reports directly to the printer.  In this case the client
        will normally attempt to save or open the report instead.

:tryton:field:`~ir.action.report.model`
    This is the model that provides the records that are used by the report.
    The model should be referred to by it's internal name.

    .. tip::

        A model's internal name can be found by opening the
        :tryton:menu:`ir.menu_model_form` menu item, finding the model, and
        looking in the :tryton:field:`~ir.model.model` field.

:tryton:field:`~ir.action.report.report_name`
    This is the internal name used for the report, it should be formatted
    similarly to the :tryton:field:`~ir.action.report.model`, and can in
    some cases be the same value.

:tryton:field:`~ir.action.report.icon`
    The icon associated with the report, not normally used or displayed, and
    can be left blank.

:tryton:field:`~ir.action.report.report_content`
    This field contains the template that is used to generate the report.

:tryton:field:`~ir.action.report.report`
    For modules that provide reports, this is the path to the template that
    is used by default for the report.  For reports that you create you will
    not need to fill this in.

:tryton:field:`~ir.action.report.template_extension`
    This is the file format that the template is in.

:tryton:field:`~ir.action.report.extension`
    This is the file format that you want the generated report to be in.  Once
    the report has been created from the template, the resulting file will
    be converted to this file format before being sent to the user or printer.
    If this is not filled in then no conversion will be attempted and the
    report will be in the same file format as the template.

    .. important::

        To convert reports into different file formats you must have
        LibreOffice_ installed and configured on the server that is running
        the :ref:`administration/services/trytond:trytond` service.

:tryton:field:`~ir.action.report.email`
    In clients that support opening a report as an attachment to a new email
    in an external email program.  This field allows you to specify the
    default values the ``cc``, ``to``, and ``subject`` fields of the new
    email.

:tryton:field:`~ir.action.report.keywords`
    This field allows you to define a list of the events that can be used to
    open the report.  You will normally want to use the ``Print form``
    :tryton:field:`~ir.action.keyword.keyword` to add the report to the Print
    menu in the client.  You must also set the
    :tryton:field:`~ir.action.keyword.model` that the report can be used with.
    If you also set the record part of the
    :tryton:field:`~ir.action.keyword.model` field, then the report will only
    appear for that particular record.

:tryton:field:`~ir.action.report.groups`
    The groups field contains a list of the groups whose members are allowed
    to use the report.  More information on user access controls can be
    found in the :ref:`administration/system/access/index:Access Management`
    section.


.. include:: /common/global.rst

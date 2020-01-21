Report Templates
================

The dynamic reports that Tryton can generate are built from a template.
The template provides the layout and styling for the report and contains the
directives and expressions that control what data gets inserted into the
report and where it gets put.

Tryton uses Relatorio_ to dynamically generate reports.  The directives and
expressions that Relatorio supports are from the Genshi_ templating language.


File Formats
------------

The templates must be in one of the supported file formats:

* OpenDocument Text (``odt``),
* OpenDocument Presentation (``odp``),
* OpenDocument Spreadsheet (``ods``),
* OpenDocument Graphics (``odg``),
* Plain Text (``txt``),
* XML (``xml``),
* HTML (``html``),
* XHTML (``xhtml``).

Once the report has been created it can be automatically converted to another
format supported by LibreOffice_, as long as LibreOffice is installed and
configured on the server that is running the
:ref:`administration/services/trytond:trytond` service.


Directives
----------

The template directives are special instructions that are used by the
templating engine to enclose parts of the template and control how the
template is rendered.  They allow you to repeat sections of the template or
only include parts of the template if certain conditions are met.

The exact syntax needed to include a directive in your template differs between
each of the supported file formats and is described in the
:ref:`administration/system/reports/templates:Including Directives and Expressions`
section.  However the available directives are the same for all the file
formats.

The supported directives are:

for
    The ``for`` directive is used to loop through the values in a list.  This
    allows you to create parts of a template that get copied and filled in for
    each item in the list.

    The ``for`` directive works in the same way as the ``for`` statement in
    Python_.  It takes a parameter, normally of the form ``item in items``,
    where ``items`` is the list (or iterable) to loop through and ``item`` is
    the variable to use inside the for loop.

    The part of the template that is enclosed in the ``for`` loop is copied
    for each item in the list.  For each of these copies the variable
    (``item`` in the example above) is set to the corresponding value from the
    list.

if
    The ``if`` directive allows you to conditionally include, or exclude, parts
    of the template from the final report.

    The ``if`` directive takes a parameter that gets evaluated to either a
    ``True`` or ``False`` value.

    The part of the template that is enclosed in the ``if`` directive only gets
    included in the final report if the parameter evaluates to ``True``.

choose
    The ``choose`` directive allows you to include one of several alternative
    parts of your template in the final report.  Inside the ``choose``
    directive there must be one or more parts starting with a ``when``
    directive and optionally a part starting with an ``otherwise`` directive.

    when
        The ``when`` directive should appear inside a ``choose`` directive
        and at the start of a part of the template to optionally include in
        the final report.

        The ``when`` directive takes a single parameter that is either
        evaluated, or compared to the parameter from the ``choose`` directive.

    otherwise
        The ``otherwise`` directive, if included, should appear at the start
        of the last part of a ``choose`` directive.

    When a ``choose`` directive is encountered the part of the template after
    the first matching ``when`` directive is included in the final report.
    If no ``when`` directives match and there is a ``otherwise`` directive
    then the part starting with the ``otherwise`` directive is included in the
    final report.

    The ``choose`` directive can operate in two different ways.
    If the ``choose`` directive has a parameter, then matches are found by
    comparing the ``when`` directive's parameters to the one from the
    ``choose`` directive.  
    If the ``choose`` directive has no parameter, then matches are found by
    evaluating the ``when`` directive's parameters.  Any parameters that
    evaluate to ``True`` are considered to have matched.

with
    The ``with`` directive allows you to assign expressions to variables,
    which can be used to make expressions inside the directive less verbose
    and more efficient.


Expressions
-----------

Template expressions allow you to dynamically substitute parts of the template
with variable data taken from your Tryton system.  The method you use to
include these in the report differs between the different file formats and is
described in the
:ref:`administration/system/reports/templates:Including Directives and Expressions`
section.

A template expression is a standard Python_ expression.  The report's context
contains the variables and functions that can be used in the template
expressions.  The context is set when the report is generated, and it's exact
contents depends on the specific type of report.  However, normally the
context will contain at least:

* the ``records``, or ``record`` (if the
  :tryton:field:`~ir.action.report.single` field is ticked for the report),
  that the report is being generated for,
* the ``user`` that is generating the report,
* the ``datetime`` object that can be used to get the current date and time,
* some functions that can be used to format numbers
  (``format_number(value, lang, [[[digits], grouping], monetary])``),
  currencies (``format_currency(value, lang, currency, [[symbol], grouping])``)
  and dates (``format_date(value, [lang])``) for specific locales,

.. note::

    It is possible to add any data from your Tryton system to reports.
    However, if the data is not available in the existing report's context,
    then you will need to create a new module and extend or add a new report
    type in order to do this.

Here are some examples of how these variables and functions may be used:

.. code:: python3

    # These first few examples assume the record, and records are from the
    # Groups model,

    # Get the group's name
    record.name

    # Get the number of users in the first group
    len(records[0].users)

    # Get the name of the first group's first user
    records[0].users[0].rec_name

    # Get the user's name
    user.rec_name

    # Get the current date and time
    datetime.datetime.now()

    # Format the current date to the transactions language format
    format_date(datetime.date.today(), None)

    # Format an amount of money
    # (note: euros must be a Currency defined in the context)
    format_currency(123.45, None, euros, True, True)
    # "€123.45"

    # Format a number to 2 decimal places and group the digits
    format_number(12345.6789, None, 2, True) 
    # "12,345.68"


Including Directives and Expressions
------------------------------------

The exact syntax that you need to use to include directives and expressions in
your template depends on the type of template file that you are using.  There
are three main types of template file that are supported.

OpenDocument Files
^^^^^^^^^^^^^^^^^^

The directives and expressions in OpenDocument files should be included in the
document in ``Placeholder`` ``Text`` fields.  Each directive must be closed
using a separate ``Placeholder`` ``Text`` field that contains a marker that
closes the directive.

In LibreOffice the ``Placeholder`` ``Text`` fields can be inserted into the
document from the ``Fields`` window.  In LibreOffice Writer by default this
window can be opened by pressing ``Ctrl+F2``, or by using the
*Insert* / *Field* / *More Fields...* menu item.  With this window open,
in the *Functions* tab, you will need to select ``Placeholder`` from the list
of *Types* and ``Text`` from the list of *Formats*.  The directive, or
expression, you want to use should be entered into the *Placeholder* field.

Each directive must be placed on it's own line, or table cell, in the template.
Any lines in the template that contain a directive are removed from the final
report, so any text or other items that appears on the same line as the
directive will not be output.  The same applies to items in the same table
cell as a directive.

Fields that contain expressions are evaluated and replaced with the result of
the expression.  Everything before and after the field containing the
expression will appear in the final report.

.. tip::

    Tables with variable numbers of columns can be created in OpenDocument Text
    templates.  This is done by putting a ``for`` directive in the first
    column, and an ``/for`` directive in the last column.  The columns that
    are between these directives will be repeated for each value, and the
    first and last columns that contain the directives will not appear in the
    final report.

.. tip::

    Dynamic images can be included in the template by creating a ``Frame``, and
    setting the *Name* to ``image: expression``, where expression must evaluate
    to a tuple containing two elements.  The first element must be the image
    data, and the second element must be the mime type of the image data.
    For example ``image: (record.image, "image/png")``.

    In LibreOffice Writer ``Frames`` can be added by using the
    *Insert* / *Frame* / *Frame...* menu item, and the *Name* field can be
    found on the *Options* tab.

The syntax for the text to use in the *Placeholder* fields for directives is:

.. code::

    for each="item in items"
    /for

    if test="condition"
    /if

    choose test="value"
      when test="expression"
      /when
      otherwise
      /otherwise
    /choose

    with vars="a=expression; b=expression"
    /with

When these have been entered into a ``Placeholder`` ``Text`` field LibreOffice
will display them inside ``<`` ... ``>`` brackets.  These brackets should not
be entered as part of the ``Placeholder`` ``Text``.

In this example of a OpenDocument Text template, the sections between the
``<`` ... ``>`` brackets should be entered as ``Placeholder`` ``Text`` fields,
and the table should be a proper table inserted into the template.

.. code::

    The number of user records selected
    <choose test="len(records)">
    <when test="0">
    No user records selected.
    </when>
    <when test="1">
    1 user record selected.
    </when>
    <otherwise>
    <len(records)> user records selected.
    </otherwise>
    </choose>

    Number of groups each user is in:
    +========================+========================+
    | User                   | Num Groups             |
    +========================+========================+
    | <for each="record in records">                  |
    +------------------------+------------------------+
    | <record.name>          | <len(record.groups)>   |
    +------------------------+------------------------+
    | </for>                                          |
    +=================================================+

    Report run at: <datetime.datetime.now()>
    <if test="user.name == 'Administrator'">
    This report was generated by the Administrator.
    </if>


Text Files
^^^^^^^^^^

Within text files the directives should be enclosed with ``{%`` ... ``%}``
characters.  Each directive needs to be terminated using an ``{% end %}``
marker.  To suppress the newlines that appear after a directive use a single
backslash (``\``) character.

Expressions are included inside ``${`` ... ``}`` characters.

Example:

.. code::

    The number of user records selected:
    {% choose len(records) %}\
      {% when 0 %}No user records selected.{% end %}\
      {% when 1 %}1 user record selected.{% end %}\
      {% otherwise %}${ len(records) } user records selected.{% end %}\
    {% end %}

    Number of groups each user is in:
    {% for record in records %}\
      ${ record.name }: ${ len(record.groups) } 
    {% end %}\

    Report run at: ${ datetime.datetime.now() }
    {% if user.name == "Administrator" %}\
    This report was generated by the Administrator.
    {% end %}\


XML, HTML and XHTML Files
^^^^^^^^^^^^^^^^^^^^^^^^^

For HTML and XML based files the directives can be specified as elements or
attributes in the template.  They are identified by the namespace
``http://genshi.edgewall.org/``.  To correctly use the directives in the
template the namespace must be declared, which is normally done on the root
element (e.g. ``<html xmlns:py="http://genshi.edgewall.org/">``).

The directives can be included in the the template as either attributes or
elements.

As attributes:

.. code:: html

    <div py:for="item in items"></div>
    <div py:if="condition"></div>
    <div py:choose="value">
      <span py:when="expression"></span>
      <span py:otherwise></span>
    </div>
    <div py:with="a=expression; b=expression"></div>

As elements:

.. code:: html

    <py:for each="item in items"></py:for>
    <py:if test="condition"></py:if>
    <py:choose test="value">
      <py:when test="expression"></py:when>
      <py:otherwise></py:otherwise>
    </py:choose>
    <py:with vars="a=expression; b=expression"></py:with>

Example:

.. code:: html

    <!DOCTYPE html>
    <html xmlns:py="http://genshi.edgewall.org/">
      <head>
        <title>User Report</title>
      </head>
      <body>
        <p>
          The number of user records selected:<br/>
          <span py:choose="len(records)">
            <py:when test="0">No user records selected.</py:when>
            <py:when test="1">1 user record selected.</py:when>
            <py:when test="len(records)">${ len(records) } user records selected.</py:when>
          </span>
        </p>

        <p>
          Number of groups each user is in:
          <ul>
            <py:for each="record in records">
              <li>${ record.name }: ${ len(record.groups) }</li>
            </py:for>
          </ul>
        </p>

        <p>
          Report run at: ${ datetime.datetime.now() }
          <py:if test="user.name == 'Administrator'">
          <br/>This report was generated by the Administrator.
          </py:if>
        </p>
      </body>
    </html>


.. include:: /common/global.rst

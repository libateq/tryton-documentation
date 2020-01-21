.. inherit:: inside administration/configuration/options,//section[title=="Sections"]

timesheet_cost
^^^^^^^^^^^^^^

This section allows you to configure the system wide settings that are
required for the timesheet_cost module.

price_decimal
    The price_decimal configuration option sets the number of decimal places
    that are available for use with the employee's hourly cost price.

    .. important::

        Once the database has been created you cannot lower this value.

    The default number of decimal places for hourly cost prices is ``4``.

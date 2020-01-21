.. inherit:: inside administration/configuration/options,//section[title=="Sections"]

product
^^^^^^^

The product section allows you to configure the system wide settings that are
required for the product module.

price_decimal
    The price_decimal configuration option sets the number of decimal places
    that are available for the unit prices of products.

    .. important::

        Once the database has been created you cannot lower this value.

    The default number of decimal places for unit prices is ``4``.

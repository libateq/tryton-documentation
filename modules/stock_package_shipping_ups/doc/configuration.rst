.. inherit:: inside administration/configuration/options,//section[title=="Sections"]

stock_package_shipping_ups
^^^^^^^^^^^^^^^^^^^^^^^^^^

This section allows you to configure the settings for shipping packages using
UPS.

production
    This is the production URL to use when connecting to UPS API for shipping
    packages. 

    This defaults to ``https://onlinetools.ups.com/json/Ship``.

testing
    This is the URL to use when testing the UPS API.

    This defaults to ``https://wwwcie.ups.com/json/Ship``.

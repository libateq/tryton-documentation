.. inherit:: inside administration/configuration/options,//section[title=="Sections"]

stock_package_shipping_dpd
^^^^^^^^^^^^^^^^^^^^^^^^^^

This section allows you to configure the settings for shipping packages using
DPD.

production
    This is the production URL to use when connecting to the DPD API for
    shipping packages. 

    This defaults to ``https://public-ws.dpd.com/services/``.

testing
    This is the URL to use when testing the DPD API.

    This defaults to ``https://public-ws-stage.dpd.com/services/``.

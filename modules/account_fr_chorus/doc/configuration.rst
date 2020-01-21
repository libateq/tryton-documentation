.. inherit:: inside administration/configuration/options,//section[title=="Sections"]

account_fr_chorus
^^^^^^^^^^^^^^^^^

This section allows you to configure the settings required to send invoices
through the `Chorus Pro`_ portal.

url
    The base url that is used when connecting to the Chorus Pro portal.

    The url defaults to ``https://chorus-pro.gouv.fr:5443``.

certificate
    This is the path to the certificate that is needed to connect to the
    Chorus Pro portal.

privatekey
    This is the path to the private key that is needed when connecting to the
    Chorus Pro portal.

    .. important::

        The private key must be unencrypted otherwise Tryton will not be able
        to use it.

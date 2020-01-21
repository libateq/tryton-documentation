.. inherit:: inside administration/configuration/options,//section[title=="Sections"]

account_payment_sepa
^^^^^^^^^^^^^^^^^^^^

This section contains the configuration options that allow you to adjust some
of the settings related to SEPA payments.

filestore
    This option allows you to decide whether SEPA messages get saved in the
    database, or in the file store with other data files.  To store SEPA
    messages in the database set this to ``False``.

    By default this option is set to ``True`` and SEPA messages get stored in
    the file store.

store_prefix
    This option allows you to add a prefix to use with the file store.

    By default there is no prefix for SEPA messages that are stored in the
    file store.

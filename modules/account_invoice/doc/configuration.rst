.. inherit:: inside administration/configuration/options,//section[title=="Sections"]

account_invoice
^^^^^^^^^^^^^^^

This section contains the configuration options that allow you to adjust some
settings related to invoicing.

filestore
    This option allows you to decide whether invoices get saved in the
    database, or in the file store with other data files.  To store invoices
    in the database set this to ``False``.

    By default this option is set to ``True`` and invoices get stored in the
    file store.

store_prefix
    This option allows you to add a prefix to use with the file store.

    By default there is no prefix for invoices that are stored in the
    file store.

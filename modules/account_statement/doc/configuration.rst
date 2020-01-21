.. inherit:: inside administration/configuration/options,//section[title=="Sections"]

account_statement
^^^^^^^^^^^^^^^^^

This section contains the configuration options that allow you to adjust some
settings related to statements.

filestore
    This option allows you to decide whether the original files that get
    imported are saved in the database, or in the file store with other data
    files.  To use the database for the origin files set this to ``False``.

    By default this option is set to ``True`` and the original files that
    get imported are stored in the file store.

store_prefix
    This option allows you to add a prefix to use with the file store.

    By default there is no prefix for origin files that are stored in the
    file store.

.. inherit:: inside administration/configuration/options,//section[title=="session"]/definition_list/definition_list_item[1]//definition_list
    :filter: ./definition_list/definition_list_item

ldap
    This authentication method allows Tryton to authenticate users against an
    LDAP server using the login name and password that they provide.  This
    enables them to use the same password for a range if different services.

.. inherit:: inside administration/configuration/options,//section[title=="Sections"]

ldap_authentication
^^^^^^^^^^^^^^^^^^^

This section allows you to configure the settings to use when connecting to an
LDAP server for user authentication.

uri
    This option allows you to set the LDAP URL for the LDAP service that is
    used for the user authentication.  It should be in format specified by
    RFC-2255_.

bind_pass
    If you need to bind to the LDAP server in order to perform the
    authentication then this should be set to the password used for the bind
    operation.

    .. caution::

        Take care to ensure that only the user running the ``trytond`` service
        can access the configuration file if you are storing a bind password
        in it.

    .. tip::

        Try and setup LDAP authentication without binding to the server if at
        all possible.

uid
    The attribute on the LDAP server that contains the user's login name.

    By default the ``uid`` attribute is assumed to contain the user's login
    name.

create_user
    This indicates whether a new user should be created on Tryton if the user
    successfully authenticates, but no user already exists on the system.
    Set this to ``True`` to automatically create new Tryton users as required.

    If not specified this option defaults to ``False``.

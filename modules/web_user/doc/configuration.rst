.. inherit:: inside administration/configuration/options,//section[title=="web"]/definition_list
    :filter: ./definition_list/definition_list_item

email_validation_url
    The email validation URL is the address which is used for email validation
    of web users.  A token parameter will be automatically added to this URL
    when it is used.

reset_password_url
    This option allows you to set the URL which is sent to the web user when
    they are attempting to reset their password.  An email address and token
    will be automatically added to this URL when it is used.

.. inherit:: inside administration/configuration/options,//section[title=="session"]/definition_list
    :filter: ./definition_list/definition_list_item

web_timeout
    This is the time in seconds that a web session is valid for.

    The default web timeout is ``2592000`` seconds (30 days).

web_timeout_reset
    This is the length of time that a web user password reset token is valid
    for.  After this time the web user will need to make another request to
    reset their password.

    The default reset timeout is ``86400`` seconds (1 day).

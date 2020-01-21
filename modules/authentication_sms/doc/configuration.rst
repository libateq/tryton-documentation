.. inherit:: inside administration/configuration/options,//section[title=="session"]/definition_list/definition_list_item[1]//definition_list
    :filter: ./definition_list/definition_list_item

sms
    This authentication method sends a code to the user via an SMS text
    message.  They must then enter this code in when requested.

    In order to use this authentication method the user must have a mobile
    phone number saved on the system.

password_sms
    This authentication method sends a code to the user via an SMS text
    message only once they have provided a valid password for their account.
    Using this authentication method provides `two-factor authentication`_.

    In order to use this authentication method the user must have a mobile
    phone number saved on the system.

.. inherit:: inside administration/configuration/options,//section[title=="Sections"]

authentication_sms
^^^^^^^^^^^^^^^^^^

This section is used to configure the settings for authentication via SMS text
messages.

function
    This is the fully qualified name of the method that is used to send the
    SMS text message.  This configuration option is required to be able to
    send SMS text messages.

from
    This is the number from which the SMS text messages are sent.

length
    This is the length of the generated code.

    The default length is ``6`` characters.

ttl
    The number of seconds that the generated code is valid for, also known as
    the time to live (ttl) for the code.

    Generated codes are by default valid for ``300`` seconds (5 minutes).

name
    This is the name used in the SMS text message.

    The name defaults to ``Tryton``.

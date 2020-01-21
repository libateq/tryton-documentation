.. inherit:: inside administration/system/scheduled-actions,//section[title=="Available Methods"]/definition_list
    :filter: ./definition_list/definition_list_item

Charge Stripe Payments
    This method is used to connect to stripe and charge customers for any
    payments that are due.  The status of the payments are updated
    appropriately.

Capture Stripe Payments
    This method is used to connect to stripe and capture the payments and is
    the second of the two-step payment flow.

Create Stripe Customer
    This will create new customers on Stripe.

Delete Stripe Customer
    This will delete customers from Stripe if they have been deactivated on the
    system.

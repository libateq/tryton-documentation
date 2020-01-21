.. inherit:: inside administration/system/scheduled-actions,//section[title=="Available Methods"]/definition_list
    :filter: ./definition_list/definition_list_item

Generate Subscription Line Consumptions
    This method creates the consumptions for reoccuring sales subscriptions.
    The sales subscription must be running, and the next consumption must be
    due.

Generate Subscription Invoices
    This method generates invoices for sales subscriptions that are currently
    running.  Only subscriptions that have consumptions available can
    generate an invoice, and only if the next invoice date for the
    subscription has passed.

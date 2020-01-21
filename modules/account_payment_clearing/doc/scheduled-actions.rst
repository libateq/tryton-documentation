.. inherit:: inside administration/system/scheduled-actions,//section[title=="Available Methods"]/definition_list
    :filter: ./definition_list/definition_list_item

Post Clearing Moves
    This method automatically posts clearing moves.  The moves that are posted
    are only in journals that have a
    :tryton:field:`~account.payment.journal.clearing_posting_delay` set and
    that happened far enough back in time for the delay to have now passed.

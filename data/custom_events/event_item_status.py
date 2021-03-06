"""
Item status filter

Tested on Fri, 14 Aug, 01:35 AM
"""

import aux
import json

def operate(mode, options):
    """ Driver for get_status
    Implements the query_event_driver specification
    """

    if 'item_status' not in options:
        return None, None, None
    item_status = options['item_status']
    if not isinstance(item_status, list):
        item_status = [item_status]
    return get_status(mode, item_status)

def get_status(mode, item_status):
    query = """
    SELECT so.fk_customer, sois.name FROM sales_order so
    JOIN sales_order_item soi ON so.id_sales_order = soi.fk_sales_order
    JOIN sales_order_item_status sois on sois.id_sales_order_item_status = soi.fk_sales_order_item_status
    WHERE sois.name in (%s)
    """ % json.dumps(item_status).strip("[]")

    return aux.typical_event_routing(mode, query, ['Item Status'])

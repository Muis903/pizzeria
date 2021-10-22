#
# IMPORTING necessary libraries and scripts.
#


import ast
import json
import yaml


#
# DEFINING functions.
#


def save_order(order_id, order):
    """SAVING AN ORDER TO THE ORDERS JSON."""
    # Saving a new order in a dictionary.
    order_id_to_order = {order_id: order}
    print(order_id_to_order)
    print("The new order is successfully saved!")

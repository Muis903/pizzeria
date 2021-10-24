#
# IMPORTING necessary libraries and scripts.
#


import ast
import json

#
# DEFINING functions.
#

def add_staff():
    """Add new staff and save it in the list."""

    #Data
    name = "Name: " + input("First and last name: ")
    birthday = "Birthday: " + input("Birthday dd/mm/yyyy: ")
    login = "Login: " + input("Login: ")
    password = "Password: " + input("Password: ")
    function = "Function: " + input("Function: ")

    #Create profile
    profile = [name, birthday, login, password, function]

    #Add and save profile
    try:
        with open ('data.json', "a+") as data:
            if profile in data:
                pass
            else:
                for i in profile:
                    data.write(("\n|" + i + "|").replace('"',''))

    except FileNotFoundError:
        with open ('data.json', "a+") as data:
            for i in profile:
                data.write(("\n|" + i + "|").replace('"',''))




def save_order(order_id, order):
    """SAVING AN ORDER TO THE ORDERS JSON."""
    # Saving a new order in a dictionary.
    order_id_to_order = {order_id: order}
    print(order_id_to_order)
    print("The new order is successfully saved!")


#
# <--- Test Function --->
#

add_staff()

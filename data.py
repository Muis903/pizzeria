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
    name = input("First and last name: ")
    birthday = input("Birthday dd/mm/yyyy: ")
    login = input("Login: ")
    password = input("Password: ")
    function = input("Function: ")

    #Create profile
    profile = str("\n" + "Name: " + name.title() + "\n"
        + "Birthday: " + "\n" + "Login: " + login + "\n" + "Password: " + password + "\n" + "Function: " + function)
    return profile

    #Add and save profile
    try:
        with open ('data.json', "r+") as data:
            if profile in data:
                pass
            else:
                json.dump(profile, data)
    except FileNotFoundError:
        with open ('data.json', "w") as data:
            json.dump(profile, data)




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

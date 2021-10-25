#
# IMPORTING necessary libraries and scripts.
#


import json


#
# DECLARING global variables.
#


staff_json = "staff.json"


#
# DEFINING functions.
#


def get_new_staff():
    """Get new staff and save it into the json."""

    #Data
    name = input("First and last name: ")
    birthday = input("Birthday dd/mm/yyyy: ")
    login = input("Login: ")
    password = input("Password: ")
    function = input("Function: ")

    # Saving new staff.
    save_new_staff(name, birthday, login, password, function)


def save_new_staff(name, birthday, login, password, function):
    """Save new staff in json file format."""
    
    #Create an object as a profile in the form of Python dictionary.
    profile = {
        "name": name,
        "birthday": birthday,
        "login": login,
        "password": password,
        "function": function
    }

    # Putting the profile into the staff.json.
    with open(staff_json, 'w') as file:
        # Dumping the profile to the file with indent of 4 spaces.
        json.dump(profile, file, indent=4)


#
# <--- Test Function --->
#

get_new_staff()

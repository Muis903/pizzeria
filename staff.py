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


def get_new_staff() -> dict: # dat de functie retourneert dict (voor leesbaarheid bedoeld). Kan ook niet gebruiken. Verwirder deze omschrijving als duidelijk.
    """Get new staff and save it into the json."""

    #Data
    name = input("First and last name: ")
    birthday = input("Birthday dd/mm/yyyy: ")
    login = input("Login: ")
    password = input("Password: ")
    function = input("Function: ")
    
    #Create an object as a profile in the form of Python dictionary.
    profile = {
        "name": name,
        "birthday": birthday,
        "login": login,
        "password": password,
        "function": function
    }

    # Saving new staff.
    save_new_staff(profile)

    # Returning the profile to work with further if need it.
    return profile


def save_new_staff(profile:dict): # :dict geeft aan dat de attribuut dict MOET zijn. Er zijn nog :str, :list ezv. Verwijder de omschrijving als duidelijk.
    """Save new staff in json file format."""

    # Putting the profile into the staff.json.
    with open(staff_json, 'w') as file:
        # Dumping the profile to the file with indent of 4 spaces.
        json.dump(profile, file, indent=4)


#
# <--- Test Function --->
#

get_new_staff()

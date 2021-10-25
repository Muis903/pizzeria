#
# IMPORTING necessary libraries and scripts.
#


import os
import json


#
# DECLARING global variables.
#


# Defining staff.json file in order to keep track of all staff.
staff_json = "staff.json"


#
# DEFINING functions.
#


def get_new_person_profile() -> dict: # dat de functie retourneert dict (voor leesbaarheid bedoeld). Kan ook niet gebruiken. Verwirder deze omschrijving als duidelijk.
    """Get a new person profile and save it into the staff.json."""

    # Defining the person details.
    name, birthday, login, password, position = get_person_profile_input()

    #Create an object as a person profile in the form of Python dictionary.
    person_profile = create_person_profile(name, birthday, login, password, position)
    print("Created a new person profile.")

    # Saving the new person profile in staff.json file.
    save_new_person_profile(person_profile, position)
    print("The new person profile is successfully added into staff.json :)")

    # Returning the new person profile to work with further if need it.
    return person_profile


def get_person_profile_input() -> str:
    """Get an user input about person profile."""

    #Data
    name = input("First and last name: ")
    birthday = input("Birthday dd/mm/yyyy: ")
    login = input("Login: ")
    password = input("Password: ")
    position = input("Position: ")

    return (name, birthday, login, password, position)


def get_staff_positions() -> list:
    """Return all staff_positions inside of the company."""

    # Defining the positions inside of the company.
    # @dev Feel free to add more
    positions = [
        "junior", "medio", "senior", "team leader", "project leader", "manager"
    ]

    return positions




def create_person_profile(name=None, birthday=None, login=None, password=None, position=None): # None betekent dat de waarde van de parameter is niet vereist. Verwijder de omschrijving als duidelijk :)
    """Create and return a person profile."""
   
    profile = {
        "name": name,
        "birthday": birthday,
        "login": login,
        "password": password,
        "position": position
    }
    
    return profile




def check_for_staff_json_file():
    """Create staff.json if not already exists."""
    
    # GETting Current Working Directory.
    PATH = os.getcwd()
    
    # If staff.json not in the current working directory, then create one.
    if staff_json not in os.listdir(PATH):
        open(staff_json, 'w')
        print("Created new staff.json file.")
    else:
        print("Checked: found staff.json.")


def check_for_staff_json_template():
    """Create staff.json template and upload it to staff.json."""

    """
    @dev The implemantation of this function needs improvements because
         if you start adding new staff, the index 0 in will always have None as the value.
    """
    
    if staff_json_file_is_empty() == False:
        print("Checked: staff.json is not empty.")
    else:
        print("Creating a template in staff.json")
        # Getting all positions in the company.
        staff_positions = get_staff_positions()
        # Defining the person profile as Python dictionary.
        person_profile = dict()
        # Looping through all positions and adding to the template.
        for position in staff_positions:
            # Key/value pair, where position is a key and the rest is the value.
            person_profile[position] = [
                {   
                    "name": None,
                    "birthday": None,
                    "login": None,
                    "password": None,
                    "position": None
                }
            ]

        # Check for existance of staff.json file otherwise create it.
        check_for_staff_json_file()
        # Saving the template to staff.json.
        with open(staff_json, 'r+') as file:
            json.dump(person_profile, file, indent=4)




def save_new_person_profile(person_profile:dict, position:str): # :dict geeft aan dat de attribuut dict MOET zijn. Er zijn nog :str, :list ezv. Verwijder de omschrijving als duidelijk ;-)
    """Save new person profile in staff.json file in json file format."""

    # Check for existance of staff.json file otherwise create it.
    check_for_staff_json_file()
    # Check for existance of staff.json template otherwise create it.
    check_for_staff_json_template()

    # Putting the person profile into the staff.json.
    with open(staff_json, 'r+') as file:
        # First we loading an existing staff into a Python dict.
        file_data = json.load(file)
        # Joining person profile with file_data inside position dict.
        file_data[position].append(person_profile)
        # Sets file's current position at offset.
        file.seek(0)
        # Dumping the person profile to the file with indent of 4 spaces.
        json.dump(file_data, file, indent = 4)




def staff_json_file_is_empty():
    """Check if staff.json file is empty."""

    """
    @dev We checking this by causing a specific json error that appears if can
         not load the existing .json file because of emptiness.
         
         True if error occur and the file is actual empty.
         False if there is no error occur and the contents of .json file can be loaded.
    """

    try:
        with open(staff_json, "r+") as file:
            json.load(file)
    except json.decoder.JSONDecodeError:
        return True
    else: 
        return False


#
# <--- Test Function --->
#

"""
@dev Actually this is not the case how to test the code.
     For that we need to use pytest library.
     I'll create later the apart directory to test our functions properly.
     We will have to do that as the project growth up and every time input the name, birthday etc. is not an option.
"""

get_new_person_profile()

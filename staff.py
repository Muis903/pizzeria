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


def get_new_staff() -> dict: # dat de functie retourneert dict (voor leesbaarheid bedoeld). Kan ook niet gebruiken. Verwirder deze omschrijving als duidelijk.
    """Get new staff and save it into the json."""

    #Data
    name = input("First and last name: ")
    birthday = input("Birthday dd/mm/yyyy: ")
    login = input("Login: ")
    password = input("Password: ")
    position = input("Position: ")
    
    #Create an object as a profile in the form of Python dictionary.
    profile = create_profile(name, birthday, login, password, position)

    # Saving new staff.
    save_new_staff(profile, position)

    # Returning the profile to work with further if need it.
    return profile


def get_positions() -> list:
    """Return all positions."""

    # Defining the positions inside of the company.
    # @dev Feel free to add more
    positions = [
        "junior", "medio", "senior", "team leader", "project leader", "manager"
    ]
    print("Checking for all positions.")

    return positions


def save_new_staff(profile:dict, position:str): # :dict geeft aan dat de attribuut dict MOET zijn. Er zijn nog :str, :list ezv. Verwijder de omschrijving als duidelijk ;-)
    """Save new staff in json file format."""

    # Create staff.json file is the file does not exist.
    create_staff_json_file()
    # Create staff.json template if the staff.json is empty.
    create_staff_json_template()

    # Putting the profile into the staff.json.
    with open(staff_json, 'r+') as file:
        # First we loading existing staff into a dict.
        file_data = json.load(file)
        # Joining profile with file_data inside position.
        file_data[position].append(profile)
        # Sets file's current position at offset.
        file.seek(0)
        # Dumping the profile to the file with indent of 4 spaces.
        json.dump(file_data, file, indent = 4)
        print("The new profile is successfully added into staff.json :)")


def create_profile(name=None, birthday=None, login=None, password=None, position=None): # None betekent dat de waarde van de parameter is niet vereist. Verwijder de omschrijving als duidelijk :)
    """Create and return a profile template."""
    
    profile = {
        "name": name,
        "birthday": birthday,
        "login": login,
        "password": password,
        "position": position
    }
    
    print("Created a new profile.")

    return profile


def create_staff_json_file():
    """Create staff.json if not already exist."""
    
    # GETting Current Working Directory.
    PATH = os.getcwd()
    
    # If staff.json not in the current working directory, then create one.
    if staff_json not in os.listdir(PATH):
        open(staff_json, 'w')
        print("Created new staff.json file.")
    else:
        print("staff.json file already exists.")


def staff_json_file_is_empty():
    """Check if staff.json file is empty."""

    """
    @dev We checking this by calling a specific json error that appears if can
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


def create_staff_json_template():
    """Create staff.json template."""

    """
    @dev The implemantation of this function needs improvements because
         if you start adding new staff, the index 0 in will always have None as the value.
    """
    
    if staff_json_file_is_empty() == False:
        print("staff.json is not empty.")
    else:
        print("Creating a template in staff.json")
        # Getting all positions in the company.
        positions = get_positions()
        # Defining the profile as Python dictionary.
        profile = dict()
        # Looping through all positions and adding to the template.
        for position in positions:
            # Key/value pair, where position is a key and the rest is the value.
            profile[position] = [
                {   
                    "name": None,
                    "birthday": None,
                    "login": None,
                    "password": None,
                    "position": None
                }
            ]

        # Creating staff.json file if not already exists.
        create_staff_json_file()
        # Saving the template to staff.json.
        with open(staff_json, 'r+') as file:
            json.dump(profile, file, indent=4)


#
# <--- Test Function --->
#

# Remove # in order to test a specific function.
#create_staff_json_file()
get_new_staff()
#save_new_staff(create_profile())

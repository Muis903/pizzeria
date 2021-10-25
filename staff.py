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
    """Get a new staff profile and save it into the staff.json."""

    #Data
    name = input("First and last name: ")
    birthday = input("Birthday dd/mm/yyyy: ")
    login = input("Login: ")
    password = input("Password: ")
    position = input("Position: ")
    
    #Create an object as a staff profile in the form of Python dictionary.
    person_profile = create_person_profile(name, birthday, login, password, position)
    print("Created a new staff profile.")

    # Saving new staff.
    save_new_person_profile(person_profile, position)

    # Returning the person_profile to work with further if need it.
    return person_profile


def get_staff_positions() -> list:
    """Return all staff_positions inside of the company."""

    # Defining the positions inside of the company.
    # @dev Feel free to add more
    positions = [
        "junior", "medio", "senior", "team leader", "project leader", "manager"
    ]
    print("Checking for all positions.")

    return positions


def save_new_person_profile(person_profile:dict, position:str): # :dict geeft aan dat de attribuut dict MOET zijn. Er zijn nog :str, :list ezv. Verwijder de omschrijving als duidelijk ;-)
    """Save new staff profile in staff.json file in json file format."""

    # Create staff.json file is the file does not exist.
    create_staff_json_file()
    # Create staff.json template if the staff.json file is empty.
    create_staff_json_template()

    # Putting the staff profile into the staff.json.
    with open(staff_json, 'r+') as file:
        # First we loading an existing staff into a Python dict.
        file_data = json.load(file)
        # Joining staff profile with file_data inside position dict.
        file_data[position].append(person_profile)
        # Sets file's current position at offset.
        file.seek(0)
        # Dumping the staff profile to the file with indent of 4 spaces.
        json.dump(file_data, file, indent = 4)
        print("The new staff profile is successfully added into staff.json :)")


def create_person_profile(name=None, birthday=None, login=None, password=None, position=None): # None betekent dat de waarde van de parameter is niet vereist. Verwijder de omschrijving als duidelijk :)
    """Create and return a staff profile."""
    
    profile = {
        "name": name,
        "birthday": birthday,
        "login": login,
        "password": password,
        "position": position
    }
    

    return profile


def create_staff_json_file():
    """Create staff.json if not already exists."""
    
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
    """Create staff.json template and upload it to staff.json."""

    """
    @dev The implemantation of this function needs improvements because
         if you start adding new staff, the index 0 in will always have None as the value.
    """
    
    if staff_json_file_is_empty() == False:
        print("staff.json is not empty.")
    else:
        print("Creating a template in staff.json")
        # Getting all positions in the company.
        staff_positions = get_staff_positions()
        # Defining the staff profile as Python dictionary.
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

        # Creating staff.json file if not already exists.
        create_staff_json_file()
        # Saving the template to staff.json.
        with open(staff_json, 'r+') as file:
            json.dump(person_profile, file, indent=4)


#
# <--- Test Function --->
#

# Remove # in order to test a specific function.
#create_staff_json_file()
get_new_person_profile()
#save_new_person_profile(create_person_profile())

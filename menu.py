import json
import os
from self_made_python_libraries.file import File


#
# DEFINING global variables
#


menu_card_json = "menu_card.json"


#
# DEFINING functions
#


def get_item_types():
    """Return all item types for menu card."""

    item_types = [
        "pizzas", "crunchy_chicken", "side_dish", "desserts_and_drinks"
    ]

    return item_types


def get_item_type_pizzas():
    """Return item type pizzas."""

    # Check for existance of menu_card.json file otherwise create it.
    check_for_menu_card_json_file()
    # Check for existance of menu_card.json template otherwise create it.
    check_for_menu_card_json_template()

    with open(menu_card_json, "r+") as file:
         # First we loading an existing menu card into a Python dictionary.
         file_data = json.load(file)
         pizzas = file_data["pizzas"]

    return pizzas


def get_item_type_crunchy_chicken():
    """Return item type crunchy chicken."""

    # Check for existance of menu_card.json file otherwise create it.
    check_for_menu_card_json_file()
    # Check for existance of menu_card.json template otherwise create it.
    check_for_menu_card_json_template()

    with open(menu_card_json, "r+") as file:
        # First we loading an existing menu card into a Python dictionary.
        file_data = json.load(file)
        crunchy_chicken = file_data["crunchy_chicken"]

    return crunchy_chicken


def create_item(item_type=None, item_sectie=None, name=None, price=None):
    """Create and return new item."""

    item = {
        item_type: [
            {
                item_sectie: [
                    {
                        "name": name,
                        "price": price
                    }
                ]
            }
        ]
    }

    return item


def menu_card_json_file_is_empty():
    """Check if menu_card.json file is empty."""

    # Check for existance of menu_card.json file otherwise create one.
    check_for_menu_card_json_file()

    try:
        with open(menu_card_json, "r+") as file:
            json.load(file)
    except json.decoder.JSONDecodeError:
        return True # is empty
    else:
        return False # is not empty


def check_for_menu_card_json_file():
    """Check for menu_card.json file, otherwise create one."""

    # GETing Current Working Directory.
    PATH = os.getcwd()

    # If menu_card.json not in the current working directory, then create one.
    if menu_card_json not in os.listdir(PATH):
        open(menu_card_json, "w")
        # Created new menu_card.json file.
    else:
        # Checked: found menu_card.json file.
        pass


def check_for_menu_card_json_template():
    """Check for template in manu_card.json, otherwise upload it to menu_card.json"""
    if menu_card_json_file_is_empty() == False:
        pass # menu_card.json is not empty
    else: # Creating a template in menu_card.json
        # Getting all item types for menu card.
        item_types = get_item_types()
        # Defining the menu card as Python dictionary.
        menu_card = dict()
        # Looping through all item types and adding to the template.
        for item_type in item_types:
            # Key/Value pair, where item type is a key and the rest is the value.
            menu_card[item_type] = [
                {
                    "test": [
                        {
                            "name": None,
                            "price": None
                        }
                    ]
                }
            ]

        # Saving the template to menu_card.json.
        with open(menu_card_json, 'r+') as file:
            json.dump(menu_card, file, indent=4)


def append_new_item_into_menu_card(item:dict, item_type:str):
    """Append new item into menu_card.json file."""

    # Check for existance of menu_card.json file otherwise create it.
    check_for_menu_card_json_file()
    # Check for existance of menu_card.json template otherwise create it.
    check_for_menu_card_json_template()

    # Putting item into menu_card.json
    with open(menu_card_json, "r+") as file:
        # First we loading an existing menu card into a Python dictionary.
        file_data = json.load(file)
        # Joining item with file_data inside item type dict, inside of list with index 0.
        file_data[item_type].append(item[item_type][0])
        # Sets file's current position at offset.
        # Read more about Python's seek() function:
        # https://www.geeksforgeeks.org/python-seek-function/
        file.seek(0)
        # Dumping the menu card to the file with indent of 4 spaces.
        json.dump(file_data, file, indent=4)


def edit_item_in_menu_card():
    pass


def delete_item_from_menu_card():
    pass


def get_menu_card():
    """Return whole menu card."""

    with open(menu_card_json, "r+") as file:
        # First we loading an existing menu card into a Python dictionary.
        menu_card = json.load(file)

    return menu_card


def choose_item():
    pass

#
# TEST
#

f = File()
print(f)

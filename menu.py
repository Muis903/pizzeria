import json
import os

menu_json = "menu.json"

def get_items_type():

    pizzas = {
        #Pizza types
        "pizza's & populair": [
            #Pizza's
            {"name": "pizza 4 cheese",
            "price": "4.95"},

            {"name": "pizza peperomi",
            "price": "7.25"}
        ]
    }
    drinks = {
        #Drinks types
        "hot drinks": [
        {"name": "tea",
        "price": "1.5"},

        {"name": "cofee"
        "cold_drinks": ["cola", "water"]
    }
    snacks = []
    desserts = []
    sla = []
    sauces = []

def create_menu_card_item():
    item = None
    pass


def menu_json_file_is_empty():
    """Check if menu.json file is empty."""
    try:
        with open("menu.json", "r+") as file:
            json.load(file)
    except json.decoder.JSONDecodeError:
        return True
    else:
        return False


def check_for_menu_json_file():
    """Check for menu.json file, otherwise create one."""
    PATH = os.getcwd()
    if menu_json not in os.listdir(PATH):
        open(menu_json, "w")
        print("Created new 'menu.json' file.")
    else:
        print("Checked: found menu.json file.")


def append_item_to_menu_card():
    pass


def edit_item_in_menu_card():
    pass


def delete_item_from_menu_card():
    pass


def display_menu_card_items():
    pass


def choose_item():
    pass

#
# TEST
#

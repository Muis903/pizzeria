from menu_config import *
import json
import os
from lib.file import File


#
# DEFINING global variables
#


class Menu():
    """Menu."""
    def __init__(
        self,
    ):
        self.MENU_CARD_DATA_FILE_NAME = MENU_CARD_DATA_FILE_NAME
        self.PATH_TO_MENU_CARD_DATA = PATH_TO_MENU_CARD_DATA
        self.MENU_CARD_DATA_IS_EXIST = MENU_CARD_DATA_IS_EXIST
        self.MENU_CARD_DATA_IS_EMPTY = MENU_CARD_DATA_IS_EMPTY
        self.MENU_CARD_DATA_TEMPLATE = MENU_CARD_DATA_TEMPLATE
        self.MENU_CARD_DATA = MENU_CARD_DATA

        self.ITEM_TYPES_CRUNCHY_CHICKEN = ITEM_TYPES_CRUNCHY_CHICKEN
        self.ITEM_TYPES_PIZZAS = ITEM_TYPES_PIZZAS
        self.ITEM_TYPES_SIDE_DICH = ITEM_TYPES_SIDE_DICH
        self.ITEM_TYPES_DESSERTS_AND_DRINKS = ITEM_TYPES_DESSERTS_AND_DRINKS
        self.ITEM_TYPES = ITEM_TYPES
        self.ITEM = ITEM

class Item(Menu):
    """"""
    def __init__(
        self,
    ):
        super().__init__():
            pass

    def create_item():




#
# DEFINING functions
#




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


#
#
#def edit_item_in_menu_card():
#    pass
#
#
#def delete_item_from_menu_card():
#    pass




#def choose_item():
#    pass

#
# TEST
#


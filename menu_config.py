from self_made_python_libraries.file import File


file = File()

# MANU CARD
MENU_CARD_DATA_FILE_NAME = "menu_card.yaml"
PATH_TO_MENU_CARD_DATA = f"./{MENU_CARD_FILE_NAME}"
MENU_CARD_DATA_IS_EXIST = file.is_exist(PATH_TO_MENU_CARD_DATA)
MENU_CARD_DATA_IS_EMPTY = file.is_empty(PATH_TO_MENU_CARD_DATA)
MENU_CARD_DATA_TEMPLATE = None
MENU_CARD_DATA = file.load_from_yaml(PATH_TO_MENU_CARD_DATA)
# ITEM AND ITEM TYPES
ITEM_TYPES_CRUNCHY_CHICKEN = MENU_CARD_DATA["crunchy_chicken"]
ITEM_TYPES_PIZZAS = MENU_CARD_DATA["pizzas"]
ITEM_TYPES_SIDE_DISH = MENU_CARD_DATA["side_dich"]
ITEM_TYPES_DESSERTS_AND_DRINKS = MENU_CARD_DATA["deserts_and drinks"]
ITEM_TYPES = ["pizzas", "crunchy_chicken", "side_dish", "desserts_and_drinks"]
ITEM = None

#print(MENU_CARD_DATA)
#print(ITEM_TYPES_CRUNCHY_CHICKEN)

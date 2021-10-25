#
# IMPORTING necessary libraries and scripts.
#


from random import choice


#
# DEFINING functions.
#


def get_order():
    """GETTING THE ORDER."""
    order = input("-> Order: ")
    order_id = get_order_id()
    # SAVE the order in JSON.
    save_order(order_id, order)

    return (order + " #" + order_id)


def get_order_id():
    """GETTING THE ORDER ID."""
    numbers = []
    if not numbers:
        for number in range(1, 1000):
            numbers.append(number)
    order_id = numbers.pop(choice(numbers))

    return str(order_id)


def save_order(order_id, order):
    """SAVING AN ORDER."""
    # Saving a new order in a dictionary.
    order_id_to_order = {order_id: order}
    print(order_id_to_order)
    print("The new order is successfully saved!")

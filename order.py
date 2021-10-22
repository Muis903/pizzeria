class Order():


def get_order():
    """GETTING THE ORDER."""
    order_id = get_order_id()
    order = input("-> Order: ")
    # SAVE the order in JSON.
    save_order(order_id, order)

    return order + " #" order_id


def get_order_id():
    """GETTING THE ORDER ID."""
    numbers = []
    if not numbers:
        for number in range(1, 1000):
            numbers.append(number)
    order_id = numbers.pop(choice(numbers))

    return order_id


def show_order():
    """Show the order to the cook."""
    print(order)

	
def give_order(order, pay):
    ready_order = True
    if ready_order and len(order) > 20:
        print(f"Your {order[:20]}... is ready to take away!")
        print(str(pay) + " to pay.")
    if ready_order and len(order) < 20:
        print(f"Your {order} is ready to take away!")
        print(str(pay) + " to pay.")

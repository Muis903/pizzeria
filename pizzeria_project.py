from random import choice
from menu_pizzeria import menu
import os
os.system("clear")

def make_order_number():
    """Make a list with random numbers."""
    numbers = []
    if not numbers:
        for number in range(1, 1000):
            numbers.append(number)

    order_number = numbers.pop(choice(numbers))

    return order_number

def accept_order(order_number, order):
    """Accept and  save the new order"""
    order_number = make_order_number()
    accepted_order = str(order_number) + " - " + order.title()
    with open("show_order_2screen.py", "w") as file:
        file.write(order)

    return accepted_order

def show_order(accepted_order):
    """Show the order to the cook."""
    print(accepted_order)

def calculate_price(accepted_order):
    """Calculate the total price of placed order"""
    to_pay = []
    for product in menu:
        if accepted_order == product['product']:
            price = (product['price'])
            to_pay.append(int(price))
    pay = sum(to_pay) + int(price)
    return pay

def give_order(accepted_order, pay):
    ready_order = True
    if ready_order and len(accepted_order) > 20:
        print(f"Your {accepted_order[:20]}... is ready to take away!")
        print(str(pay) + " to pay.")
    if ready_order and len(accepted_order) < 20:
        print(f"Your {accepted_order} is ready to take away!")
        print(str(pay) + " to pay.")

if __name__ == "__main__":
    for product in menu:
        print(product['product']  + " €" + product['price'])
    print("\n")
    order = input("Your order:\n")
    order_number = make_order_number()
    accepted_order = accept_order(order_number, order)
    pay = calculate_price(accepted_order)
    show_order(accepted_order)
    give_order(accepted_order, pay)

def calculate_price(accepted_order):
    """Calculate the total price of placed order"""
    to_pay = []
    for product in menu:
        if accepted_order == product['product']:
            price = (product['price'])
            to_pay.append(int(price))
    pay = sum(to_pay) + int(price)
    return pay

def check_inventory(products):
    for product, stock in products.items():
        if stock < 15:
            print(f"{product}: Reorder Alert (Stock = {stock})")
        else:
            print(f"{product}: Stock OK (Stock = {stock})")

inventory = {
    "Rice": 10,
    "Wheat": 25,
    "Sugar": 8,
    "Oil": 20
}

check_inventory(inventory)

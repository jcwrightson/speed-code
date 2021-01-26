import os
from src.persistence.core import save

sub_menu = """
[0] - Back
[1] - View
[2] - Create
[3] - Update
[4] - Delete
"""


def view_products(products):
    os.system("clear")
    idx = 0
    for product in products:
        print(f"{idx} \t {product['name']} \t £{product['price']}")
        idx += 1


def create_product(products):
    name = input("Name: ")
    price = float(input("Price: "))

    product = {
        "name": name,
        "price": price
    }

    products.append(product)
    save(products)
    return products


def update_product(products):
    view_products(products)
    idx = int(input("Select: "))

    for key in products[idx].keys():
        update = input(f"{key}: ")
        if update != "":
            if key == "price":
                products[idx][key] = float(update)
            else:
                products[idx][key] = update

    save(products)
    return products


def delete_product(products):
    view_products(products)
    idx = int(input("Select: "))
    products.pop(idx)
    save(products)
    return products


def product_menu(products=[]):
    os.system("clear")
    while True:
        print(sub_menu)
        sub_option = int(input("Please choose an option: "))

        if sub_option == 0:
            break

        if sub_option == 1:
            view_products(products)

        if sub_option == 2:
            create_product(products)

        if sub_option == 3:
            update_product(products)

        if sub_option == 4:
            delete_product(products)

    return products

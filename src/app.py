import os

from src.product.core import product_menu
from src.persistence.core import read_csv_data, save

# products = []
orders = []
couriers = []


main_menu = """
[0] - Exit
[1] - Products
[2] - Couriers
[3] - Orders
"""

sub_menu = """
[0] - Back
[1] - View
[2] - Create
[3] - Update
[4] - Delete
"""


def courier_menu():
    pass


def order_menu():
    pass


def menu(products):

    while True:
        os.system("clear")
        print(main_menu)
        option = int(input("Please choose an option: "))

        if option == 0:
            break

        if option == 1:
            products = product_menu(products)

        # if option == 2:
        #     courier_menu()

        # if option == 3:
        #     order_menu()


def init():
    global products
    products = read_csv_data("./data/products.csv")


init()
menu(products)
save(products)

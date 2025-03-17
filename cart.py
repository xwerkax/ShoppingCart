from products import *

class Cart:
    def __init__(self):
        self.__products_list = []
        self.__cart_value = 0

    def add_to_cart(self, product):
        if isinstance(product, Product):
            if product not in self.__products_list:
                self.__products_list.append(product)
                self.calculate_cart()

    def calculate_cart(self):
        self.__cart_value = 0
        for el in self.__products_list:
            self.__cart_value += el.price



    def __str__(self):
        strData = "\nCart info, products list:"
        for el in self.__products_list:
            strData += "\n - " + str(el.name) + " " + str(el.price)
        strData += "\n cart value: " + str(self.__cart_value)
        return strData
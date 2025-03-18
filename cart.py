
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} ({self.price} PLN)"

    def __eq__(self, other):
        return isinstance(other, Product) and self.name == other.name and self.price == other.price

    def __hash__(self):
        return hash((self.name, self.price))


class Cart:
    def __init__(self):
        self.__products_list = {}  # Przechowuje produkty i ich ilość
        self.__cart_value = 0

    def add_to_cart(self, product):
        if isinstance(product, Product):
            if product in self.__products_list:
                self.__products_list[product] += 1
            else:
                self.__products_list[product] = 1
            self.calculate_cart()

    def remove_from_cart(self, product_name):
        found_product = next((p for p in self.__products_list if p.name == product_name), None)

        if found_product:
            if self.__products_list[found_product] > 1:
                self.__products_list[found_product] -= 1
            else:
                del self.__products_list[found_product]
            self.calculate_cart()
            print("✅ Produkt usunięty!")
        else:
            print("❌ Produkt nie znajduje się w koszyku.")

    def calculate_cart(self):
        self.__cart_value = sum(product.price * qty for product, qty in self.__products_list.items())

    def __str__(self):
        if not self.__products_list:
            return "\n🛒 Koszyk jest pusty!"
        strData = "\n🛍️  Zawartość koszyka:"
        for product, qty in self.__products_list.items():
            strData += f"\n - {product.name} ({product.price} PLN) x{qty}"
        strData += f"\n💰 Wartość koszyka: {self.__cart_value} PLN"
        return strData

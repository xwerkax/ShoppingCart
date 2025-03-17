from cart import *

phone1 = Phone("iphone xr", 2000, "white")
phone2 = Phone("samsung s4", 1000, "black")
tv1 = TV("samsung", 2200, 80)
tv2 = TV("LG", 3000, 70)
tv3 = TV("Philips", 2300, 65)

cart = Cart()
cart.add_to_cart(phone1)
cart.add_to_cart(phone2)
cart.add_to_cart(tv3)
cart.add_to_cart(tv2)
cart.add_to_cart(tv1)

print(cart)
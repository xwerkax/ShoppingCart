from cart import *

cart = Cart()

def display_menu():
    print("\n📌 MENU:")
    print("1️⃣ - Dodaj produkt do koszyka")
    print("2️⃣ - Usuń produkt z koszyka")
    print("3️⃣ - Wyświetl koszyk")
    print("4️⃣ - Wyjście")

while True:
    display_menu()
    choice = input("Wybierz opcję: ")

    if choice == "1":
        name = input("📦 Podaj nazwę produktu: ")
        try:
            price = float(input("💰 Podaj cenę produktu: "))
            product = Product(name, price)
            cart.add_to_cart(product)
            print("✅ Produkt dodany do koszyka!")
        except ValueError:
            print("❌ Błąd: cena musi być liczbą!")

    elif choice == "2":
        print(cart)
        prod_name = input("✂ Podaj nazwę produktu do usunięcia: ")
        cart.remove_from_cart(prod_name)

    elif choice == "3":
        print(cart)

    elif choice == "4":
        print("👋 Zamknięcie programu.")
        break

    else:
        print("❌ Nieprawidłowa opcja. Spróbuj ponownie.")

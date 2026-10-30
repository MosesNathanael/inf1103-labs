import json

class Product:
    def __init__(self, product_id, name, price, stock):
        self.__product_id: str = product_id
        self.__name: str = name
        self.__price: float = price
        self.__stock: int = stock

    def update_stock(self, qty: int):
        self.__stock: int = qty

    def display_information(self):
        print(f"ID:{self.__product_id} | Name: {self.__name} | Price: ${self.__price} | Stock: {self.__stock}")
        print("-------------------------------------") 

class Inventory:
    def __init__(self, inventory):
        self.__list = inventory

    def add_product(self, product):
        self.__list.append(product)

    def search_product(self, product_id):
        for p in self.__list:
            if p._Product__product_id == product_id:
                p.display_information()  
                return p
        return False

    def display_all(self):
        if len(self.__list) == 0:
            print("Inventory is empty")
        for p in self.__list:
            p.display_information()



def validate_int(x):
    try:
        x = int(x)
    except ValueError:
        return False
    
    if x <= 0:
        return False

    return True

def validate_int_float(x):
    try:
        x = float(x)
    except ValueError:
        return False
        
    if x <= 0:
        return False
    
    return True


def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            inventory = json.load(file)
            inventory_list = [Product(**product) for product in inventory]
            return inventory_list
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_inventory(inventory):
    inventory_dict = []
    for product in inventory._Inventory__list:
        inventory_dict.append({
            "product_id": product._Product__product_id,
            "name": product._Product__name,
            "price": product._Product__price,
            "stock": product._Product__stock
        })
    with open("inventory.json", "w") as file:
        json.dump(inventory_dict, file, indent=4)


def display_menu():
    print("------------- MENU -------------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("---------------------------------")

 

def main():
    print("====================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("====================================")

    inven = load_inventory()
    inventory = Inventory(inven)

    while True:
        print("\n")
        display_menu()
        try:
            choice = int(input("Enter option [1-6]: "))
        except Exception:
            print("Please input number 1 - 6 only")
            continue
        
        if choice == 1:
            inventory.display_all()

        elif choice == 2:
            print("Add New Product")
            id = input("Product ID: ")
            name = input("Product Name: ")
            price = input("Price: ")
            if validate_int_float(price) == False:
                print("You should only input positive number")
                continue 
            stock = input("Stock Quantity: ")
            if validate_int(stock) == False:
                print("You should only input positive number")
                continue
            
            product = Product(id, name, float(price), stock)
            inventory.add_product(product)
            print("Product added")

        elif choice == 3:
            id = input("Product ID: ")
            product = inventory.search_product(id)
            if not product:
                print("Product Not Found")
                continue

            new_qty = input("New Qty: ")
            if not validate_int(new_qty):
                print("Please input a positive integer number")
                continue

            product.update_stock(new_qty)
            print("Product updated")
            

        elif choice == 4:
            id = input("Product ID: ")
            product = inventory.search_product(id)
            if not product:
                print("Product Not Found")
                continue

        elif choice == 5:
            save_inventory(inventory)
            print("Saving inventory...")
            print("Inventory saved successfully to inventory.json")
        elif choice == 6:
            save_inventory(inventory)
            print("Saving inventory before exit...")
            print("Inventory saved successfully.\n")
            print("Thankyou for using Inventory Management System")
            print("Program terminated.")
            break
        else:
            print("Please input number 1 - 6 only")

        



main()



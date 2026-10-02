import json

def display_menu():
    print("====================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("====================================")
    print("------------- MENU -------------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("---------------------------------")



def add_product():
    print("Add New Product")
    id = input("Product ID: ")
    name = input("Product Name: ")
    price = input("Price: ")
    stock = input("Stock Quantity: ")
    return {
        "ID": id,
        "Name": name,
        "Price": price,
        "Stock": stock
    }


def search_product(inventory, id):
    for item in inventory:
        if item["ID"] == id:
            print("Product Found")
            print("-------------------------------------")
            print(f"ID: {item["ID"]}")
            print(f"Name: {item["Name"]}")
            print(f"Price: ${item["Price"]}")
            print(f"Stock: {item["Stock"]}")
            print("-------------------------------------")
            return item
        
    return False


def update_stock(inventory, id):
    item = search_product(inventory, id)
    if item == False:
        print("Product not found")
    else:
        new_stock = input("New stock Quantity: ")
        try:
            new_stock = int(new_stock)
        except ValueError:
            print("You should only input positive integer")
            return

        if new_stock <= 0:
            print("You should only input positive integer")
            return

        return new_stock

        


def load_inventory():
    with open("inventory.json", "r") as file:
        product = json.load(file)

    return product










  

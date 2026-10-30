import json


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


def display_menu():
    print("------------- MENU -------------")
    print("1. Display All Products")
    print("2. Add Product")
    print("3. Update Stock")
    print("4. Search Product")
    print("5. Save Inventory")
    print("6. Exit")
    print("---------------------------------")

def load_inventory():
    try:
        with open("inventory.json", "r") as file:
            product = json.load(file)
            return product
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def display_inventory(inventory):
    print("\nCurrent Inventory")
    if len(inventory) == 0:
        print("Inventory is empty!")
    else:
        print("-------------------------------------")

        for item in inventory:
            print(f"ID: {item["ID"]} | Name: {item["Name"]} | Price: ${item["Price"]} | Stock: {item["Stock"]}")

        print("-------------------------------------\n")


def add_product():
    print("Add New Product")
    id = input("Product ID: ")
    name = input("Product Name: ")
    price = input("Price: ")
    if validate_int_float(price) == False:
        print("You should only input positive number")
        return 
    stock = input("Stock Quantity: ")
    if validate_int(stock) == False:
        print("You should only input positive number")
        return
    print("Product added successfully!\n")
    return {
        "ID": id,
        "Name": name,
        "Price": float(price),
        "Stock": int(stock)
    }






def search_product(inventory):
    if len(inventory) == 0:
        print("Inventory is Empty!")
        return False
    id = input("Enter Product ID: ")
    for item in inventory:
        if item["ID"] == id:
            print("Product Found")
            print("-------------------------------------")
            print(f"ID: {item["ID"]}")
            print(f"Name: {item["Name"]}")
            print(f"Price: ${item["Price"]}")
            print(f"Stock: {item["Stock"]}")
            
            print("-------------------------------------")
            return id

    print("Product Not Found")
    return False



def update_stock(inventory):
    check = search_product(inventory)
    if check == False:
        return False

    new_stock = input("New stock Quantity: ")
    if validate_int(new_stock) == False:
        print("You should only enter positive integers.")
        return False
    
    for item in inventory:
        if item["ID"]  == check:
            item["Stock"] = int(new_stock)
            print("Stock Updated Successfully!\n")

    return inventory

        




def save_inventory(inventory):
    with open("inventory.json", "w") as file:
        json.dump(inventory, file, indent=4)



def main():
    print("====================================")
    print("INVENTORY MANAGEMENT SYSTEM")
    print("====================================")

    inventory = load_inventory()


    while True:
        display_menu()
        try:
            choice = int(input("Enter option [1-6]: "))
        except Exception:
            print("Please input number 1 - 6 only")
            continue
        
        if choice == 1:
            display_inventory(inventory)

        elif choice == 2:
            product = add_product()
            if product != None:
                inventory.append(product)

        elif choice == 3:
            new_inventory = update_stock(inventory)
            if new_inventory != False:
                inventory = new_inventory

        elif choice == 4:
            search_product(inventory)

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




  

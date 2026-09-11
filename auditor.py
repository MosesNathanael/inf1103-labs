total_inventory = 0
failed = 0
while True:
    user = input("Enter Stock Quantity: ")
    if user == "quit":
        break  

    if user.isdigit() == False:
        print("Error, you should only input integers")
        continue
    

    user = int(user)

    
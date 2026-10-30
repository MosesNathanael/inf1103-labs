total_inventory = 0
failed = 0
while True:
    user = input("Enter Stock Quantity: ")
    if user == "quit":
        print(f"Total Units Processed: {total_inventory}")
        print(f"Number of Failed/Rejected: {failed}")
        break  

    if user.isdigit() == False:
        print("Error, you should only input integers")
        failed += 1
        continue

    if int(user) < 0:
        print("Rejected, please input positive number")
        failed += 1
        continue

    total_inventory += int(user)

    if total_inventory > 500:
        print("Overstock Alert!")
        break

    
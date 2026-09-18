total_inventory = 0

def get_valid_input():
    user = input("Enter Stock Quantity: ")
    if user == "quit":
        return "quit"
    if user.isdigit() == False:
        print("Error, you should only input integers")
        return False
            
    if int(user) <= 0:
        print("Rejected, please input positive number")
        return False
    else:
        return user


def process_delivery(current_total, new_value):
    new_total = int(current_total) + int(new_value)
    return new_total


def calculate_tax(amount):
    return amount*0.1


def calculate_tax(amount):
    return amount*0.1

def generate_report(total_units, failed_attemps):
    print(f"Total Deliveries Processed: {total_units}, Failed_attemps: {failed_attemps}")


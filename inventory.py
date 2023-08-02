
#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        # Initialize the attributes of the Shoe class
        self.country = country 
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    def get_cost(self):
        # Return the cost of the shoe
        return self.cost
    def get_quantity(self):
        # Return the quantity of the shoe
        return self.quantity
    def __str__(self):
        # Return a string representation of the shoe object
        return f"{self.product} ({self.code}) from {self.country}, {self.quantity} pairs available at ${self.cost} each."
#=============Shoe list===========
'''
The list will be used to store a list of objects of shoes.
'''
shoe_list = []
#==========Functions outside the class==============
def read_shoes_data():
    try:
        with open('inventory.txt', 'r') as f:
            next(f) # skip the first line
            for line in f:
                data = line.strip().split(',')
                if len(data) == 5:
                    country, code, product, cost, quantity = data
                    shoe_list.append(Shoe(country, code, product, float(cost), int(quantity)))
            print()
            print("Success! The file has been read.")
    except FileNotFoundError:
        print()
        print('File not found')
    except Exception as e:
        print()
        print(f'Error: {e}')

# This function captures information about a new pair of shoes and adds it to a list
def capture_shoes():
    country = input("Enter country: ")
    code = input("Enter code: ")
    product = input("Enter product: ")
    cost = float(input("Enter cost: "))
    quantity = int(input("Enter quantity: "))
    shoe_list.append(Shoe(country, code, product, cost, quantity))
    with open('inventory.txt', 'a') as f:
        f.write(f"{country},{code},{product},{cost},{quantity}\n")
    print()
    print(f"Added {product} ({code}) from {country} to inventory.")

# This function displays information about all shoes in the inventory
def view_all():
    # If the inventory is empty, print a message and exit the function
    print(len(shoe_list))
    if len(shoe_list) == 0:
        print("No shoes in inventory.")
        return
    # If the inventory is not empty, loop through each shoe in the list and print its information
    for shoe in shoe_list:
        print(shoe.__str__())

# This function restocks the shoe with the lowest quantity in the inventory
def re_stock():
    # If the inventory is empty, print a message and exit the function
    if len(shoe_list) == 0:
        print("No shoes in inventory.")
        return
    # Find the shoe with the lowest quantity by using the min() function with a lambda function as the key
    lowest_qty_shoe = min(shoe_list, key=lambda shoe: shoe.quantity)
    # Print a message indicating which shoe has the lowest quantity
    print(f"The shoe with code '{lowest_qty_shoe.code}' has the lowest quantity of {lowest_qty_shoe.quantity}.")
    # Ask the user to enter the quantity to restock and update the shoe's quantity
    restock_qty = int(input("Enter quantity to restock: "))
    lowest_qty_shoe.quantity += restock_qty
    # Print a message indicating that the restock was successful
    print(f"Restocked {restock_qty} {lowest_qty_shoe.product} ({lowest_qty_shoe.code}) from {lowest_qty_shoe.country}. New quantity: {lowest_qty_shoe.quantity}.")

def search_shoe():
    # If the inventory is empty, print a message and exit the function
    if len(shoe_list) == 0:
        print("No shoes in inventory.")
        return
    # Ask the user to enter the code of the shoe to search for
    code = input("Enter shoe code to search: ")
    # Loop through each shoe in the inventory and print its information if the code matches
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe.__str__())
            return
    # If no shoe with the given code is found, print a message indicating that
    print(f"No shoe with code '{code}' found in inventory.")

# This function calculates the total value of each type of shoe in the inventory
# by multiplying its cost by its quantity

def value_per_item():
    # If the inventory is empty, print a message and exit the function
    if len(shoe_list) == 0:
        print("No shoes in inventory.")
        return
    # Loop through each shoe in the inventory and calculate its total value
    for shoe in shoe_list:
        value = shoe.cost * shoe.quantity
        # Print the shoe's name and its total value
        print(f"{shoe.product}: {value}")
# This function finds the shoes with the highest quantity in the inventory
def highest_qty():
    # If the inventory is empty, print a message and exit the function
    if len(shoe_list) == 0:
        print("No shoes in inventory.")
        return
    # Find the highest quantity among all shoes in the inventory
    max_qty = max(shoe.quantity for shoe in shoe_list)
    # Loop through each shoe in the inventory and print its name and quantity if it has the highest quantity
    for shoe in shoe_list:
        if shoe.quantity == max_qty:
            print(f"{shoe.product} is for sale with the highest quantity: {max_qty}")
#==========Main Menu=============
print("Welcome to the Shoe Inventory Management System!")
while True:
    print("\nPlease select an option:")
    print("1. Read shoes data from file")
    print("2. Capture shoes data manually")
    print("3. View all shoes in inventory")
    print("4. Re-stock shoes with lowest quantity")
    print("5. Search for a shoe by code")
    print("6. Calculate the total value of each shoe")
    print("7. Find the product with the highest quantity")
    print("8. Quit the program")
    choice = input("Enter your choice (1-8): ")
    if choice == "1":
        read_shoes_data()
    elif choice == "2":
        capture_shoes()
    elif choice == "3":
        view_all()
    elif choice == "4":
        re_stock()
    elif choice == "5":
        search_shoe()
    elif choice == "6":
        value_per_item()
    elif choice == "7":
        highest_qty()
    elif choice == "8":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

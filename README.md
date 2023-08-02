# Inventory Management System (inventory.py)

The Inventory Management System (inventory.py) is a Python script that helps manage a shoe inventory. The script uses object-oriented programming (OOP) to create a Shoe class and various functions for handling the shoe data.

## Shoe Class

The script defines a `Shoe` class, representing a shoe item in the inventory. The class has the following attributes:

- `country`: The country of origin for the shoe.
- `code`: The code or unique identifier for the shoe.
- `product`: The product name or description of the shoe.
- `cost`: The cost of the shoe.
- `quantity`: The quantity of the shoe available in the inventory.

The `Shoe` class also has the following methods:

- `get_cost()`: Returns the cost of the shoe.
- `get_quantity()`: Returns the quantity of the shoe.

The `__str__()` method is overridden to provide a string representation of a `Shoe` object, displaying its product name, code, country of origin, available quantity, and cost per shoe.

## Usage of Object-Oriented Programming (OOP)

The script demonstrates the usage of OOP principles by creating and utilizing the `Shoe` class. OOP provides a structured and modular approach to managing the shoe inventory. By encapsulating the shoe data and related functionalities within a class, the script promotes code reusability and maintainability.

The `Shoe` class allows the script to create shoe objects with specific attributes and methods, making it easier to work with shoe data and perform operations related to the inventory. It also provides a cleaner way to handle shoe-related information and perform actions on individual shoes, such as updating quantities, restocking, and searching for shoes.

## Functions

The script includes several functions outside the `Shoe` class to interact with the shoe inventory:

- `read_shoes_data()`: Reads shoe data from the "inventory.txt" file and populates the `shoe_list` with `Shoe` objects.
- `capture_shoes()`: Captures information about a new pair of shoes and adds it to the inventory list and the "inventory.txt" file.
- `view_all()`: Displays information about all shoes in the inventory.
- `re_stock()`: Restocks the shoe with the lowest quantity in the inventory.
- `search_shoe()`: Searches for a shoe in the inventory by its code and displays its information.
- `value_per_item()`: Calculates the total value of each type of shoe in the inventory by multiplying its cost by its quantity.
- `highest_qty()`: Finds the shoes with the highest quantity in the inventory.
- `Main Menu`: The main menu presents a list of options for users to interact with the shoe inventory. Users can choose options to read shoe data, capture new shoes, view shoe information, restock shoes, search for a specific shoe, calculate total values, find the shoe with the highest quantity, and quit the program.

## Data Storage

The script stores shoe data in the "inventory.txt" file. Each line in the file represents a shoe and contains comma-separated values for country, code, product, cost, and quantity. The `shoe_list` maintains a list of `Shoe` objects that represent individual shoes in the inventory.

## Note

- When capturing new shoes, the user is prompted to input relevant details such as country, code, product, cost, and quantity, which are then added to the inventory list and the "inventory.txt" file.
- The script provides various functionalities to view shoe information, restock shoes, calculate total values, and search for shoes in the inventory.

## Docker

The script includes a Dockerfile for containerizing the Inventory Management System. With Docker and Docker Compose installed on your system, you can build and run the Docker container to execute the inventory.py script within the container environment.

# Daily Challenge: Coffee Shop Menu Manager
# You were hired to help a small coffee shop manage their product menu using Python.

# Write a program that:

# 1. Stores the coffee shop menu in memory
# 2. Lets the user:
# Create a new item
# Read (view) all items
# Update an item’s price
# Delete an item
# Exit
# Your program must be organized with functions.
# Do not write all the logic in one giant while loop.
# You should split behavior into reusable functions.

# 1. Data structure
# We will represent the menu using a dictionary called menu.
# The key is the drink name (string)
# The value is the price (float)
# Example starting data (you MUST start with this so tests are consistent):

menu = {
    "espresso": 7.0,
    "latte": 12.0,
    "cappuccino": 10.0
}

# 2. Required functions
# You must implement the following functions.

# a) show_menu(menu_dict)
# Input: the dictionary
# Output: prints all items in the format drink - price₪
# If the menu is empty, print: "The menu is empty."
# Example:
# Current menu:
# espresso - 7.0₪
# latte - 12.0₪
# cappuccino - 10.0₪
# This function only prints. It does not return anything.

def show_menu(menu_dict):
    for (k,v) in menu_dict.items():
        print(f"{k} - {v}₪")

# show_menu(menu)

# b) add_item(menu_dict)
# Ask the user for:
# drink name
# price
# Add it to the dictionary.
# If the drink already exists, print "Item already exists!" and do not change the price.
# Example interaction:
# Enter new drink name: mocha
# Enter price: 14
# "mocha" added!
# This function mutates the dictionary. It does not return anything.

def add_item(menu_dict):
    drink_name = input("Enter new drink name: ")
    drink_price = input("Enter price: ")
    if drink_name in menu_dict.keys():
        print("Item already exists!")
    else:
        menu_dict[drink_name] = drink_price
        print(f"\"{drink_name}\" added!")

# add_item(menu)
# print(menu)

# c) update_price(menu_dict)
# Ask the user which drink they want to update.
# If it exists:
# ask for the new price
# update it
# print: "Price updated!"
# If it doesn’t exist:
# print: "Item not found."

def update_price(menu_dict):
    drink_name = input("Enter which drink to update: ")
    drink_new_price = input("Enter its new price: ")
    if drink_name in menu_dict.keys():
        menu_dict[drink_name] = drink_new_price
        print("Price updated!")
    else:
        print("Item not found.")

# update_price(menu)
# print(menu)

# d) delete_item(menu_dict)
# Ask the user which drink to remove.
# If it exists:
# delete it from the dict
# print: "Item deleted."
# Otherwise:
# print: "Item not found."

def delete_item(menu_dict):
    drink_name = input("Enter which drink to remove: ")
    if drink_name in menu_dict.keys():
        del menu_dict[drink_name]
        print("Item deleted.")
    else:
        print("Item not found.")

# delete_item(menu)
# print(menu)

# e) show_options()
# Prints the main menu of actions for the user:
# What would you like to do?
# 1. Show menu
# 2. Add item
# 3. Update price
# 4. Delete item
# 5. Exit
# Only prints. Doesn’t return anything.

def show_options():
    print("What would you like to do?")
    print("1. Show menu" + "\n" + "2. Add item" + "\n" + "3. Update price" + "\n" + "4. Delete item" + "\n" + "5. Exit")

# show_options()

# f) run_coffee_shop()
# This is the main controller of the program.

# Behavior:
# Keep running in a loop.
# Show options.
# Ask the user to choose (1-5).
# Depending on the choice, call the correct function.


# Rules:
# Invalid choice → print "Invalid choice, try again."
# Choice 5 stops the loop and prints "Goodbye!"

def run_coffee_shop(menu_dict):
    while True:
       show_options()
       action = input("Please choose an action 1-5: ")
       if action.isdigit()==False or int(action) not in range(1,6):
           print("Invalid choice, try again.")
           continue
       if int(action) == 1:
           show_menu(menu_dict)
       elif int(action) == 2:
           add_item(menu_dict)
       elif int(action) == 3:
           update_price(menu_dict)
       elif int(action) == 4:
           delete_item(menu_dict)
       elif int(action) == 5:
           print("Goodbye!")
           break
    print(menu)      

run_coffee_shop(menu)
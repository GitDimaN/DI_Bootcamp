# Exercise 7: Temperature Advice
# Goal: Generate a random temperature and provide advice based on the temperature range.

# Key Python Topics:
# Functions
# Conditionals (if / elif)
# Random numbers
# Floating-point numbers (Bonus)
# Handling seasons (Bonus)

import random

# Step 1: Create the get_random_temp() Function
# Create a function called get_random_temp() that returns a random integer between -10 and 40 degrees Celsius.

# Step 2: Create the main() Function
# Create a function called main(). Inside this function:
# Call get_random_temp() to get a random temperature.
# Store the temperature in a variable and print a friendly message like:
# “The temperature right now is 32 degrees Celsius.”

# Step 3: Provide Temperature-Based Advice
# Inside main(), provide advice based on the temperature:
# Below 0°C: e.g., “Brrr, that’s freezing! Wear some extra layers today.”
# Between 0°C and 16°C: e.g., “Quite chilly! Don’t forget your coat.”
# Between 16°C and 23°C: e.g., “Nice weather.”
# Between 24°C and 32°C: e.g., “A bit warm, stay hydrated.”
# Between 32°C and 40°C: e.g., “It’s really hot! Stay cool.”

# Expected Output:
# The temperature right now is 32 degrees Celsius.
# It's really hot! Stay cool.

def get_random_temp():
    return random.randint(-10, 40) # for integer temperatures

def main():
    temperature = get_random_temp()
    print(f"The temperature right now is {temperature} degrees Celsius.")
    if temperature < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif temperature <= 16:
        print("Quite chilly! Don’t forget your coat.")
    elif temperature <= 23:
        print("Nice weather.")
    elif temperature <= 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It’s really hot! Stay cool.")
main()

# Step 4: Floating-Point Temperatures (Bonus)
# Modify get_random_temp() to return a random floating-point number using random.uniform() for more accurate temperature values.

def get_random_temp():
    return random.uniform(-10, 40) # for float temperatures
main()

# Step 5: Month-Based Seasons (Bonus)
# Instead of directly generating a random temperature, ask the user for a month (1-12) and determine the season using if/elif conditions.
# Modify get_random_temp() to return temperatures specific to each season.

def get_random_temp_by_season(month):
    if month < 3 or month == 12:
        temp_LB=-10; temp_UB = 0
    elif month < 5 or month > 9:
        temp_LB=0; temp_UB = 16
    elif month < 7:
        temp_LB=16; temp_UB = 23
    elif month == 7:
        temp_LB=23; temp_UB = 32
    else:
        temp_LB=32; temp_UB = 40
    return random.uniform(temp_LB, temp_UB) # for float temperatures

def main():
    month = int(input("please specify the current month 1-12: "))
    temperature = get_random_temp_by_season(month)
    print(f"The temperature right now is {temperature} degrees Celsius.")
    if temperature < 0:
        print("Brrr, that’s freezing! Wear some extra layers today.")
    elif temperature <= 16:
        print("Quite chilly! Don’t forget your coat.")
    elif temperature <= 23:
        print("Nice weather.")
    elif temperature <= 32:
        print("A bit warm, stay hydrated.")
    else:
        print("It’s really hot! Stay cool.")
main()

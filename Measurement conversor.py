# Function to convert inches to feet
def inches_to_feet(inches):
    return inches / 12

# Function to convert feet to inches
def feet_to_inches(feet):
    return feet * 12

# Function to convert feet to yards
def feet_to_yards(feet):
    return feet / 3

# Function to convert yards to feet
def yards_to_feet(yards):
    return yards * 3

# Function to convert meters to feet
def meters_to_feet(meters):
    return meters * 3.28084

# Function to convert feet to meters
def feet_to_meters(feet):
    return feet / 3.28084

# Function to display the menu of conversion options
def display_menu():
    print("Please select an option:")
    print("1. Convert inches to feet")
    print("2. Convert feet to inches")
    print("3. Convert feet to yards")
    print("4. Convert yards to feet")
    print("5. Convert meters to feet")
    print("6. Convert feet to meters")

# Function to get the user's choice from the menu
def get_choice():
    choice = int(input("Enter your choice: "))
    return choice

# Function to get the value to be converted
def get_value():
    value = float(input("Enter the value to be converted: "))
    return value

# Main program
while True:
    display_menu()
    choice = get_choice()
    
    if choice == 1:
        value = get_value()
        print(value, "inches is equal to", inches_to_feet(value), "feet")
    elif choice == 2:
        value = get_value()
        print(value, "feet is equal to", feet_to_inches(value), "inches")
    elif choice == 3:
        value = get_value()
        print(value, "feet is equal to", feet_to_yards(value), "yards")
    elif choice == 4:
        value = get_value()
        print(value, "yards is equal to", yards_to_feet(value), "feet")
    elif choice == 5:
        value = get_value()
        print(value, "meters is equal to", meters_to_feet(value), "feet")
    elif choice == 6:
        value = get_value()
        print(value, "feet is equal to", feet_to_meters(value), "meters")
    else:
        print("Invalid choice, please try again.")

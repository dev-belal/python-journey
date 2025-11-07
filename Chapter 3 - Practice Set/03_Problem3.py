""" Program to detect double spaces in a string """

# Taking input from user
text = input("Enter a string: ")

# Detecting double spaces
double_space_index = text.find("  ")

# Checking if double space exists
if double_space_index != -1:
    print(f"Double space found at index {double_space_index}")
else:
    print("No double spaces found!")

""" Program to replace double spaces with 
single space in a string """

# Taking input from user
text = input("Enter a string: ")

# Detecting double spaces
double_space_index = text.find("  ")

# Checking if double space exists and the replacing it with sinle space
if double_space_index != -1:
    double_space_removed = text.replace("  ", " ")
    print(f"Double space found and replaced with single space\n{double_space_removed}")
else:
    print("No double spaces found!")
    print(f"{text}")

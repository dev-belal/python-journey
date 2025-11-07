# --------------------------------------------
#  Lists in Python
# --------------------------------------------
# Definition:
# A List is a collection of ordered and changeable (mutable) items.
# Lists can store multiple values of different data types (string, int, float, etc.)
# They are created using square brackets [].

# Example List
friends = ["Ali", "Ahmed", "Sara", "Bilal", 25]

# Printing the whole list
print(friends)

# Accessing elements using index
print(friends[0])   # Prints the first element
print(friends[2])   # Prints the third element

# Changing an element (lists are mutable)
friends[1] = "Hassan"
print(friends)

# Adding a new item at the end of the list
friends.append("Zain")
print(friends)

# Removing an item from the list
friends.remove("Sara")
print(friends)

# Slicing a list (prints elements from index 1 to 3)
print(friends[1:4])

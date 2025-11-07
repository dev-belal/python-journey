# --------------------------------------------
# 🔹 Tuples in Python
# --------------------------------------------

# 📘 Definition:
# A Tuple is an ordered and immutable(unchangeable) collection of items.
# - Ordered: The items have a fixed order and can be accessed using indexes.
# - Immutable: Once created, you cannot change, add, or remove items.
# - Tuples are written using round brackets ().

# Example of a Tuple
tup = (10, 20, 30, 40, 50)
print("Tuple:", tup)

# --------------------------------------------
# 🔸 Accessing Tuple Elements
print("First element:", tup[0])       # Indexing
print("Last element:", tup[-1])       # Negative Indexing
print("Slice from 1 to 3:", tup[1:4]) # Slicing

# --------------------------------------------
# 🔸 Tuple with Mixed Data Types
mixed = ("Bylal", 21, True, 78.9)
print("Mixed Tuple:", mixed)

# --------------------------------------------
# 🔸 Tuple with One Element
# NOTE: You must add a comma at the end, otherwise it will not be recognized as a tuple
single = (5,)
print("Single Element Tuple:", single)

# --------------------------------------------
# 🔸 Tuple Methods
# count()  → Returns the number of times a value occurs
# index()  → Returns the index of the first occurrence of a value
numbers = (1, 2, 3, 2, 4, 2)
print("Count of 2:", numbers.count(2))
print("Index of 3:", numbers.index(3))

# Extra Operations (not methods but useful with tuples)
print("Length of tuple:", len(tup))        # Get the number of elements
print("Max value:", max(tup))              # Get the largest value
print("Min value:", min(tup))              # Get the smallest value
print("Sum of all values:", sum(tup))      # Sum of all numeric items
print("Is 40 in tuple?", 40 in tup)        # Membership test (True/False)

# --------------------------------------------
# 🔸 Tuple is Immutable (Example)
# The below line will cause an error if uncommented, because tuples cannot be changed
# tup[0] = 100

# --------------------------------------------
# 📘 Summary:
# ✅ Tuples are like lists bt immutable
# ✅ Use () instead of []
# ✅ Faster and more memory-efficient than lists
# ✅ Used for fixed collections of items
# --------------------------------------------

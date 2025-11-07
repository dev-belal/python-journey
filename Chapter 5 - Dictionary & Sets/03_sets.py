# --------------------------------------------
# 🔹 Sets in Python
# --------------------------------------------

# 📘 Definition:
# A set is an unordered collection of unique elements.
# Sets do not allow duplicate values.
# Sets are defined using curly braces { }.

# Example:
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# Duplicates are automatically removed
numbers = {1, 2, 2, 3, 4, 4, 5}
print("Unique Numbers:", numbers)  # Output: {1, 2, 3, 4, 5}

# --------------------------------------------
# Adding elements
my_set.add(6)
print("After adding 6:", my_set)

# Adding multiple elements using update()
my_set.update([7, 8, 9])
print("After update:", my_set)

# --------------------------------------------
# Removing elements
my_set.remove(3)     # Removes 3, raises error if not found
print("After removing 3:", my_set)

my_set.discard(10)   # No error even if 10 is not present
print("After discard(10):", my_set)


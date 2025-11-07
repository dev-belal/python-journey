# --------------------------------------------
# Problem 9: Mutable vs Immutable in Sets
# --------------------------------------------

# s = {8, 7, 12, "Harry", [1, 2]}
# ❌ Error: Lists are mutable (changeable), so they cannot be added to a set.

# Example of allowed types:
s = {8, 7, 12, "Harry", (1, 2)}  # ✅ Tuple is immutable, allowed
print(s)

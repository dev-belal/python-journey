"""Program to Demonstrate immutability of tuples"""

# Concept: Tuples are immutable → their elements cannot be changed after creation.

a = (2, "bylal", 6, 8)
print("Original Tuple:", a)

# Trying to change a value will cause an error
# a[1] = "Byla"  # ❌ TypeError: 'tuple' object does not support item assignment

print("Tuples are immutable — elements cannot be modified.")

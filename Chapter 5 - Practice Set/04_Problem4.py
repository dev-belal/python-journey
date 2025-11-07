# --------------------------------------------
# Problem 4: Length of Set After Operations
# --------------------------------------------

s = set()
s.add(20)
s.add(20.0)
s.add("20")

# Note: 20 and 20.0 are considered equal in Python, so only one of them is stored.
print("Set contents:", s)
print("Length of set is:", len(s))  # Output: 2

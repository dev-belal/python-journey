# --------------------------------------------
# Problem 3: Can Set Have 18 and "18"?
# --------------------------------------------

# Yes! Because 18 (integer) and "18" (string) are of different data types.
s = set()
s.add(18)
s.add("18")
print(s)  # Output: {18, '18'}

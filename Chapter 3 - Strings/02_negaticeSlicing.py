""" Negative String Slicing in Python """

# Take a string 'name'
name = "Bylal"

# Negative Slicing:
# Negative indexes count from the end of the string.
#  B   y   l   a   l
# -5  -4  -3  -2  -1
print(name[-5:-2])   # Output: Byl
# Explanation: Starts from index -5 (B) and goes up to -2 (exclusive, i.e., stops before the last 'a' position)

# Tricky Notation Examples:

# name[:4] → same as name[0:4]
print(name[:4])      # Output: Byla
# Explanation: Starts from beginning (index 0) and ends at index 4 (exclusive).

# name[1:] → same as name[1:5]
print(name[1:])      # Output: ylal
# Explanation: Starts from index 1 (y) to the end of the string (since end index is not given).

# Negative step example (reversing a string)
print(name[::-1])    # Output: lal yB
# Explanation: When step = -1, it reads the string backward (reverses it).

# Another example using negative slicing range
print(name[-3:])     # Output: lal
# Explanation: Starts from 3rd character from the end (-3 = 'l') and goes to the end.

print(name[:-3])     # Output: By
# Explanation: Takes all characters up to index -3 (exclusive).

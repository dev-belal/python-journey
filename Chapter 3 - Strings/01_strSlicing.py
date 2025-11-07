""" String Slicing in Python """

# Take a string 'name'
name = "Bylal"

# String Slicing
# Syntax: string[start:end]
# It extracts characters from index 'start' to 'end - 1' (end is not included)
nameShort = name[0:4]
print(nameShort)      # Output: Byla
# Explanation: Takes characters from index 0 (B) to 3 (a). 
# The character at index 4 (l) is NOT included.

# Example 2: Slicing from middle
print(name[1:4])      # Output: yla
# Explanation: Starts from index 1 (y) and stops before index 4 (l).

# Example 3: Omitting start index
print(name[:3])       # Output: Byl
# Explanation: When 'start' is omitted, slicing starts from the beginning (index 0).

# Example 4: Omitting end index
print(name[2:])       # Output: lal
# Explanation: When 'end' is omitted, slicing continues till the end of the string.

# Example 5: Using step value
print(name[0:5:2])    # Output: Bla
# Explanation: Starts at index 0, goes up to 5 (exclusive), taking every 2nd character.

# Example 6: Full string with slicing
print(name[:])        # Output: Bylal
# Explanation: Returns the entire string since both start and end are omitted.

# Example 7: Reversing the string using slicing
print(name[::-1])     # Output: lal yB
# Explanation: A step of -1 reverses the string.

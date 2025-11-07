""" String Functions in Python """

# len() Function – Returns the number of characters in a string
name = "Bylal"
print(len(name))        # Output: 5

# endswith() Function – Checks if the string ends with a specific substring
print(name.endswith("lal"))   # Output: True

# startswith() Function – Checks if the string starts with a specific substring
print(name.startswith("By"))  # Output: True

# lower() Function – Converts all characters in the string to lowercase
print(name.lower())     # Output: bylal

# upper() Function – Converts all characters in the string to uppercase
print(name.upper())     # Output: BYLAL

# capitalize() Function – Converts the first character to uppercase and the rest to lowercase
print(name.capitalize())  # Output: Bylal

# title() Function – Capitalizes the first letter of every word in the string
sentence = "hello world from bylal"
print(sentence.title())   # Output: Hello World From Bylal

# strip() Function – Removes any leading and trailing spaces from the string
text = "   hello world   "
print(text.strip())      # Output: hello world

# replace() Function – Replaces a substring with another substring
print(name.replace("By", "I"))  # Output: Ilal

# find() Function – Returns the index of the first occurrence of a substring
print(name.find("l"))    # Output: 2  (index of first occurrence)

# count() Function – Returns the number of times a substring appears in the string
print(name.count("l"))   # Output: 2

# split() Function – Splits the string into a list of words based on spaces (default) or a given separator
sentence = "Python is fun"
print(sentence.split())  # Output: ['Python', 'is', 'fun']

# join() Function – Joins elements of a list into a single string with a given separator
words = ["Bylal", "is", "awesome"]
print(" ".join(words))   # Output: Bylal is awesome

# isalpha() Function – Checks if all characters in the string are alphabetic (no digits or spaces)
print(name.isalpha())    # Output: True

# isdigit() Function – Checks if all characters in the string are digits
num = "12345"
print(num.isdigit())     # Output: True

# isalnum() Function – Checks if all characters are alphanumeric (letters and/or digits)
print("Bylal123".isalnum())  # Output: True

# swapcase() Function – Converts uppercase characters to lowercase and vice versa
mixed = "HeLLo"
print(mixed.swapcase())  # Output: hEllO

# center() Function – Centers the string within a specified width, using a specified fill character
print(name.center(10, "-"))  # Output: --Bylal---

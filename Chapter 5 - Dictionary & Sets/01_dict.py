# --------------------------------------------
# 🗂️ Dictionary in Python
# --------------------------------------------

# 📘 Definition:
# A dictionary is a collection of key-value pairs.
# Each key in a dictionary is unique and is used to access its corresponding value.
# Syntax: dictionary = {key1: value1, key2: value2, ...}

# Example:
student = {
    "name": "Bylal",
    "age": 26,
    "grade": "A",
    "subjects": ["Math", "Science", "English"]
}

print("Dictionary:", student)

# Accessing values using keys
print("Name:", student["name"])       # Output: Bylal
print("Subjects:", student["subjects"])  # Output: ['Math', 'Science', 'English']


# Adding new key-value pair
student["school"] = "Bright Future High School"
print("\nAfter adding school:", student)

# Updating existing value
# student["grade"] = "A+"
student.update({"Bylal":" B+"})
print("After updating grade:", student)

# Removing a key-value pair
student.pop("age")
print("After removing 'age':", student)


# --------------------------------------------
# 🗂️ Dictionary Methods in Python
# --------------------------------------------

# Example dictionary
student = {
    "name": "Bylal",
    "age": 20,
    "grade": "A"
}

print("Original Dictionary:", student)

# --------------------------------------------
# 1️⃣ get() → Returns the value for a key, or None if key not found
print("\nget('name'):", student.get("name"))       # Output: Bylal
print("get('school'):", student.get("school"))     # Output: None (no error)

# --------------------------------------------
# 2️⃣ keys() → Returns all keys in the dictionary
print("\nKeys:", student.keys())                   # Output: dict_keys(['name', 'age', 'grade'])

# --------------------------------------------
# 3️⃣ values() → Returns all values in the dictionary
print("Values:", student.values())                 # Output: dict_values(['Bylal', 20, 'A'])

# --------------------------------------------
# 4️⃣ items() → Returns all key-value pairs as tuples
print("Items:", student.items())                   # Output: dict_items([('name', 'Bylal'), ('age', 20), ('grade', 'A')])

# --------------------------------------------
# 5️⃣ update() → Updates dictionary with new key-value pairs
student.update({"grade": "A+", "school": "Bright Future"})
print("\nAfter update():", student)

# --------------------------------------------
# 6️⃣ pop() → Removes a key and returns its value
removed_value = student.pop("age")
print("After pop('age'):", student)
print("Removed Value:", removed_value)

# --------------------------------------------
# 7️⃣ popitem() → Removes the last inserted key-value pair
student.popitem()
print("After popitem():", student)

# --------------------------------------------
# 8️⃣ clear() → Removes all items from the dictionary
temp = {"x": 1, "y": 2}
temp.clear()
print("\nAfter clear():", temp)                    # Output: {}

# --------------------------------------------
# 9️⃣ copy() → Returns a shallow copy of the dictionary
copy_dict = student.copy()
print("Copied Dictionary:", copy_dict)

# --------------------------------------------
# 🔟 fromkeys() → Creates a new dictionary with specified keys and a default value
keys = ["a", "b", "c"]
new_dict = dict.fromkeys(keys, 0)
print("\nNew Dictionary using fromkeys():", new_dict)

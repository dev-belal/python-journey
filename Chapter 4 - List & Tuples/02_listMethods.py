# --------------------------------------------
# 🔹 Common List Methods in Python (with Examples)
# --------------------------------------------

# Creating a list
numbers = [5, 2, 9, 1, 7]

print("Original List:", numbers)

# 1️⃣ append() → Adds an element at the end of the list
numbers.append(10)
print("After append(10):", numbers)

# 2️⃣ insert() → Inserts an element at a specific position
numbers.insert(2, 99)  # Insert 99 at index 2
print("After insert(2, 99):", numbers)

# 3️⃣ remove() → Removes the first occurrence of a specified value
numbers.remove(9)
print("After remove(9):", numbers)

# 4️⃣ pop() → Removes the last element (or by index)
numbers.pop()   # Removes the last element
print("After pop():", numbers)

# 5️⃣ sort() → Sorts the list in ascending order
numbers.sort()
print("After sort():", numbers)

# 6️⃣ reverse() → Reverses the order of elements
numbers.reverse()
print("After reverse():", numbers)

# --------------------------------------------
# 📘 Summary: Common List Methods
# append()  → Add to end
# insert()  → Add at specific index
# remove()  → Delete specific element
# pop()     → Delete last element
# sort()    → Arrange in ascending order
# reverse() → Reverse the list order
# --------------------------------------------

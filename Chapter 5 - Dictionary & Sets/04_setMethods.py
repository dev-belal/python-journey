# --------------------------------------------
# 🔹 Set Methods in Python
# --------------------------------------------

# Example set
numbers = {1, 2, 3, 4, 5}
print("Original Set:", numbers)

# --------------------------------------------
# 1️⃣ add() → Adds an element to the set
numbers.add(6)
print("After add(6):", numbers)

# --------------------------------------------
# 2️⃣ update() → Adds multiple elements (from list, tuple, or another set)
numbers.update([7, 8, 9])
print("After update([7, 8, 9]):", numbers)

# --------------------------------------------
# 3️⃣ remove() → Removes a specific element (raises error if not found)
numbers.remove(3)
print("After remove(3):", numbers)

# --------------------------------------------
# 4️⃣ discard() → Removes an element (no error if element doesn’t exist)
numbers.discard(10)
print("After discard(10):", numbers)

# --------------------------------------------
# 5️⃣ pop() → Removes and returns an arbitrary(random) element
removed = numbers.pop()
print("Removed element:", removed)
print("After pop():", numbers)

# --------------------------------------------
# 6️⃣ clear() → Removes all elements from the set
temp = {10, 11, 12}
temp.clear()
print("After clear():", temp)


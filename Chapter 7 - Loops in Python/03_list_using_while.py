# 🧠 USING WHILE LOOP WITH LISTS IN PYTHON
# You can use a while loop to iterate through a list or to build one dynamically.

# ✅ Example 1: Iterate through a list using while loop
fruits = ["apple", "banana", "cherry", "mango"]
i = 0
while i < len(fruits):
    print("Fruit:", fruits[i])
    i += 1
# Output:
# Fruit: apple
# Fruit: banana
# Fruit: cherry
# Fruit: mango


# ✅ Example 2: Create a list using while loop
numbers = []
i = 1
while i <= 5:
    numbers.append(i)   # Add numbers to the list
    i += 1
print("Numbers list:", numbers)
# Output:
# Numbers list: [1, 2, 3, 4, 5]


# ✅ Example 3: Remove items from a list using while loop
colors = ["red", "green", "blue", "yellow"]
while colors:
    print("Removing:", colors.pop())
print("All colors removed, list is now:", colors)
# Output:
# Removing: yellow
# Removing: blue
# Removing: green
# Removing: red
# All colors removed, list is now: []

# 🧠 FOR LOOP IN PYTHON
# A 'for' loop is used to iterate (loop) over a sequence such as a list, tuple, string, or range.
# It automatically goes through each element in the sequence — no need for manual counters.

# 🧩 Syntax:
# for variable in sequence:
#     statement(s)


# ✅ Example 1: Loop through a list
fruits = ["apple", "banana", "cherry", "mango"]
for fruit in fruits:
    print("Fruit:", fruit)
# Output:
# Fruit: apple
# Fruit: banana
# Fruit: cherry
# Fruit: mango


# ✅ Example 2: Loop through a string
for letter in "Python":
    print(letter)
# Output:
# P
# y
# t
# h
# o
# n


# ✅ Example 3: Using range() in for loop
# range(start, stop, step)
for i in range(1, 6):
    print("Number:", i)
# Output:
# Number: 1
# Number: 2
# Number: 3
# Number: 4
# Number: 5


# ✅ Example 4: Using break and continue
for i in range(1, 6):
    if i == 3:
        continue   # skip 3
    if i == 5:
        break      # stop loop when i == 5
    print("Loop value:", i)
# Output:
# Loop value: 1
# Loop value: 2
# Loop value: 4


# ✅ Example 5: Nested for loop
colors = ["red", "green"]
objects = ["car", "ball"]
for color in colors:
    for obj in objects:
        print(color, obj)
# Output:
# red car
# red ball
# green car
# green ball

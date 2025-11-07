# 🧠 FOR LOOP ITERATION IN PYTHON
# The 'for' loop is mainly used to iterate (go through) items in a sequence such as a list, tuple, string, or range.
# Each iteration picks one element from the sequence and runs the loop body.

# 🧩 Syntax:
# for variable in sequence:
#     statement(s)


# ✅ Example 1: Iterating through a list
names = ["Ali", "Sara", "Zain", "Hina"]
for name in names:
    print("Hello,", name)
# Output:
# Hello, Ali
# Hello, Sara
# Hello, Zain
# Hello, Hina


# ✅ Example 2: Iterating through a string
for letter in "Python":
    print("Letter:", letter)
# Output:
# Letter: P
# Letter: y
# Letter: t
# Letter: h
# Letter: o
# Letter: n


# ✅ Example 3: Iterating using range()
for i in range(5):  # range(5) = 0,1,2,3,4
    print("Iteration number:", i)
# Output:
# Iteration number: 0
# Iteration number: 1
# Iteration number: 2
# Iteration number: 3
# Iteration number: 4


# ✅ Example 4: Iterating through list with index using range(len())
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print("Index:", i, "| Fruit:", fruits[i])
# Output:
# Index: 0 | Fruit: apple
# Index: 1 | Fruit: banana
# Index: 2 | Fruit: cherry


# ✅ Example 5: Iterating through a dictionary
student = {"name": "Ali", "age": 20, "grade": "A"}
for key, value in student.items():
    print(key, ":", value)
# Output:
# name : Ali
# age : 20
# grade : A

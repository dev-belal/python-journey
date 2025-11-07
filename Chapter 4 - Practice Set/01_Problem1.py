
"""Program to Store 7 fruits entered by user in a list"""

# Concept: Lists in Python can store multiple items in one variable.

fruits = []  # Empty list to store fruits

# Using Manual append
# f1 = input("Enter Fruit Name: ")
# fruits.append(f1)
# f2 = input("Enter Fruit Name: ")
# fruits.append(f2)
# f3 = input("Enter Fruit Name: ")
# fruits.append(f3)
# f4 = input("Enter Fruit Name: ")
# fruits.append(f4)
# f5 = input("Enter Fruit Name: ")
# fruits.append(f5)
# f6 = input("Enter Fruit Name: ")
# fruits.append(f6)
# f7 = input("Enter Fruit Name: ")
# fruits.append(f7)


# Using For Loop
for i in range(7):
    fruit = input(f"Enter fruit {i+1}: ")
    fruits.append(fruit)

print("\nList of fruits entered:", fruits)

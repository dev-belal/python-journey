# --------------------------------------------
# Problem 2: Display Unique Numbers Entered by User
# --------------------------------------------

numbers = set()  # Using a set to automatically remove duplicates

# Using Individual input() execution
num = int(input(f"Enter number 1: "))
numbers.add(num)
num = int(input(f"Enter number 2: "))
numbers.add(num)
num = int(input(f"Enter number 3: "))
numbers.add(num)
num = int(input(f"Enter number 4: "))
numbers.add(num)
num = int(input(f"Enter number 5: "))
numbers.add(num)
num = int(input(f"Enter number 6: "))
numbers.add(num)
num = int(input(f"Enter number 7: "))
numbers.add(num)
num = int(input(f"Enter number 8: "))
numbers.add(num)

# Using For Loop
# for i in range(8):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.add(num)

print("Unique numbers are:", numbers)

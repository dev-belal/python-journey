""" 
🔸 Conditional Expressions in Python (Ternary Operator)
A conditional expression lets you write an if-else statement in one line.
It checks a condition and returns one value if True, another if False.

Syntax:
    value_if_true if condition else value_if_false
"""

# Example 1: Find the greater number
a = 10
b = 20

# If a > b, return a else return b
max_num = a if a > b else b
print("The greater number is:", max_num)    # Output: 20


# Example 2: Even or Odd check
num = int(input("Enter a number: "))

# If num is divisible by 2, it's Even else Odd
result = "Even" if num % 2 == 0 else "Odd"
print(f"The number {num} is {result}.")     # Output: Even (if num=4)


# Example 3: Pass or Fail
marks = int(input("Enter your marks: "))

# If marks >= 40 → Pass, else Fail
status = "Pass ✅" if marks >= 40 else "Fail ❌"
print("Result:", status)


# Example 4: Nested Conditional Expression (Advanced)
age = int(input("Enter your age: "))

# If age >= 18 → 'Adult', elif 13–17 → 'Teenager', else → 'Child'
category = "Adult" if age >= 18 else ("Teenager" if age >= 13 else "Child")
print(f"You are a {category}.")

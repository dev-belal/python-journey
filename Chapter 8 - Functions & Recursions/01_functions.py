# ✅ Functions in Python
# A function is a block of reusable code that performs a specific task.
# It helps make code modular, organized, and easier to maintain.

#  Syntax:
# def function_name(parameters):
#     """optional docstring"""
#     statement(s)
#     return value (optional)

# 🧩 Example:
# Defining a Function
def greet(name):
    """This function greets the person passed as a parameter."""
    print(f"Hello, {name}! Welcome to Python.")

# Calling the function
name = input("Enter your name: ")
greet(name)

# Function with return value
def add_numbers(a, b):
    """Returns the sum of two numbers."""
    return a + b

result = add_numbers(5, 10)
print("Sum:", result)

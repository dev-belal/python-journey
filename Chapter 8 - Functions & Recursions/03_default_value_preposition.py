# ✅ Default Argument Values in Python
# Default arguments are used when you want to give a parameter a default value.
# If no value is provided during the function call, the default is used.

#  Syntax:
# def function_name(arg1=value1, arg2=value2, ...):
#     statement(s)

# 🧩 Example:

def greet(name, message="Welcome to Python!"):
    """Function with default argument"""
    print(f"Hello {name}, {message}")

# Calling function with both arguments
greet("Ninja", "Good to see you!")

# Calling function with only one argument (uses default value)
greet("Ayaan")

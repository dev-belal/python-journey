# ✅ RECURSION IN PYTHON
# Recursion is a process where a function calls itself to solve smaller parts of a problem.
# Every recursive function must have a **base case** (to stop recursion) 
# and a **recursive case** (where the function calls itself).

#  Syntax:
# def function_name(parameters):
#     if base_condition:
#         return value
#     else:
#         return function_name(modified_parameters)

# 🧩 Example 1: Factorial using Recursion
def factorial(n):
    """Returns factorial of n using recursion"""
    if n == 0 or n == 1:  # base case
        return 1
    else:  # recursive case
        return n * factorial(n - 1)

print("Factorial of 5 is:", factorial(5))  # Output: 120


# 🧩 Example 2: Sum of first n natural numbers using Recursion
def sum_natural(n):
    """Returns sum of first n natural numbers"""
    if n == 0:  # base case
        return 0
    else:   # recursive case
        return n + sum_natural(n - 1)

print("Sum of first 5 numbers is:", sum_natural(5))  # Output: 15

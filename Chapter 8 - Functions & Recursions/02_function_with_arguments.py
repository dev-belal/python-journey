# ✅ Function with Arguments in Python
# Arguments are values passed to a function when it is called.
# They allow functions to work dynamically with different data.

#  Syntax:
# def function_name(arg1, arg2, ...):
#     statement(s)

# 🧩 Example:

def introduce(name, age):
    """Function with arguments"""
    print(f"My name is {name} and I am {age} years old.")

# Calling function with arguments
introduce("Ninja", 22)
introduce("Ayaan", 18)

userName = input("What is your name: ")
userAge = int(input("What is your age: "))
introduce(userName, userAge)
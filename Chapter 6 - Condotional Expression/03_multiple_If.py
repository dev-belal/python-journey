# 🧠 Explanation:
# Multiple `if` statements in Python are independent of each other.
# Unlike an if-elif-else ladder, all conditions are checked — 
# not just until one is True. This means multiple blocks can execute.

# 🧩 Syntax:
# if condition1:
#     statement(s)
# if condition2:
#     statement(s)
# if condition3:
#     statement(s)

# ✅ Example:
age = 25
income = 60000
has_license = True

if age >= 18:
    print("✅ You are an adult.")
if income > 50000:
    print("💰 You have a good income.")
if has_license:
    print("🚗 You can drive a car.")

# Output:
# ✅ You are an adult.
# 💰 You have a good income.
# 🚗 You can drive a car.

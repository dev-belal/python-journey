# 🧠 Explanation:
# In Python, the if-elif-else ladder is used for decision-making.
# - `if` checks the first condition.
# - `elif` (else if) checks the next condition(s) if previous ones are False.
# - `else` executes when none of the above conditions are True.

# 🧩 Syntax:
# if condition1:
#     statement(s)
# elif condition2:
#     statement(s)
# elif condition3:
#     statement(s)
# else:
#     statement(s)

# ✅ Example:
marks = 85

if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
else:
    print("Grade: F")

# Output: Grade: A

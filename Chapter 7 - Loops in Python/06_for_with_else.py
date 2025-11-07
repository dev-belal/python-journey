# 🧠 FOR LOOP WITH ELSE IN PYTHON
# In Python, a 'for' loop can have an optional 'else' block.
# The 'else' part runs **only if the loop finishes normally** (i.e., no break occurs).

# 🧩 Syntax:
# for variable in sequence:
#     statement(s)
# else:
#     statement(s)  # executes when loop completes without 'break'


# ✅ Example 1: Simple for-else
for i in range(5):
    print("Number:", i)
else:
    print("Loop finished successfully!")
# Output:
# Number: 0
# Number: 1
# Number: 2
# Number: 3
# Number: 4
# Loop finished successfully!


# ✅ Example 2: for-else with break
for i in range(5):
    if i == 3:
        print("Breaking at:", i)
        break
    print("Number:", i)
else:
    print("Loop finished without break.")
# Output:
# Number: 0
# Number: 1
# Number: 2
# Breaking at: 3
# (else block does NOT execute because of break)


# ✅ Example 3: Searching in a list using for-else
names = ["Ali", "Sara", "Hina", "Zain"]
search = "Hina"

for name in names:
    if name == search:
        print(f"{search} found in list!")
        break
else:
    print(f"{search} not found in list.")
# Output:
# Hina found in list!

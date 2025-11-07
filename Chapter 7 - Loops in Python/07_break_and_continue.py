# 🧠 BREAK, CONTINUE, AND PASS STATEMENTS IN PYTHON
# These control the flow of loops by changing how iterations behave.

# ----------------------------------------------------------
# 🔹 1. BREAK STATEMENT
# Used to stop the loop immediately when a condition is met.

print("Example: break statement")
for i in range(1, 6):
    if i == 3:
        print("Breaking at:", i)
        break
    print("Number:", i)
# Output:
# Number: 1
# Number: 2
# Breaking at: 3


# ----------------------------------------------------------
# 🔹 2. CONTINUE STATEMENT
# Used to skip the current iteration and move to the next one.

print("\nExample: continue statement")
for i in range(1, 6):
    if i == 3:
        print("Skipping:", i)
        continue
    print("Number:", i)
# Output:
# Number: 1
# Number: 2
# Skipping: 3
# Number: 4
# Number: 5


# ----------------------------------------------------------
# 🔹 3. PASS STATEMENT
# Used as a placeholder — it does nothing but prevents syntax errors.
# Commonly used when writing empty loops, functions, or condition blocks.

print("\nExample: pass statement")
for i in range(1, 6):
    if i == 3:
        pass   # Placeholder for future code
    else:
        print("Number:", i)
# Output:
# Number: 1
# Number: 2
# Number: 4
# Number: 5

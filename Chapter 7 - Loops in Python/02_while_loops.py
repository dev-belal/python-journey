# 🧠 WHILE LOOP IN PYTHON
# A while loop is used to execute a block of code repeatedly 
# as long as a given condition remains True.

# 🧩 Syntax:
# while condition:
#     statement(s)

# ✅ Example 1: Simple while loop
count = 1
while count <= 5:
    print("Count is:", count)
    count += 1
# Output:
# Count is: 1
# Count is: 2
# Count is: 3
# Count is: 4
# Count is: 5


# ✅ Example 2: Using break
# 'break' stops the loop immediately
num = 1
while num <= 10:
    if num == 6:
        break
    print(num)
    num += 1
# Output:
# 1
# 2
# 3
# 4
# 5


# ✅ Example 3: Using continue
# 'continue' skips the current iteration and moves to the next
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue
    print("Number:", num)
# Output:
# Number: 1
# Number: 2
# Number: 4
# Number: 5


# ✅ Example 4: Infinite while loop (⚠️ Be careful!)
# while True:
#     print("This will run forever until stopped manually (Ctrl + C)")

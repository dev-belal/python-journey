# Program to check if a given name is present in a list

names = ["Ali", "Bilal", "Sara", "Zara", "Hamza"]
user_name = input("Enter name to check: ")

if user_name in names:
    print(f"✅ {user_name} is present in the list.")
else:
    print(f"❌ {user_name} is not present in the list.")

# Program to print multiplication table in reverse order

num = int(input("Enter a number: "))
for i in range(10, 0, -1):
    print(f"{num} x {i} = {num * i}")

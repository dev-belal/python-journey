# 1️⃣ Write a program using functions to find greatest of three numbers.

def greatest(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

print("Greatest number is:", greatest(10, 25, 15))

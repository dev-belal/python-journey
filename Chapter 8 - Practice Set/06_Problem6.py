# 6️⃣ Write a python function which converts inches to centimeters.

def inches_to_cm(inch):
    return inch * 2.54

n = int(input("Enter the value in inches: "))
print(f"The corresponding value in cm is:", inches_to_cm(n))

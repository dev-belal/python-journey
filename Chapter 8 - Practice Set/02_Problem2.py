# 2️⃣ Write a python program using function to convert Celsius to Fahrenheit.

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

temp = int(input("Give me the temperature: "))
print(f"Temperature in Fahrenheit: {celsius_to_fahrenheit(temp)}")

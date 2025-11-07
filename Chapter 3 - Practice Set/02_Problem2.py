""" Program to fill in a letter template with name and date """

# Template
letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

# Taking inputs from user
name = input("Enter your name: ")
date = input("Enter date: ")

# Replacing placeholders with user data
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)

# Displaying the final letter
print("\n----- Final Letter -----")
print(letter)

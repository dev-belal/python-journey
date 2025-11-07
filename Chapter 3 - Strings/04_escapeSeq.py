""" Escape Sequences in Python """

# \n – Newline: Moves the cursor to the next line
print("Hello\nWorld")      
# Output:
# Hello
# World

# \t – Tab: Adds a horizontal tab space
print("Hello\tWorld")      
# Output: Hello   World

# \\ – Backslash: Prints a single backslash
print("This is a backslash: \\")  
# Output: This is a backslash: \

# \' – Single Quote: Allows you to use a single quote inside single-quoted string
print('It\'s a beautiful day!')  
# Output: It's a beautiful day!

# \" – Double Quote: Allows you to use double quotes inside double-quoted string
print("He said, \"Python is amazing!\"")  
# Output: He said, "Python is amazing!"

# \r – Carriage Return: Moves the cursor to the beginning of the same line
print("Hello\rWorld")     
# Output: World   (the "Hello" is overwritten)

# \b – Backspace: Removes the previous character
print("Hello\bWorld")     
# Output: HellWorld  (the 'o' before W is removed)

# \f – Form Feed: Moves the cursor to the next page (rarely used, mostly in printers)
print("Hello\fWorld")     
# Output may look like: HelloWorld

# \a – Bell: Produces a beep sound (if your system supports it)
print("Beep!\a")          
# Output: Beep!  (plus a beep sound)

# \ – Line continuation: Allows a statement to continue on the next line
message = "This is a long sentence \
that continues on the next line."
print(message)
# Output: This is a long sentence that continues on the next line.

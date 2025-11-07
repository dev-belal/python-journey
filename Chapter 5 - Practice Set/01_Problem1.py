# --------------------------------------------
# Problem 1: Hindi-English Dictionary Lookup
# --------------------------------------------

# Creating a dictionary with Hindi words as keys and English meanings as values
dictionary = {
    "pustak": "book",
    "billi": "cat",
    "kutta": "dog",
    "kursi": "chair",
}

# Taking user input
word = input("Enter the Hindi word you want the meaning of: ")

# Displaying the meaning using dictionary lookup
print("The meaning of your word is:", dictionary.get(word, "Word not found in dictionary."))

# 7️⃣ Write a python function to remove a given word from a list and strip it at the same time.

def remove_and_strip(words_list, word_to_remove):
    new_list = [word.strip() for word in words_list if word.strip() != word_to_remove]
    return new_list

words = [" apple ", "banana", " cherry ", "banana "]
print(remove_and_strip(words, "banana"))

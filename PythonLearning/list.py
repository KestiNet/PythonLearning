def get_word(sentence, n):
    words = sentence.split()  # Split the sentence into words
    if n > 0 and n <= len(words):
        return words[n - 1]  # Return the nth word (adjust index for 0-based indexing)
    return ""

print(get_word("This is a lesson about Lists", 4))  # Output: Lists
print(get_word("This is a lesson about Lists", -4))  # Output: ""
print(get_word("Now we are cooking!", 1))  # Output: Now
print(get_word("Now we are cooking!", 5))  # Output: ""

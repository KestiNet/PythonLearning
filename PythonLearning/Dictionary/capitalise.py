def capitalize_highlight_word(sentence, word):
    words = sentence.split()

    capitalized_words = [w.upper() if w.lower() == word.lower() else w for w in words]
    return ' '.join(capitalized_words)

# Example usage:
sentence = "The quick brown fox jumps over the lazy dog"
highlight = "fox"

result = capitalize_highlight_word(sentence, highlight)
print(result)

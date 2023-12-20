import re
# ^: Asserts the start of the string.
# [A-Z]: Matches any uppercase letter at the beginning of the string.
# [a-z\s]+: Matches one or more lowercase letters or spaces after the initial uppercase letter. The \s represents any whitespace character, including spaces.
# [.!?]$: Matches a period, question mark, or exclamation point at the end of the string.
# $: Asserts the end of the string.
#https://docs.python.org/3/howto/regex.html
def check_sentence(text):
  result = re.search(r"^[A-Z][a-z\s]+[.!?]$", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True
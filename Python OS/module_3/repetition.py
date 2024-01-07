import re

print(re.search(r"Py.*n", "Pygmalion"))

print(re.search(r"Py[a-z]*n", "Python Programming"))

print(re.search(r"Py.*n", "Pyn"))

print(re.search(r"o+l+", "goldfish"))

print(re.search(r"o+l+", "boil"))

print(re.search(r"m[a-z]", "Python Programming"))

print(re.search(r"p?each", "To each their own"))

print(re.search(r"p?each", "To peach their own"))
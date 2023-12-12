import re

result = re.search(r"aza", "bazaar")
print(result)

print(re.search(r"^x", "xenon"))

print(re.search(r"p.ng", "penguin"))

print(re.search(r"p.ng", "Pangea", re.IGNORECASE))
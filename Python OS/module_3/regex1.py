import re

result = re.search(r"aza", "bazaar")
print(result)

print(re.search(r"^x", "xenon"))

print(re.search(r"p.ng", "penguin"))

print(re.search(r"p.ng", "Pangea", re.IGNORECASE))

print(re.search(r"[Pp]ython", "python"))

print(re.search(r"[a-z]way", "The end of the highway"))

print(re.search(r"[a-z]way", "what a way to go"))

print(re.search("cloud[a-zA-Z0-9]", "cloudy"))

print(re.search("cloud[a-zA-Z0-9]", "cloud9"))

print(re.search(r"[^a-zA-Z]", "This is a sentence with spaces." ))

print(re.search(r"cat|dog", "I like dogs and cats."))

print(re.findall(r"cat|dog", "I like dogs and cats"))
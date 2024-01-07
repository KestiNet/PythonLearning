import re


print(re.search(r"[a-zA-Z]{5}", "a ghost"))

print(re.findall(r"[a-zA-Z]{5}", "a ghost"))

print(re.findall(r"[a-zA-Z]{5}", "a scary ghost appaeared"))

print(re.findall(r"[a-zA-Z]{5}\b", "a scary ghost appeared"))

print(re.findall(r"\w{5,}", "I really like strawberries"))
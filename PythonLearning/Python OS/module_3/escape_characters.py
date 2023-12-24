import re
print(re.search(r".com", "welcome"))
#\ is an escape character
print(re.search(r".com", "welcome"))
#using the backslash we can search for the dot 
print(re.search(r"\.com", "kestinet.com"))

print(re.search(r"\w*", "This is an example"))

print(re.search(r"\w*", "so_is_this_one"))
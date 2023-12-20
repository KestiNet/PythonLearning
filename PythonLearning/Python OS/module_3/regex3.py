import re
#Checks whether Country starts with an A and ends with a
print(re.search(r"A.*a", "Argentina"))
#Checks whether Country starts with an A and ends with a
print(re.search(r"^A.*a$", "Argentina"))


pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
print(re.search(pattern, "_this_is_a_valid_variable_name"))
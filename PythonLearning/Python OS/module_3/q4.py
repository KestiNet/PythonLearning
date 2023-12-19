import re
#\b: Word boundary.
#\w+: Matches one or more word characters (alphanumeric characters + underscore).
#\s+: Matches one or more whitespace characters.
#The pattern \b\w+\b\s+\b\w+\b ensures that there are at least two groups of alphanumeric characters separated by whitespace.
def check_character_groups(text):
    result = re.search(r'\b\w+\b\s+\b\w+\b', text)
    return result != None


print(check_character_groups("One"))
print(check_character_groups("123 Ready Set Go"))
print(check_character_groups("username user_01"))
print(check_character_groups("shopping list: milk, bread, eggs"))
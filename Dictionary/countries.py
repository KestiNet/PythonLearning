
def countries(countries_dict):
    result = ""

    for country in countries_dict.values():
        result += country + "\n"  # Add a newline character after each country

    return result


print(countries({"Africa" : ["Kenya","Egypt", "Nigeria"], "Asia" : ["China", "India", "Thailand"], "South America": ["Ecuador", "Bolivia", "Brazil"]}))

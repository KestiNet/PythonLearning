def skip_elements(elements):
    every_other = []
    for index, element in enumerate(elements):
        if index % 2 == 0:
            every_other.append(element)

    return every_other

print(skip_elements(["a","b","d","e","f","g"]))
print(skip_elements(['orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))
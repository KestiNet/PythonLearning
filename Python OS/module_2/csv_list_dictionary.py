import csv

users = [{"name": "sol mansi", "username": "solm", "department": "IT infrastructure"},
{"name": "Lio Nelson", "username": "lion", "department": "User experience research"},
{"name" : "Charlie Gray", "username": "greyc", "department": "Development"}]

keys = ["name", "username", "department"]
with open('by_depratment.csv', 'w') as by_depratment:
    writer = csv.DictWriter(by_depratment, fieldnames = keys)
    writer.writeheader()
    writer.writerows(users)
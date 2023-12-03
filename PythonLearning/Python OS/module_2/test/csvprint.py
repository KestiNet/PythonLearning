import csv

csv.register_dialect('empDialect', skipinitialspace=True, strict=True)

test = 'test.csv'

with open(test, 'r') as csvfile:
    employee_file = csv.DictReader(csvfile, dialect='empDialect')

    employee_list = []
    for data in employee_file:
        employee_list.append(data)

print(employee_list)


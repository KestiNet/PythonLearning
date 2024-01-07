#!/usr/bin/env python3

import csv

def read_employees(file_path='/mnt/c/Dev/PythonLearning/PythonLearning/Python OS/module_2/qwiklabs/employees.csv'):
    csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
    employee_file = csv.DictReader(open(file_path), dialect = 'empDialect')
    
    employee_list = []
    for data in employee_file:
        employee_list.append(dict(data))

    return employee_list

employee_list = read_employees('/mnt/c/Dev/PythonLearning/PythonLearning/Python OS/module_2/qwiklabs/employees.csv')

def process_data(employee_list):
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])

    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)
    return department_data

dictionary = process_data(employee_list)

def write_report(dictionary, report_file):
    with open (report_file, "w+") as f:
        for k in sorted(dictionary):
            f.write(str(k) + ':' + str(dictionary[k]) + '\n')
        f.close()
write_report(dictionary, '/mnt/c/Dev/PythonLearning/PythonLearning/Python OS/module_2/qwiklabs/test_report.txt') 

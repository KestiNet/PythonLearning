import csv

csv_file_path = '/Users/esakesti/Desktop/Dev/PythonLearning/PythonLearning/Python OS/module_2/qwiklabs/employees.csv'

try:
    with open(csv_file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        # Print the corrected header
        header = [field.strip() for field in reader.fieldnames]
        print(f"Header: {header}")

        # Print the 'Department' values for each row
        for row in reader:
            department_value = row.get('Department', '').strip()
            print(department_value)
except FileNotFoundError:
    print(f"Error: File '{csv_file_path}' not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
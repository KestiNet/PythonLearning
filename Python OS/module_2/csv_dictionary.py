import csv

with open('organisation.csv') as software:
    reader = csv.DictReader(software)
    for row in reader:
        print(("{} has {} Industry").format(row["Website"], row["Industry"]))

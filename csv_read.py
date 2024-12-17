import csv

with open('holdings.csv') as file:
    content = csv.DictReader(file)
    for row in content:
        print(row)
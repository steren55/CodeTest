import csv

with open('test.csv', newline='') as csvfile:
    rows = csv.reader(csvfile)
    for row in rows:
        print(row)
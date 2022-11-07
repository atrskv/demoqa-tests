import csv

with open('example_csv.csv') as f:
    reader = csv.reader(f)
    for row in range(len(reader.line_num)):
        if row == 3:
            print(row)
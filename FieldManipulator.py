import csv

input_file = 'Population_countries.csv'
output_file = 'output_file.csv'

with open(input_file, 'r') as file:
    reader = csv.reader(file)
    rows = [row for row in reader]

with open(output_file, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows([row[:-1] if row[-1] == '' else row for row in rows])

print("Records shaped successfully.")

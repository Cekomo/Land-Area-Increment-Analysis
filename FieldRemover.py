import csv

input_file = "Coastline_countries.csv"
output_file = "output.csv"

# Open the input and output CSV files
with open(input_file, "r", newline="") as infile, open(output_file, "w", newline="") as outfile:
    reader = csv.reader(infile)
    writer = csv.writer(outfile)

    # Read the header and write it to the output file
    header = next(reader)
    header = [header[0]] + header[2:5] + header[8:]
    writer.writerow(header)

    # Process and write each row
    for row in reader:
        modified_row = [row[0]] + row[2:5] + row[8:]
        writer.writerow(modified_row)

print("Fields deleted and new CSV created.")

import csv

csv_file = "result.csv"
search_value = "[x]"

with open(csv_file, newline='') as file:
    reader = csv.reader(file)
    for row_num, row in enumerate(reader):
        if search_value in row:
            print(f"Found at row {row_num + 1}: {row}")

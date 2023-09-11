import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('/Users/femisokoya/Documents/GitHub/cityandtrainops/result.csv')

# Define the columns with 'r' and 'x' values
integer_columns = [
    "AM peak arrivals (07:00-09:59): Number of services",
    "AM peak arrivals (07:00-09:59): Passengers standing",
    "PM peak arrivals (16:00-18:59): Number of services",
    "PM peak arrivals (16:00-18:59): Passengers standing",
]

decimal_columns = [
    "AM peak arrivals (07:00-09:59): PIXC",
    "PM peak arrivals (16:00-18:59): PIXC",
]

# Initialize lists to store the rows with 'r' and 'x' values
rows_with_r = []
rows_with_x = []

# Iterate through the DataFrame to find 'r' and 'x' values
for index, row in df.iterrows():
    for col in integer_columns:
        if row[col] == 'r':
            rows_with_r.append((index, col))
        elif row[col] == 'x':
            rows_with_x.append((index, col))
    for col in decimal_columns:
        try:
            value = float(row[col])  # Attempt to convert to float
        except ValueError:
            if row[col] == 'r':
                rows_with_r.append((index, col))
            elif row[col] == 'x':
                rows_with_x.append((index, col))

# Print rows with 'r' values
print("Rows with 'r' values:")
for row_info in rows_with_r:
    print(f"Row {row_info[0] + 2}, Column: {row_info[1]}")

# Print rows with 'x' values
print("\nRows with 'x' values:")
for row_info in rows_with_x:
    print(f"Row {row_info[0] + 2}, Column: {row_info[1]}")

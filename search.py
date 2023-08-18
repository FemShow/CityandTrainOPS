import pandas as pd

# Load the CSV data
csv_file = "result.csv"  # Replace with the actual path to your CSV file
df = pd.read_csv(csv_file)

# List out the values of the specified columns
notes_columns = ['Notes', 'Notes1', 'Notes2', 'Notes3', 'Notes4', 'Notes5']
for col in notes_columns:
    values = df[col].unique()
    print(f"Values in {col}:")
    print(values)
    print("\n")

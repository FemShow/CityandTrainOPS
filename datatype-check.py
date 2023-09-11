import pandas as pd

# Load the CSV file into a Pandas DataFrame
csv_file_path = 'result.csv'  # Replace with your CSV file path
df = pd.read_csv(csv_file_path)

# Get the columns and their data types
column_data_types = df.dtypes

# Print the column names and their data types
for column, data_type in column_data_types.iteritems():
    print(f'Column: {column}, Data Type: {data_type}')

import json
import pandas as pd

# Load the JSON configuration
with open('train-crowding-config2.json', 'r') as json_file:
    config = json.load(json_file)

# Extract column names from the JSON configuration
column_names_from_config = []
if 'columns' in config and isinstance(config['columns'], list):
    for col in config['columns']:
        if isinstance(col, dict) and 'name' in col:
            column_names_from_config.append(col['name'])
        else:
            print("Invalid column definition in JSON:", col)
else:
    print("Missing or invalid 'columns' section in JSON configuration.")

# Load the CSV file and get its column headers
df = pd.read_csv('result.csv')
column_headers_from_csv = df.columns.tolist()

# Compare column names
missing_columns = set(column_names_from_config) - set(column_headers_from_csv)
extra_columns = set(column_headers_from_csv) - set(column_names_from_config)

if missing_columns:
    print("Missing columns in CSV:", missing_columns)

if extra_columns:
    print("Extra columns in CSV:", extra_columns)

if not missing_columns and not extra_columns:
    print("Column definitions and headers match.")

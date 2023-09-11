import pandas as pd

# Read the Excel file
file_path = "/Users/femisokoya/Documents/GitHub/cityandtrainops/rai0214.xlsx"
sheet_name = "RAI0214"
df = pd.read_excel(file_path, sheet_name, header=None)

# Set the fifth row as column headers
new_header = df.iloc[4]
df = df[5:]
df.columns = new_header

# Remove '[note 3]' from the 'City' column
df['City'] = df['City'].str.replace(r'\[note 3\]', '', regex=True)

# Dictionary of ONS codes for cities
ons_codes = {
    'Bristol': 'E06000023',
    'Cardiff': 'W06000015',
    'Leeds': 'E08000035',
    'Leicester': 'E06000016',
    'Liverpool': 'E08000012',
    ' London': 'E12000007',
    'London ': 'E12000007',
    'Manchester': 'E08000003',
    'Newcastle': 'E08000021',
    'Nottingham': 'E06000018',
    'Sheffield': 'E08000019',
    'Brighton': 'E06000043',
    'Cambridge': 'E07000008',
    'Reading': 'E06000038',
    'Birmingham': 'E08000025',
    'Birmingham ': 'E08000025'
}

# Insert the 'ONS Code' column and populate it based on the 'City' column
df.insert(df.columns.get_loc('City') + 1, 'ONS Code', df['City'].map(ons_codes))
df.loc[df['City'] == 'London', 'ONS Code'] = 'E12000007'

# Create a new DataFrame to hold the result
result_df = df.copy()

# Function to insert and populate obsStatus columns
def insert_and_populate_obsStatus_column(df, col_name):
    obsStatus_col_name = 'obsStatus'
    count = 0
    while obsStatus_col_name in df.columns:
        count += 1
        obsStatus_col_name = f'obsStatus{count}'
    df.insert(df.columns.get_loc(col_name) + 1, obsStatus_col_name, '')  # Use None for missing values
    
    # Loop through each row and populate obsStatus column
    for index, row in df.iterrows():
        if '[r]' in str(row[col_name]):
            row[obsStatus_col_name] = 'r'
            row[col_name] = row[col_name].replace('[r]', '')
        elif '[x]' in str(row[col_name]):
            row[obsStatus_col_name] = 'x'
            row[col_name] = row[col_name].replace('[x]', '')

# Columns to insert obsStatus columns after
columns_to_process = [
    'AM peak arrivals (07:00-09:59): PIXC [note 1]',
    'AM peak arrivals (07:00-09:59): Passengers standing [note 1]',
    'PM peak arrivals (16:00-18:59): Number of services',
    'PM peak arrivals (16:00-18:59): PIXC [note 1]',
    'PM peak arrivals (16:00-18:59): Passengers standing [note 1]'
]

# Process each specified column
for col_name in columns_to_process:
    insert_and_populate_obsStatus_column(result_df, col_name)

# Remove '[note 1]' from column headers and strip trailing spaces
result_df.columns = result_df.columns.str.replace(r'\[note 1\]', '', regex=True).str.strip()

# Save the resulting dataset as CSV
result_file = "result.csv"
result_df.to_csv(result_file, index=False)

print("Dataset saved as", result_file)
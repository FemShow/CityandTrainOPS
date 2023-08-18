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

# Update 'ONS Code' column based on conditions
df.loc[df['City'] == 'London', 'ONS Code'] = 'E12000007'

# Columns to process (updated without '[note 1]')
observation_columns = [
    'AM peak arrivals (07:00-09:59): Number of services',
    'AM peak arrivals (07:00-09:59): PIXC [note 1]',
    'AM peak arrivals (07:00-09:59): Passengers standing [note 1]',
    'PM peak arrivals (16:00-18:59): Number of services',
    'PM peak arrivals (16:00-18:59): PIXC [note 1]',
    'PM peak arrivals (16:00-18:59): Passengers standing [note 1]'
]

# Loop through each row
for index, row in df.iterrows():
    # Check if 'obsStats' column doesn't exist and '[r]' is present
    if 'obsStats' not in df.columns and any('[r]' in str(value) for value in row[observation_columns].values):
        # Insert 'obsStats' column as the last column
        df.insert(df.shape[1], 'obsStats', '[r]')
        # Update 'obsStats' column with '[r]'
        df.at[index, 'obsStats'] = '[r]'
        # Remove '[r]' from other columns except 'Notes'
        for col in observation_columns:
            if '[r]' in str(row[col]):
                row[col] = row[col].replace('[r]', '')
    
    # Check if 'obsStats1' column doesn't exist and '[x]' is present
    if 'obsStats1' not in df.columns and any('[x]' in str(value) for value in row[observation_columns].values):
        # Insert 'obsStats1' column as the last column
        df.insert(df.shape[1], 'obsStats1', '[x]')
        # Update 'obsStats1' column with '[x]'
        df.at[index, 'obsStats1'] = '[x]'
        # Remove '[x]' from other columns except 'obsStats1'
        for col in observation_columns:
            if '[x]' in str(row[col]):
                row[col] = row[col].replace('[x]', '')

# Remove '[note 1]' from column headers
df.columns = df.columns.str.replace(r'\[note 1\]', '', regex=True)

# Save the resulting dataset as CSV
result_file = "result.csv"
df.to_csv(result_file, index=False)

print("Dataset saved as", result_file)

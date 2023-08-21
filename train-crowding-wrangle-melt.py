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

# Melt the DataFrame
df_melted = pd.melt(df, id_vars=['Year', 'City', 'ONS Code', 'Train operator'], value_vars=observation_columns, var_name='Obs_Type', value_name='Value')

# Fill '[r]' and '[x]' values in 'obsStatus' and 'obsStatus1' columns, respectively
df_melted['obsStatus'] = df_melted['Value'].apply(lambda x: '[r]' if x == '[r]' else '')
df_melted['obsStatus1'] = df_melted['Value'].apply(lambda x: '[x]' if x == '[x]' else '')

# Replace '[r]', '[x]', and '[]' values with nulls/blanks in 'Value' column
df_melted['Value'] = df_melted['Value'].replace({'\[r\]': '', '\[x\]': '', '\[\]': ''}, regex=True)

# Make case-insensitive replacements for 'C2C' and 'MerseyRail'
# df_melted['Value'] = df_melted['Value'].replace({'C2C': 'C2C', 'c2c': 'C2C', 'MerseyRail': 'MerseyRail', 'Merseyrail': 'MerseyRail'})

# Make case-insensitive replacements for 'C2C' and 'MerseyRail' in 'Train operator' column
df_melted['Train operator'] = df_melted['Train operator'].replace({'C2C': 'C2C', 'c2c': 'C2C', 'MerseyRail': 'MerseyRail', 'Merseyrail': 'MerseyRail'}, regex=True)

# Save the melted DataFrame as CSV
result_file_melted = "result_melted.csv"
df_melted.to_csv(result_file_melted, index=False)

print("Melted dataset saved as", result_file_melted)

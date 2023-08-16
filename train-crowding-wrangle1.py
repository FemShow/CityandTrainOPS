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

# Function to insert a notes column
def insert_notes_column(df, col_name):
    notes_col_name = 'Notes'
    if notes_col_name in df.columns:
        count = 1
        while f"{notes_col_name}{count}" in df.columns:
            count += 1
        notes_col_name = f"{notes_col_name}{count}"
    df.insert(df.columns.get_loc(col_name) + 1, notes_col_name, '')
    return notes_col_name

# Insert a notes column after 'AM peak arrivals (07:00-09:59): PIXC [note 1]'
pixc_notes_col = insert_notes_column(result_df, 'AM peak arrivals (07:00-09:59): PIXC [note 1]')

# Insert a notes column after 'AM peak arrivals (07:00-09:59): Passengers standing [note 1]'
standing_notes_col = insert_notes_column(result_df, 'AM peak arrivals (07:00-09:59): Passengers standing [note 1]')

# Insert a notes column after 'PM peak arrivals (16:00-18:59): PIXC [note 1]'
peak_arrivals_col = insert_notes_column(result_df, 'PM peak arrivals (16:00-18:59): PIXC [note 1]')

# Insert a notes column after 'PM peak arrivals (16:00-18:59): PIXC [note 1]'
peak_arrivals1_col = insert_notes_column(result_df, 'PM peak arrivals (16:00-18:59): PIXC [note 1]')

# Insert a notes column after 'PM peak arrivals (16:00-18:59): Passengers standing [note 1]'
stand_notes_col = insert_notes_column(result_df, 'PM peak arrivals (16:00-18:59): Passengers standing [note 1]')

# Insert a notes column after 'PM peak arrivals (16:00-18:59): Passengers standing [note 1]'
stand_notes1_col = insert_notes_column(result_df, 'PM peak arrivals (16:00-18:59): Passengers standing [note 1]')

# Loop through each row
for index, row in result_df.iterrows():
    if '[r]' in str(row['AM peak arrivals (07:00-09:59): PIXC [note 1]']):
        result_df.at[index, pixc_notes_col] = '[r]'
        row['AM peak arrivals (07:00-09:59): PIXC [note 1]'] = row['AM peak arrivals (07:00-09:59): PIXC [note 1]'].replace('[r]', '')

    if '[r]' in str(row['AM peak arrivals (07:00-09:59): Passengers standing [note 1]']):
        result_df.at[index, standing_notes_col] = '[r]'
        row['AM peak arrivals (07:00-09:59): Passengers standing [note 1]'] = row['AM peak arrivals (07:00-09:59): Passengers standing [note 1]'].replace('[r]', '')

    if '[x]' in str(row['PM peak arrivals (16:00-18:59): PIXC [note 1]']):
        result_df.at[index, peak_arrivals_col] = '[x]'
        row['PM peak arrivals (16:00-18:59): PIXC [note 1]'] = row['PM peak arrivals (16:00-18:59): PIXC [note 1]'].replace('[x]', '')

    if '[r]' in str(row['PM peak arrivals (16:00-18:59): PIXC [note 1]']):
        result_df.at[index, peak_arrivals1_col] = '[r]'
        row['PM peak arrivals (16:00-18:59): PIXC [note 1]'] = row['PM peak arrivals (16:00-18:59): PIXC [note 1]'].replace('[r]', '')

    if '[x]' in str(row['PM peak arrivals (16:00-18:59): Passengers standing [note 1]']):
        result_df.at[index, stand_notes_col] = '[x]'
        row['PM peak arrivals (16:00-18:59): Passengers standing [note 1]'] = row['PM peak arrivals (16:00-18:59): Passengers standing [note 1]'].replace('[x]', '')

    if '[r]' in str(row['PM peak arrivals (16:00-18:59): Passengers standing [note 1]']):
        result_df.at[index, stand_notes1_col] = '[r]'
        row['PM peak arrivals (16:00-18:59): Passengers standing [note 1]'] = row['PM peak arrivals (16:00-18:59): Passengers standing [note 1]'].replace('[r]', '')

# Remove '[note 1]' from column headers
result_df.columns = result_df.columns.str.replace(r'\[note 1\]', '', regex=True)

# Save the resulting dataset as CSV
result_file = "result.csv"
result_df.to_csv(result_file, index=False)

print("Dataset saved as", result_file)

import pandas as pd

# Define the input and output file paths
input_csv_file = "/Users/femisokoya/Documents/GitHub/cityandtrainops/result.csv"
output_csv_file = "/Users/femisokoya/Documents/GitHub/cityandtrainops/result_normalized.csv"

# Read the CSV file into a DataFrame
df = pd.read_csv(input_csv_file)

# Normalize values in the 'train operator' column
df['Train operator'] = df['Train operator'].str.strip()  # Remove leading and trailing spaces
df['Train operator'] = df['Train operator'].str.lower()  # Convert to lowercase
df['Train operator'].replace(['c2c', 'c2c '], 'c2c', inplace=True)  # Normalize 'c2c'
df['Train operator'].replace(['merseyrail', 'merseyrail ', 'merseyRail'], 'Merseyrail', inplace=True)  # Normalize 'Merseyrail'

# Save the DataFrame to a new CSV file
df.to_csv(output_csv_file, index=False)

print(f"Normalized data saved to {output_csv_file}")

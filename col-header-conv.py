import pandas as pd

# Read the CSV file
file_path = "/Users/femisokoya/Documents/GitHub/cityandtrainops/result.csv"
df = pd.read_csv(file_path)

# Define the column name mappings
column_mappings = {
    "Year": "Year",
    "City": "City",
    "ONS Code": "ONS_Code",
    "Train operator": "Trn_Op",
    "AM peak arrivals (07:00-09:59): Number of services": "AM_Num",
    "AM peak arrivals (07:00-09:59): PIXC": "AM_PIXC",
    "obsStatus": "obsStatus",
    "AM peak arrivals (07:00-09:59): Passengers standing": "AM_stand",
    "obsStatus1": "obsStatus1",
    "PM peak arrivals (16:00-18:59): Number of services": "PM_Num",
    "obsStatus2": "obsStatus2",
    "PM peak arrivals (16:00-18:59): PIXC": "PM_PIXC",
    "obsStatus3": "obsStatus3",
    "PM peak arrivals (16:00-18:59): Passengers standing": "PM_stand",
    "obsStatus4": "obsStatus4"
}

# Rename the columns
df.rename(columns=column_mappings, inplace=True)

# Save the result to a new CSV file
result_file = "/Users/femisokoya/Documents/GitHub/cityandtrainops/result1.csv"
df.to_csv(result_file, index=False)

print("Result saved as", result_file)

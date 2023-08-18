import pandas as pd

# Load the dataset
data = pd.read_csv("/Users/femisokoya/Documents/GitHub/cityandtrainops/result.csv")

# Define a mapping for annotations/codes
annotations_mapping = {
    "[x]": "Annotation_X",
    "[r]": "Annotation_R"
}

# Replace annotations/codes in the DataFrame
for col in data.columns:
    data[col] = data[col].replace(annotations_mapping)

# Save the modified DataFrame
data.to_csv("train-crowding-modified.csv", index=False)

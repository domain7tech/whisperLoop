import pandas as pd
import numpy as np
import random

# Generate a random start for the sequence
start = random.randint(1001, 15001)

# Read the csv file
df = pd.read_csv('./docsbox/csv/bigcalc/split__1.csv')

# Select the FirstName and LastName columns and store them
original_firstname = df['FirstName'].copy()
original_lastname = df['LastName'].copy()

# Select the FirstName and LastName columns
selected_columns = df[["FirstName", "LastName"]]

# Convert the selected columns into a 2D array
two_d_array = selected_columns.values

# Print the 2D array
for row in two_d_array:
    print(row)

# Create a sequence of integers for the FirstName and LastName columns
df['FirstName'] = np.arange(start, start + len(df))
df['LastName'] = np.arange(start + 4000, start + 4000 + len(df))

# Write the modified DataFrame to a new csv file
df.to_csv('./docsbox/csv/bigcalc/split_1_new.csv', index=False)

# Replace FirstName and LastName with the original data
df['FirstName'] = original_firstname
df['LastName'] = original_lastname

# Write the DataFrame with original FirstName and LastName to a new csv file
df.to_csv('./docsbox/csv/bigcalc/split_1_final.csv', index=False)

# Read the final csv file to check the changes
final_df = pd.read_csv('./docsbox/csv/bigcalc/split_1_final.csv')

# Print the DataFrame
print(final_df)

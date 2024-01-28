from statlib.data_preprocessing import generate_synthetic_data
import json

# Function to convert DataFrame to JSON
def dataframe_to_json(df):
    return df.to_json(orient='records')

# User input for dataset size
while True:
    size_input = input("Enter the dataset size (small=50, medium=1000, large=10000): ").lower()
    if size_input == 'small':
        size = 50
        break
    elif size_input == 'medium':
        size = 1000
        break
    elif size_input == 'large':
        size = 10000
        break
    else:
        print("Invalid input. Please enter 'small', 'medium', or 'large'.")

# Generate the selected dataset using the function from your statlib
df = generate_synthetic_data(size)

# Convert the DataFrame to JSON
json_data = dataframe_to_json(df)

# File name based on selected size
file_name = f"test_data_{size_input}.json"

# Saving to a file
with open(file_name, 'w') as file:
    file.write(json_data)

print(f"Generated {size_input} dataset and saved to {file_name}.")

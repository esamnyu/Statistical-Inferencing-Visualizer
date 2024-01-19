import pandas as pd
import numpy as np
import json

# Function to generate datasets of various sizes
def generate_dataset(size):
    np.random.seed(0)
    X = 2.5 * np.random.randn(size) + 1.5   # Array of 'size' values with mean = 1.5, stddev = 2.5
    res = 0.5 * np.random.randn(size)       # Generate 'size' residual terms
    Y = 2 + 0.3 * X + res                   # Actual values of Y
    
    # Creating a pandas DataFrame
    df = pd.DataFrame({
        'X': X,
        'Y': Y
    })
    
    # Converting the DataFrame to a JSON string
    json_data = df.to_json(orient='records')
    
    # Return the JSON data
    return json_data

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

# Generate the selected dataset
json_data = generate_dataset(size)

# File name based on selected size
file_name = f"test_data_{size_input}.json"

# Saving to a file
with open(file_name, 'w') as file:
    file.write(json_data)

print(f"Generated {size_input} dataset and saved to {file_name}.")

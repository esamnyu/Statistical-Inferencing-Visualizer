import pandas as pd
import numpy as np
import json

# Generating a simple dataset
np.random.seed(0)
X = 2.5 * np.random.randn(100) + 1.5   # Array of 100 values with mean = 1.5, stddev = 2.5
res = 0.5 * np.random.randn(100)       # Generate 100 residual terms
Y = 2 + 0.3 * X + res                  # Actual values of Y

# Creating a pandas DataFrame
df = pd.DataFrame({
    'X': X,
    'Y': Y
})

# Converting the DataFrame to a JSON string
json_data = df.to_json(orient='records')

# Saving to a file (optional)
with open('test_data.json', 'w') as file:
    file.write(json_data)

# json_data now can be used as an input for your API

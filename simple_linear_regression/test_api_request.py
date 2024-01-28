import requests
import json
import plotly.io as pio
import os

# Paths to the images and data directories
images_directory = "/Users/ethansam/Documents/GitHub/Statistical-Inferencing-Visualizer/simple_linear_regression/images"
data_directory = "/Users/ethansam/Documents/GitHub/Statistical-Inferencing-Visualizer/simple_linear_regression/data"

# Ask the user for the size of the dataset they want to test
size_input = input("Enter the dataset size (small=50, medium=1000, large=10000): ").lower()
file_map = {
    'small': 'test_data_small.json',
    'medium': 'test_data_medium.json',
    'large': 'test_data_large.json'
}

# Check if the input is valid and get the corresponding filename
if size_input not in file_map:
    print("Invalid input. Please enter 'small', 'medium', or 'large'.")
    exit()

file_name = os.path.join(data_directory, file_map[size_input])

# URL of the API endpoint
url = 'http://127.0.0.1:5000/linear_regression'

# Load your test data from the specified JSON file
with open(file_name, 'r') as file:
    json_data = json.load(file)

# Ensure the images directory exists
os.makedirs(images_directory, exist_ok=True)

# Send POST request to your API
response = requests.post(url, json=json_data)

# Check the status code of the response
if response.status_code == 200:
    # Process the successful response
    response_data = response.json()
    print(f"Slope: {response_data['slope']}\nIntercept: {response_data['intercept']}\nR-squared: {response_data['r_squared']}")

    # Convert the plot JSON to a Plotly figure and save the image
    fig = pio.from_json(response_data['plot'])
    image_path = os.path.join(images_directory, f"newplot_{size_input}.png")
    fig.write_image(image_path)
    print(f"Plot image saved to {image_path}")
    # Optionally, display the figure
    # fig.show()
else:
    # Handle unsuccessful response
    print(f"Failed with status code: {response.status_code}\n{response.text}")

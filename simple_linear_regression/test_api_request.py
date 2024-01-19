import requests
import json
import plotly.io as pio

# Ask the user for the size of the dataset they want to test
size_input = input("Enter the dataset size (small=50, medium=1000, large=10000): ").lower()
file_map = {
    'small': 'test_data_small.json',
    'medium': 'test_data_medium.json',
    'large': 'test_data_large.json'
}

# Check if the input is valid and get the corresponding filename
if size_input in file_map:
    file_name = file_map[size_input]
else:
    print("Invalid input. Please enter 'small', 'medium', or 'large'.")
    exit()

# URL of the API endpoint
url = 'http://127.0.0.1:5000/linear_regression'

# Load your test data from the specified JSON file
with open(file_name, 'r') as file:
    json_data = json.load(file)

# Send POST request to your API
response = requests.post(url, json=json_data)

# Check the status code of the response
if response.status_code == 200:
    # If response is successful, extract data
    response_data = response.json()

    # Print slope, intercept, and R-squared values
    print(f"Slope: {response_data['slope']}")
    print(f"Intercept: {response_data['intercept']}")
    print(f"R-squared: {response_data['r_squared']}")

    # Convert the plot JSON to a Plotly figure and display it
    fig = pio.from_json(response_data['plot'])
    fig.show()

else:
    # If response is not successful, print the status code and response text
    print(f"Failed with status code: {response.status_code}")
    print(response.text)

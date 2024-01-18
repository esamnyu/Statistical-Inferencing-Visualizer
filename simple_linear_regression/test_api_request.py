import requests
import json
import plotly.io as pio

# URL of the API endpoint
url = 'http://127.0.0.1:5000/linear_regression'

# Load your test data from the JSON file
with open('test_data.json', 'r') as file:
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

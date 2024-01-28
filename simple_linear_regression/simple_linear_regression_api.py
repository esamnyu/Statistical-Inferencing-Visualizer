import os
import sys
import json
from flask import Flask, request, jsonify
import pandas as pd
from plotly.utils import PlotlyJSONEncoder

# Ensure the root directory of your project is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importing custom modules from statlib
from statlib.linear_regression import LinearRegression
from statlib.visualization import plot_linear_regression

app = Flask(__name__)

@app.route('/linear_regression', methods=['POST'])
def linear_regression():
    # Load dataset from JSON input
    data = request.json
    df = pd.DataFrame(data)

    # Assuming the last column is the dependent variable
    X = df.iloc[:, :-1].values  # Convert to numpy array
    y = df.iloc[:, -1].values   # Convert to numpy array

    # Using custom LinearRegression class
    model = LinearRegression()
    model.fit(X, y)

    # Output
    slope = model.get_coefficients()[0]
    intercept = model.get_intercept()
    r_squared = model.score(X, y)

    # Plotting using custom visualization function
    fig = plot_linear_regression(X, y, model)

    # Convert the plotly figure to a JSON string using PlotlyJSONEncoder
    plot_json = json.dumps(fig, cls=PlotlyJSONEncoder)

    return jsonify({
        'slope': slope,
        'intercept': intercept,
        'r_squared': r_squared,
        'plot': plot_json
    })

if __name__ == '__main__':
    app.run(debug=True)

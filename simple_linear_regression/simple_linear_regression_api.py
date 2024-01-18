from flask import Flask, request, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression
import plotly.express as px
import json
import plotly

app = Flask(__name__)

@app.route('/linear_regression', methods=['POST'])
def linear_regression():
    # Load dataset from JSON input
    data = request.json
    df = pd.DataFrame(data)

    # Simple Linear Regression
    X = df.iloc[:, :-1]  # assuming the last column is the dependent variable
    y = df.iloc[:, -1]
    model = LinearRegression()
    model.fit(X, y)

    # Output
    slope = model.coef_[0]
    intercept = model.intercept_
    r_squared = model.score(X, y)

    # Plotting
    fig = px.scatter(df, x=df.columns[0], y=df.columns[1], trendline="ols")
    plot_json = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return jsonify({
        'slope': slope,
        'intercept': intercept,
        'r_squared': r_squared,
        'plot': plot_json
    })

if __name__ == '__main__':
    app.run(debug=True)

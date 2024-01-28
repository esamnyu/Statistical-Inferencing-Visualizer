import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objs as go

def plot_linear_regression(X, y, model):
    """
    Plots the data points and the linear regression line using Plotly.
    
    :param X: Features (independent variables)
    :param y: Target (dependent variable)
    :param model: Fitted linear regression model
    :return: Plotly figure object
    """
    # Scatter plot for the data points
    data_points = go.Scatter(
        x=X[:, 0], y=y,
        mode='markers',
        marker=dict(color='blue'),
        name='Data points'
    )
    
    # Line for the predictions
    line_x = np.linspace(X[:, 0].min(), X[:, 0].max(), 100)
    line_y = model.predict(line_x.reshape(-1, 1))
    regression_line = go.Scatter(
        x=line_x, y=line_y,
        mode='lines',
        line=dict(color='red'),
        name='Regression Line'
    )
    
    # Creating the figure
    fig = go.Figure(data=[data_points, regression_line])
    fig.update_layout(
        title='Linear Regression',
        xaxis_title='Feature',
        yaxis_title='Target',
        legend_title='Legend'
    )
    
    return fig

def plot_residuals(y_true, y_pred):
    """
    Plots the residuals of the regression model.
    :param y_true: True target values
    :param y_pred: Predicted target values
    """
    residuals = y_true - y_pred
    plt.figure(figsize=(8, 6))
    plt.scatter(y_pred, residuals, color='blue')
    plt.hlines(y=0, xmin=y_pred.min(), xmax=y_pred.max(), colors='red', linestyles='dashed')
    
    plt.xlabel('Predicted Values')
    plt.ylabel('Residuals')
    plt.title('Residuals vs Predicted')
    plt.show()

def plot_logistic_regression(X, y, model):
    """
    Plots the logistic regression decision boundary.
    :param X: Features (only two features are supported for 2D plot)
    :param y: Target
    :param model: Fitted logistic regression model
    """
    # Create a mesh to plot in
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(np.arange(x_min, x_max, 0.02), np.arange(y_min, y_max, 0.02))

    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)

    plt.figure(figsize=(8, 6))
    plt.contourf(xx, yy, Z, alpha=0.8)
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap=plt.cm.Paired)
    
    plt.xlabel('Feature 1')
    plt.ylabel('Feature 2')
    plt.title('Logistic Regression Decision Boundary')
    plt.show()

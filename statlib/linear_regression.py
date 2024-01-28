import numpy as np

class LinearRegression:
    def __init__(self):
        self.coefficients = None
        self.intercept = None

    def fit(self, X, y):
        """
        Fit the linear regression model to the training data.
        :param X: Training data features, numpy array or pandas DataFrame
        :param y: Training data target, numpy array or pandas Series
        """
        X = np.insert(X, 0, 1, axis=1)  # Adding a column of ones for intercept
        X_transpose = np.transpose(X)
        self.coefficients = np.linalg.inv(X_transpose.dot(X)).dot(X_transpose).dot(y)
        self.intercept = self.coefficients[0]
        self.coefficients = self.coefficients[1:]

    def predict(self, X):
        """
        Predict target values using the fitted model.
        :param X: Data to predict on
        :return: Predicted values
        """
        X = np.insert(X, 0, 1, axis=1)  # Add intercept term
        return X.dot(np.insert(self.coefficients, 0, self.intercept))

    def score(self, X, y):
        """
        Calculate the coefficient of determination R^2 of the prediction.
        :param X: Test data features
        :param y: Test data target
        :return: R^2 score
        """
        y_pred = self.predict(X)
        ss_total = np.sum((y - np.mean(y)) ** 2)
        ss_res = np.sum((y - y_pred) ** 2)
        r_squared = 1 - (ss_res / ss_total)
        return r_squared

    def get_coefficients(self):
        """
        Get the coefficients of the model.
        :return: Coefficients array
        """
        return self.coefficients

    def get_intercept(self):
        """
        Get the intercept of the model.
        :return: Intercept value
        """
        return self.intercept

import numpy as np

class LogisticRegression:
    def __init__(self, learning_rate=0.01, iterations=1000):
        self.learning_rate = learning_rate
        self.iterations = iterations
        self.weights = None
        self.bias = None

    def _sigmoid(self, z):
        """
        Private method to compute the sigmoid function.
        """
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        """
        Fit the logistic regression model to the training data.
        :param X: Training data features, numpy array
        :param y: Training data target, numpy array
        """
        n_samples, n_features = X.shape
        self.weights = np.zeros(n_features)
        self.bias = 0

        # Gradient Descent
        for _ in range(self.iterations):
            model = np.dot(X, self.weights) + self.bias
            predictions = self._sigmoid(model)

            # Compute gradients
            dw = (1 / n_samples) * np.dot(X.T, (predictions - y))
            db = (1 / n_samples) * np.sum(predictions - y)

            # Update parameters
            self.weights -= self.learning_rate * dw
            self.bias -= self.learning_rate * db

    def predict_proba(self, X):
        """
        Predict probability estimates for samples.
        :param X: Data to predict on
        :return: Probability estimates
        """
        linear_model = np.dot(X, self.weights) + self.bias
        return self._sigmoid(linear_model)

    def predict(self, X, threshold=0.5):
        """
        Predict class labels for samples in X.
        :param X: Data to predict on
        :param threshold: Threshold for converting predicted probabilities into class labels
        :return: Predicted class labels
        """
        probabilities = self.predict_proba(X)
        return [1 if i > threshold else 0 for i in probabilities]

    def score(self, X, y):
        """
        Calculate the accuracy of the model.
        :param X: Test data features
        :param y: Test data target
        :return: Accuracy score
        """
        predictions = self.predict(X)
        accuracy = np.sum(predictions == y) / len(y)
        return accuracy

# Statistical Inferencing APIs

## Overview
This project focuses on developing APIs for statistical inferencing methods, including linear regression, multiple linear regression, and logistic regression. These APIs are designed to handle datasets ranging from 50 to 10,000 observations and offer integration with visualization tools like Plotly.

---

### 1. Simple Linear Regression API

#### Purpose
- Enable users to perform simple linear regression on datasets ranging from 50 to 10,000 observations.

#### Problem Statement
- Provide an API to input a dataset and perform simple linear regression, calculating the linear relationship between two variables and providing regression coefficients.

#### Key Features
- **Input**: Dataset with one dependent and one independent variable.
- **Output**: Regression coefficients (slope, intercept), R-squared value.
- **Visualization**: Compatibility with Plotly for graphing the regression line.

#### Dataset Visualizations
Visualizations of datasets of different sizes used for Simple Linear Regression:

##### Small Dataset (50 observations)
![Small Dataset](images/new_plot_small.png)

##### Medium Dataset (1000 observations)
![Medium Dataset](images/new_plot_medium.png)

##### Large Dataset (10000 observations)
![Large Dataset](images/new_plot_large.png)

---

### 2. Multiple Linear Regression API

#### Purpose
- Facilitate users in performing multiple linear regression on datasets with various sizes.

#### Problem Statement
- Accept datasets with multiple independent variables for computing unique effects on a dependent variable. The API will also provide advanced statistical metrics such as the F-statistic, p-values, and R-squared values to assess the model's fit and significance.

#### Key Features
- **Input**: Dataset with one dependent and multiple independent variables.
- **Output**: 
  - Regression coefficients for each variable.
  - Overall model fit statistics including:
    - F-statistic: To assess the overall significance of the regression model.
    - p-values: For each coefficient to test the hypotheses about the relationship of each independent variable to the dependent variable.
    - R-squared value: To indicate the proportion of the variance in the dependent variable that is predictable from the independent variables.
- **Visualization**: Compatibility with visualization tools for multi-dimensional data representation and the ability to plot regression diagnostics.

---

## Additional Considerations
- **Ease of Use**: Focus on user-friendly interfaces and documentation.
- **Error Handling**: Graceful management of exceptions and errors.
- **Extensibility**: Design with potential future integration with more complex models (like neural networks) in mind.


---

### 3. Logistic Regression API

#### Purpose
- Interface for performing logistic regression, suitable for binary classification problems.

#### Problem Statement
- Allow users to perform logistic regression on datasets, including hyperparameter tuning and probability outputs for binary outcomes.

#### Key Features
- **Input**: Dataset with one dependent binary variable and multiple independent variables.
- **Output**: Predicted probabilities, classification threshold tuning, model accuracy.
- **Integration**: Capability with frameworks for visualizing categorical data outcomes.

---

## Additional Considerations
- **Ease of Use**: Focus on user-friendly interfaces and documentation.
- **Error Handling**: Graceful management of exceptions and errors.
- **Extensibility**: Design with potential future integration with more complex models (like neural networks) in mind.

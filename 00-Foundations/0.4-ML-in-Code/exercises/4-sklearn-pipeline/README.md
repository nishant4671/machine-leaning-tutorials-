# Exercise 4: Scikit-Learn Pipeline

## Question
Build a Pipeline with StandardScaler and LinearRegression. Train on the same data and compare coefficients.

## Detailed Explanation
In professional machine learning workflows, we rarely train models in isolation. We use **Pipelines** to bundle preprocessing steps and estimators together.

### Components:
1. **StandardScaler**: This transformer scales your data so that it has a mean of 0 and a standard deviation of 1. While not strictly necessary for simple linear regression with one feature, it is a best practice that helps gradient-based models converge faster.
2. **LinearRegression**: The standard OLS (Ordinary Least Squares) implementation in `scikit-learn`.

### Goals:
- Use `sklearn.pipeline.Pipeline` to chain these two steps.
- Use `fit()` to train the entire pipeline on your synthetic data.
- Extract the coefficients and intercept from the trained model.
- **Compare**: Check how these coefficients compare to the results from your manual Normal Equation (Ex 2) and Gradient Descent (Ex 3) implementations. Note that scaling might change the *scale* of the coefficients if not accounted for!

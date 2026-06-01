# Exercise 2: Closed-form Solution (Normal Equation)

## Question
Using numpy, compute the optimal slope and intercept via the normal equation. Compare to the true values.

## Detailed Explanation
Linear regression has an analytical solution that finds the parameters that minimize the Mean Squared Error (MSE) without needing an iterative optimization process. This is known as the **Normal Equation**:

$$\theta = (X^T X)^{-1} X^T y$$

Where:
- **$\theta$**: The vector of optimal parameters (intercept and slope).
- **$X$**: The feature matrix (usually including a column of ones for the intercept).
- **$y$**: The target vector.

### Key Concepts:
- **Bias Term**: You must augment your input data $x$ with a column of 1s to allow the model to calculate an intercept (bias).
- **Matrix Operations**: You will use `numpy` functions for transpose (`.T`), matrix multiplication (`@` or `np.dot`), and matrix inversion (`np.linalg.inv`).
- **Comparison**: After calculating the weights, compare them to the "true" values you used to generate the data in Exercise 1. Small differences are expected due to the noise ($\epsilon$).

This approach is efficient for small datasets but can become computationally expensive as the number of features increases.

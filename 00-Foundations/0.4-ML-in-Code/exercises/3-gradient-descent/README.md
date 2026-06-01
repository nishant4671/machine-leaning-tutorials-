# Exercise 3: Gradient Descent

## Question
Implement a simple gradient descent loop that updates weights. Track MSE over iterations.

## Detailed Explanation
Gradient Descent is an iterative optimization algorithm used to find the minimum of a cost function. In the context of linear regression, it is used to find the slope and intercept that minimize the Mean Squared Error (MSE).

### The Process:
1. **Initialize**: Start with random weights (slope and intercept).
2. **Calculate Loss**: Compute the Mean Squared Error for the current weights.
3. **Compute Gradients**: Find the partial derivatives of the MSE with respect to each weight. These tell you the "slope" of the error surface.
4. **Update Weights**: Subtract a portion of the gradient from the current weights:
   $$w = w - \eta \cdot \nabla L(w)$$
   Where $\eta$ is the **learning rate**.
5. **Repeat**: Iterate until the loss stabilizes (converges).

### What to Track:
- **Weight History**: How the slope and intercept change over time.
- **Loss History**: Store the MSE at each step. Plotting this "learning curve" helps verify that the algorithm is actually learning (the error should decrease).

This exercise builds intuition for how most modern machine learning and deep learning models are trained.

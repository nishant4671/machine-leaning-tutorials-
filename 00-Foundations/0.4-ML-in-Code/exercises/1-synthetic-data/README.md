# Exercise 1: Synthetic Data Generation

## Question
Generate 10 synthetic data points with a known linear relationship (e.g., y = 3x + 2 + noise). Plot them.

## Detailed Explanation
In this exercise, you will create a controlled dataset to simulate a real-world linear relationship. The goal is to generate a set of features ($x$) and corresponding targets ($y$) based on a linear formula:

$$y = mx + c + \epsilon$$

Where:
- **$m$ (slope)**: The coefficient of $x$ (e.g., 3).
- **$c$ (intercept)**: The value of $y$ when $x=0$ (e.g., 2).
- **$\epsilon$ (noise)**: Random variance added to make the data more realistic and less perfectly linear.

### Why this matters:
Generating synthetic data is a crucial skill for ML engineers. It allows you to:
1. Verify if your algorithm can correctly "recover" the known parameters ($m$ and $c$).
2. Test how your model behaves under different noise levels.
3. Visualize the data to understand the underlying distribution before applying complex models.

You should use `numpy` for data generation and `matplotlib` for plotting the results.

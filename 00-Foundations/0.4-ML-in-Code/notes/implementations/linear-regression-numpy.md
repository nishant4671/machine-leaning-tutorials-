# Linear Regression Using NumPy

## Purpose

Implement Linear Regression manually using NumPy.

The goal is to understand what sklearn automates.

---

## Core Equation

y = mx + b

Where:

- y = prediction
- x = input
- m = slope
- b = intercept

---

## Example

Dataset:

x = [1,2,3]

y = [3,5,7]

Expected relationship:

y = 2x + 1

---

## NumPy Implementation

```python
import numpy as np

x = np.array([1,2,3])

m = 2
b = 1

predictions = m * x + b

print(predictions)Output:

[3 5 7]

Why NumPy?

NumPy performs vectorized operations.

Instead of processing values one by one, it operates on entire arrays.

Common Mistakes
Using Python lists instead of NumPy arrays
Forgetting the intercept
Shape mismatch errors
Industry Notes

Understanding this implementation makes it easier to learn:

PyTorch
TensorFlow
JAX
Revision Summary

Linear Regression predicts:

y = mx + b

NumPy allows efficient vectorized computation.


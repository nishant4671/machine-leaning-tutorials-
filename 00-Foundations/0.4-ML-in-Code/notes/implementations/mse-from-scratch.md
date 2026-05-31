# MSE From Scratch

## Purpose

Understand how Mean Squared Error works.

MSE is one of the most common loss functions in Machine Learning.

---

## Formula

MSE = Mean((Actual - Predicted)^2)

---

## Example

Actual:

[3,5,7]

Predicted:

[2,5,8]

Errors:

[1,0,-1]

Squared Errors:

[1,0,1]

MSE:

(1 + 0 + 1) / 3

= 0.67

---

## NumPy Implementation

```python
import numpy as np

actual = np.array([3,5,7])
predicted = np.array([2,5,8])

errors = actual - predicted

squared_errors = errors ** 2

mse = np.mean(squared_errors)

print(mse)Why We Need MSE

Gradient Descent requires a score.

MSE provides that score.

Lower MSE means better predictions.

Common Mistakes
Forgetting to square errors
Averaging before squaring
Confusing MSE and RMSE
Future Connection

Neural Networks use loss functions exactly the same way.

Only the formula changes.

Revision Summary

MSE measures prediction quality.

Gradient Descent tries to minimize MSE.


# Gradient Descent Loop

## Purpose

Understand the structure of a Machine Learning training loop.

---

## Training Loop

Predict

?

Calculate Loss

?

Update Parameters

?

Repeat

---

## Skeleton

```python
for iteration in range(100):

    predictions = ...

    loss = ...

    update_parameters()
Example

Iteration 1

Loss = 27

Iteration 2

Loss = 15

Iteration 3

Loss = 6

Iteration 4

Loss = 2

The model is improving.

What Is Learning?

Learning = Parameter Updates

Nothing more.

Nothing less.

Common Mistakes
Learning rate too large
Learning rate too small
Not tracking loss
Future Connection

PyTorch training loops follow the exact same structure.

Revision Summary

Training = Repeated Error Correction.


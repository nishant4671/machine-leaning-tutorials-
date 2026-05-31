# Cross Validation Snippet

## Purpose

Evaluate model performance more reliably.

---

## Problem

One train-test split may be misleading.

A lucky split can make a bad model appear good.

---

## Solution

Cross Validation

Train multiple times using different splits.

Average the results.

---

## Example

```python
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LinearRegression

model = LinearRegression()

scores = cross_val_score(
    model,
    X,
    y,
    cv=5
)

print(scores)
What Happens?

Data is divided into folds.

Example:

Fold 1

Train on 80%

Test on 20%

Fold 2

Different 20% used for testing

Repeat

Average scores

Why It Matters

Provides a more reliable estimate of model quality.

Industry Usage

Commonly used when:

Comparing models
Tuning hyperparameters
Evaluating datasets
Revision Summary

Cross Validation = Multiple train-test evaluations averaged together.


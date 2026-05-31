# fit vs transform vs fit_transform

## Why This File Exists

One of the most common beginner confusions in sklearn.

---

## fit()

Purpose:

Learn from data.

Example:

```python
scaler.fit(X)

The scaler learns:

mean
standard deviation

No data changes yet.

transform()

Purpose:

Apply learned rules.

Example:

scaled_X = scaler.transform(X)

Data changes.

Scaler does not learn anything new.

fit_transform()

Purpose:

Learn and apply in one step.

Example:

scaled_X = scaler.fit_transform(X)

Equivalent to:

scaler.fit(X)

scaled_X = scaler.transform(X)
Mental Model

fit()

Study the data

transform()

Apply the learned rules

fit_transform()

Study + Apply

Common Mistakes

Mistake:

Using fit() on test data.

Correct:

Fit on training data.

Transform both training and test data.

Interview Question

Q:

What is the difference between fit() and transform()?

A:

fit() learns parameters.

transform() applies parameters.

Revision Summary

fit() = Learn

transform() = Apply

fit_transform() = Learn + Apply


# ML Debugging Log

## Purpose

This file records common mistakes, errors, and debugging patterns encountered while learning Machine Learning.

Future Me:

Before spending hours debugging, check this file.

---

# Section 1 - Conceptual Mistakes

## Mistake

Thinking training and inference are the same.

Reality:

Training:
Learn parameters.

Inference:
Use parameters.

---

## Mistake

Thinking lower loss means perfect predictions.

Reality:

Lower loss means better predictions.

Not necessarily perfect.

---

## Mistake

Thinking Gradient Descent is intelligence.

Reality:

Gradient Descent is optimization.

---

# Section 2 - NumPy Mistakes

## Problem

Using Python lists instead of NumPy arrays.

Wrong

x = [1,2,3]

Right

x = np.array([1,2,3])

---

## Problem

Shape mismatch.

Example

Expected:

(100,1)

Received:

(100,)

Solution:

Check:

X.shape

---

## Problem

Broadcasting confusion.

NumPy automatically expands dimensions.

Always verify shapes.

---

# Section 3 - sklearn Mistakes

## Problem

Forgetting model.fit()

Error:

Model not trained.

Solution:

Call fit() before predict().

---

## Problem

Using transform() before fit().

Wrong:

scaler.transform(X)

Right:

scaler.fit(X)

scaler.transform(X)

---

## Problem

Fitting scaler on test data.

Wrong:

scaler.fit(test_data)

Correct:

Fit on training data only.

Transform both datasets.

---

## Problem

Using different preprocessing during prediction.

Training:

Scaled

Prediction:

Not Scaled

Result:

Bad predictions.

---

# Section 4 - Pipeline Mistakes

## Problem

Scaling manually during training but forgetting during prediction.

Solution:

Use Pipeline.

---

## Problem

Saving model but not scaler.

Solution:

Save Pipeline instead.

---

# Section 5 - joblib Mistakes

## Problem

model.pkl not found.

Solution:

Check current working directory.

---

## Problem

Wrong file path.

Debug:

pwd

dir

---

## Problem

Loading incompatible files.

Solution:

Retrain model and regenerate .pkl.

---

# Section 6 - Learning Rate Problems

## Learning Rate Too Small

Symptoms:

Loss decreases very slowly.

Training takes forever.

---

## Learning Rate Too Large

Symptoms:

Loss oscillates.

Loss explodes.

Training unstable.

---

# Section 7 - Debugging Checklist

Before Panicking:

[ ] Is the model fitted?

[ ] Are shapes correct?

[ ] Is preprocessing applied?

[ ] Is model.pkl present?

[ ] Is prediction data scaled?

[ ] Are training and inference separated?

[ ] Is learning rate reasonable?

---

# Notes To Future Me

Whenever I encounter a new bug:

1. Record it here.
2. Explain the cause.
3. Explain the solution.
4. Include prevention tips.

This file should grow over time.


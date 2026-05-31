# Model Persistence

## Purpose

Save trained models for later use.

---

## Problem

Training may take:

- minutes
- hours
- days

Retraining every time is wasteful.

---

## Solution

Save the trained model.

---

## Using joblib

Save:

```python
import joblib

joblib.dump(model, "model.pkl")

Load:

model = joblib.load("model.pkl")
What Is Stored?

The trained model's learned parameters.

Examples:

coefficients
intercepts
learned weights
Why .pkl Files Exist

.pkl = Pickle File

A serialized Python object.

Think:

Save Brain

?

Load Brain

Industry Workflow

Train Model

?

Save model.pkl

?

Deploy API

?

Load model.pkl

?

Predict

Common Mistakes
Forgetting to save preprocessing objects
Loading incompatible model versions
Revision Summary

joblib allows trained models to be saved and loaded.


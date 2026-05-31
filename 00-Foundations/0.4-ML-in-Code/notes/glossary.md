# Glossary

## Feature

An input variable used by the model.

Example:
Hours Studied

---

## Target

The value the model tries to predict.

Example:
Exam Score

---

## Model

A mathematical function that maps inputs to outputs.

Example:
y = mx + b

---

## Prediction

The model's estimated output.

Often written as:

y_hat

---

## Error

Difference between actual and predicted values.

Error = Actual - Predicted

---

## Loss

A single number representing how wrong the model is.

Lower loss is better.

---

## MSE

Mean Squared Error.

Average of squared prediction errors.

---

## RMSE

Root Mean Squared Error.

Square root of MSE.

Often easier to interpret.

---

## Gradient

Direction of steepest increase in loss.

Gradient Descent moves in the opposite direction.

---

## Gradient Descent

Optimization algorithm used to reduce loss.

Core idea:

Predict
? Measure Error
? Update Parameters
? Repeat

---

## Learning Rate

Controls update size during training.

Small:
Slow Learning

Large:
Unstable Learning

---

## Iteration

One complete training update.

Predict
? Loss
? Update

---

## Training

Process of learning model parameters from data.

---

## Inference

Using a trained model to make predictions.

---

## StandardScaler

Transforms features to a common scale.

Improves optimization.

---

## Pipeline

A chain of preprocessing and modeling steps.

Example:

Scale Data
? Train Model
? Predict

---

## joblib

Python library used to save and load trained models.

---

## .pkl File

Serialized Python object.

Used to store trained models on disk.


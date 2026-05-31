# Training vs Inference

## One Of The Most Important Distinctions In ML

Every machine learning system has two phases:

1. Training
2. Inference

Many beginner confusions come from mixing these together.

---

## Training

Training means:

Learning from data.

Process:

Data
? Predictions
? Errors
? Loss
? Parameter Updates

Goal:

Learn useful parameters.

Examples:

- slope
- intercept
- weights

Training may take:

- seconds
- hours
- days
- weeks

depending on model size.

---

## Inference

Inference means:

Using a trained model to make predictions.

Example:

User enters:

House Size = 2000 sqft

Model predicts:

House Price = ?80,00,000

No learning occurs.

Only prediction.

---

## Real Industry Workflow

Train Once

?

Save Model

?

Load Model

?

Predict Thousands Of Times

---

## Why joblib Exists

Training can be expensive.

Instead of retraining:

Save model:

joblib.dump()

Later:

Load model:

joblib.load()

---

## Common Mistakes

Mistake:

Thinking prediction causes learning.

Reality:

Prediction and learning are separate phases.

---

## Future Connections

This distinction appears everywhere:

- FastAPI
- Docker
- MLOps
- LLM Deployment
- Production AI Systems

---

## Revision Summary

Training:

Learn Parameters

Inference:

Use Parameters

---

## Common Doubts

Q: Does the model learn during prediction?

A: Usually no.

Q: Why save models?

A: To avoid retraining.


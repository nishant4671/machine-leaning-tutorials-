# Pipeline = Assembly Line

## The Mental Picture

Imagine a car factory.

Raw metal enters.

Step 1:
Cutting

?

Step 2:
Painting

?

Step 3:
Assembly

?

Finished Car

---

## ML Translation

Raw Data

?

Scaling

?

Model

?

Prediction

---

## Why Pipelines Exist

Without a pipeline:

You must manually remember every step.

Example:

Scale Data

?

Train Model

?

Save Scaler

?

Scale New Data

?

Predict

Many opportunities for mistakes.

---

## With A Pipeline

The pipeline remembers everything.

You simply say:

pipeline.fit()

or

pipeline.predict()

---

## What Happens Internally?

pipeline.fit()

Automatically:

1. Fit Scaler
2. Scale Data
3. Train Model

---

pipeline.predict()

Automatically:

1. Scale New Data
2. Send To Model
3. Return Prediction

---

## Industry Usage

Pipelines are heavily used because:

- fewer bugs
- cleaner code
- reproducible workflows

---

## One-Sentence Memory

Pipeline = ML assembly line that automatically performs every step in order.


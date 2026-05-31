# Cost Function Landscape

## Purpose

A cost function tells us how bad a model currently is.

Lower cost means better predictions.

Higher cost means worse predictions.

---

## What Is A Cost Function?

A cost function converts:

Predictions

?

Errors

?

One Number

This number represents model quality.

---

## Example

Actual:

[3,5,7]

Predicted:

[2,5,8]

Errors:

[1,0,-1]

MSE:

0.67

The model's cost is 0.67.

---

## Landscape Analogy

Imagine every possible combination of:

m
b

as a location on a giant map.

Each location has a loss value.

---

## Mountain Interpretation

High Loss

= Mountain

Low Loss

= Valley

---

## Goal

Find:

Lowest Point

Lowest Loss

Best Parameters

---

## Why This Matters

Gradient Descent moves through this landscape.

Its goal is:

Reach the valley.

---

## Future Connection

Neural networks have millions of parameters.

The same landscape idea still applies.

The landscape simply becomes much larger.

---

## Common Doubts

Q: Is there always one valley?

A: No.

Large models may have many local minima.

---

## Revision Summary

Cost Landscape:

A map showing how loss changes as parameters change.


# Gradient Descent Update Rules

## Purpose

Gradient Descent updates model parameters to reduce loss.

---

## Core Idea

Current Parameters

?

Measure Loss

?

Compute Gradient

?

Update Parameters

?

Repeat

---

## Generic Update Rule

New Parameter

=

Old Parameter

-

Learning Rate × Gradient

---

## Meaning

Gradient:

Direction of increasing loss

Learning Rate:

Step size

Minus Sign:

Move downhill

---

## Linear Regression

Parameters:

m
b

Both are updated repeatedly.

---

## Learning Rate Effects

Too Small:

Slow learning

Too Large:

Unstable learning

Good:

Steady convergence

---

## Why Updates Work

If loss increases:

Move opposite the gradient.

If loss decreases:

Continue moving.

---

## Future Connection

Backpropagation in neural networks ultimately applies the same idea.

The update rule remains conceptually identical.

---

## Common Doubts

Q: Why subtract?

A: Because gradients point uphill.

We want to go downhill.

---

## Revision Summary

Update Rule:

Move opposite the gradient to reduce loss.


# Normal Equation Derivation

## Purpose

Linear Regression has a unique advantage.

We can directly compute the best parameters.

No iterative optimization required.

---

## Two Approaches

Approach 1:

Gradient Descent

Guess

?

Improve

?

Repeat

---

Approach 2:

Normal Equation

Compute answer directly.

---

## Mathematical Form

? = (X?X)^(-1)X?y

Do not memorize.

Understand the purpose.

---

## Intuition

Imagine solving:

2x + 1 = 5

You can calculate x directly.

No guessing required.

The Normal Equation works similarly.

---

## Why It Exists

Linear Regression has a closed-form solution.

Many other ML models do not.

---

## Advantages

- Exact solution
- No learning rate
- No iterations

---

## Disadvantages

- Expensive on large datasets
- Not suitable for deep learning

---

## Future Connection

Neural Networks:

No closed-form solution.

Must use Gradient Descent.

---

## Common Doubts

Q: Why don't we always use the Normal Equation?

A: It becomes computationally expensive as data grows.

---

## Revision Summary

Normal Equation:

Directly computes optimal Linear Regression parameters.


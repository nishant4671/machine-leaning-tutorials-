# StandardScaler = Converting Everything To Common Units

## The Mental Picture

Imagine comparing:

Height = centimeters

Salary = rupees

Age = years

These numbers live on completely different scales.

---

## Example

Age:

20
21
22

Salary:

2000000
2200000
2400000

---

## The Problem

Salary values are much larger.

The model may pay more attention to salary simply because the numbers are bigger.

---

## What StandardScaler Does

It transforms values into a common scale.

Age:

-1
0
1

Salary:

-1
0
1

Now both features are comparable.

---

## Real Analogy

Imagine comparing:

5 kilograms

5000 grams

They represent the same quantity.

Different units.

StandardScaler creates a common measurement system.

---

## Why Models Like This

Optimization becomes easier.

Gradient Descent often converges faster.

---

## Industry Usage

StandardScaler is commonly used with:

- Linear Regression
- Logistic Regression
- Neural Networks
- SVM

---

## One-Sentence Memory

StandardScaler puts different features onto a comparable scale.


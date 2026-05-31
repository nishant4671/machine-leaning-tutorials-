# Gradient Descent = Walking Down A Mountain

## The Mental Picture

Imagine standing on a mountain in thick fog.

You cannot see:

- the whole mountain
- the valley
- the best path

You only know:

Which direction slopes downward.

---

## What Do You Do?

Step 1:
Take a small step downhill.

Step 2:
Check your new position.

Step 3:
Take another small step.

Repeat.

Eventually:

You reach the valley.

---

## ML Translation

Mountain Height:
Loss

Position:
Current Parameters

Valley:
Minimum Loss

Walking:
Parameter Updates

---

## Learning Rate

Learning Rate controls step size.

Small Learning Rate:

Tiny careful steps.

Large Learning Rate:

Huge jumps.

---

## Why Large Learning Rates Fail

Imagine jumping 100 meters every step.

You keep overshooting the valley.

You may never stop near the minimum.

---

## Why Small Learning Rates Fail

Imagine taking 1-centimeter steps.

You eventually reach the valley.

But it takes forever.

---

## The Entire Story Of Gradient Descent

Start High

?

Move Downhill

?

Reduce Loss

?

Reach Better Parameters

---

## Future Connection

This same idea trains:

- Linear Regression
- Neural Networks
- CNNs
- Transformers
- LLMs

ChatGPT was trained using gradient-based optimization.

---

## One-Sentence Memory

Gradient Descent = Walking downhill until prediction error becomes small.


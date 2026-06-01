# Unit 0.4: ML in Code (from scratch to sklearn)

## 🎯 Learning Objectives
Implement linear regression manually, then using sklearn; save and load models; understand pipelines.

---

## 🧪 Exercises
1. **Generate 10 synthetic data points** with a known linear relationship (e.g., y = 3x + 2 + noise). Plot them.

2. **Closed‑form solution**: Using numpy, compute the optimal slope and intercept via the normal equation. Compare to the true values.

3. **Gradient descent**: Implement a simple gradient descent loop that updates weights. Track MSE over iterations.

4. **sklearn pipeline**: Build a Pipeline with StandardScaler and LinearRegression. Train on the same data and compare coefficients.

5. **Model persistence**: Use joblib to save the pipeline to disk, load it back in a new script, and make a prediction. Ensure the output matches.

6. **Write a test** (pytest) that checks the loaded model’s prediction is within a small tolerance of the original.

---

## ✅ Completion Checklist
*You have completed this unit when…*
I can explain what a gradient is and why we subtract it.
I can write a numpy linear regression from scratch without looking.
I can explain what StandardScaler does and when to use it.
I can save and load a trained model, and test that it works identically.

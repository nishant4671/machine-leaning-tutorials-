# Scikit-Learn Pitfalls ⚠️

1. **Data Leakage**: Fitting your scaler on the *entire* dataset instead of just the training set.
   *Fix*: Only call `.fit()` on training data.

2. **Scaling Categorical Data**: Trying to use `StandardScaler` on strings.
   *Fix*: Use `OneHotEncoder` or `LabelEncoder` for categories first.

3. **Wrong Metric**: Using 'Accuracy' for a dataset where 99% of samples are the same class.
   *Fix*: Use 'F1-score' or 'Precision/Recall'.

4. **Imbalanced Data**: Training on a dataset where one class is very rare.
   *Fix*: Use `class_weight='balanced'` in your model.

5. **Not Setting Random State**: Getting different results every time you run your code.
   *Fix*: Always set `random_state=42` (or any number).

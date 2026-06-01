# Scikit-Learn Common Patterns 💡

### 1. The Fit-Predict Cycle
The universal workflow for any model.
```python
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier()
model.fit(X_train, y_train)
predictions = model.predict(X_test)
```

### 2. Using Pipelines
Keep your preprocessing and modeling together.
```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
pipe = Pipeline([
    ('scaler', StandardScaler()),
    ('model', LogisticRegression())
])
pipe.fit(X_train, y_train)
```

### 3. Data Splitting
Always test on data the model hasn't seen.
```python
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
```

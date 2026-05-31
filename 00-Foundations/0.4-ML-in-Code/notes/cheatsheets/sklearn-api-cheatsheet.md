# sklearn API Cheatsheet

## Import Linear Regression

```python
from sklearn.linear_model import LinearRegression
Create Model
model = LinearRegression()
Train Model
model.fit(X, y)
Predict
prediction = model.predict(X_new)
StandardScaler
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
Scale Data
X_scaled = scaler.fit_transform(X)
Pipeline
from sklearn.pipeline import Pipeline
pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])
Train Pipeline
pipeline.fit(X, y)
Predict With Pipeline
pipeline.predict(X_new)
Save Model
import joblib

joblib.dump(model, "model.pkl")
Load Model
model = joblib.load("model.pkl")
Cross Validation
from sklearn.model_selection import cross_val_score
scores = cross_val_score(
    model,
    X,
    y,
    cv=5
)
Remember

fit()

Learn

transform()

Apply

fit_transform()

Learn + Apply


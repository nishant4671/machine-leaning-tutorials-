# Pipeline Template

## Purpose

Pipelines automate preprocessing and modeling steps.

They reduce bugs and make ML workflows reproducible.

---

## Mental Model

Pipeline = Assembly Line

Raw Data

?

Preprocessing

?

Model

?

Prediction

---

## Example

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

pipeline = Pipeline([
    ("scaler", StandardScaler()),
    ("model", LinearRegression())
])
What Happens During fit()

pipeline.fit(X, y)

Internally:

StandardScaler.fit()
StandardScaler.transform()
LinearRegression.fit()
What Happens During predict()

pipeline.predict(new_data)

Internally:

StandardScaler.transform()
LinearRegression.predict()
Why Use Pipelines?

Benefits:

Cleaner code
Fewer mistakes
Easier deployment
Reproducible workflows
Common Mistakes
Scaling training data manually but forgetting prediction data
Applying different preprocessing during inference
Industry Notes

Pipelines are considered best practice.

Revision Summary

Pipeline = Automatic sequence of ML steps.


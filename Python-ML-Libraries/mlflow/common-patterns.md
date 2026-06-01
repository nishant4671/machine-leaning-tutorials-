# MLflow Common Patterns 💡

### 1. Automatic Logging
Many libraries can log everything automatically with one line!
```python
import mlflow
mlflow.autolog() # Works for sklearn, pytorch, etc.
# Now just train your model...
```

### 2. The Context Manager Pattern
Ensuring runs are closed properly even if code crashes.
```python
with mlflow.start_run():
    mlflow.log_param("alpha", 0.5)
    # ... training code ...
    mlflow.log_metric("rmse", 0.8)
```

### 3. Comparing Runs
Use the UI to select multiple runs and see a comparison chart of parameters vs metrics.

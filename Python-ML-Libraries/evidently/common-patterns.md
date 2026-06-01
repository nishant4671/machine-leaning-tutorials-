# Evidently Common Patterns 💡

### 1. Comparing Reference vs. Current
The most common way to check if data has changed since you trained the model.
```python
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset
report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=train_df, current_data=production_df)
report.save_html("drift_report.html")
```

### 2. Column Mapping
Telling Evidently which columns are features and which is the target.
```python
from evidently.utils import ColumnMapping
mapping = ColumnMapping()
mapping.target = 'price'
mapping.numerical_features = ['sqft', 'age']
# Now run report with this mapping...
```

### 3. Automated Monitoring
Integrating into a CI/CD pipeline or a scheduled job to alert if tests fail.

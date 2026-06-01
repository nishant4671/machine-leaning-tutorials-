import pandas as pd
from sklearn import datasets
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, DataQualityPreset

# 1. Prepare data (Reference vs Current)
iris = datasets.load_iris(as_frame=True)
iris_frame = iris.frame

reference = iris_frame.sample(n=75, random_state=42)
current = iris_frame.sample(n=75, random_state=1)

# 2. Setup and Run Report
report = Report(metrics=[
    DataDriftPreset(), 
    DataQualityPreset()
])

report.run(reference_data=reference, current_data=current)

# 3. Save
report.save_html("iris_drift_report.html")
print("Report 'iris_drift_report.html' created! Open it in your browser.")

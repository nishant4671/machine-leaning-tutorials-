# Pandas Common Patterns 💡

### 1. The Clean-Filter-Analyze Workflow
The bread and butter of data science.
```python
import pandas as pd
df = pd.read_csv('data.csv')
# Clean: fill missing, Filter: Age > 18, Analyze: Mean salary
result = df.fillna(0)[df['Age'] > 18]['Salary'].mean()
```

### 2. Grouping and Aggregating
Summarizing data by categories.
```python
import pandas as pd
# Group by Category and get sum of Sales
summary = df.groupby('Category')['Sales'].sum()
```

### 3. Creating New Features
Adding logic based on existing columns.
```python
import pandas as pd
# Add a flag for high spenders
df['IsHighSpender'] = df['TotalSpent'] > 1000
```

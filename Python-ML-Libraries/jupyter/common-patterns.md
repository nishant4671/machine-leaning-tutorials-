# Jupyter Common Patterns 💡

### 1. Exploratory Data Analysis (EDA)
The classic flow of data work.
```python
# Cell 1: Imports
import pandas as pd
# Cell 2: Load
df = pd.read_csv('data.csv')
# Cell 3: View
df.head()
```

### 2. Interactive Plotting
Seeing your charts right in the notebook.
```python
%matplotlib inline
import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
```

### 3. Using Shell Commands
Installing libraries or checking files without leaving the notebook.
```python
!pip install requests
!ls -lh
```

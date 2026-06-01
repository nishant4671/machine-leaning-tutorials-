# NumPy Common Patterns 💡

### 1. Vectorized Operations
Stop using loops! Let NumPy handle the math across the whole array.
```python
import numpy as np
prices = np.array([10, 20, 30])
# Add 5% tax to all prices instantly
taxed_prices = prices * 1.05
print(taxed_prices)
```

### 2. Boolean Masking
Filtering data is super easy and readable.
```python
import numpy as np
scores = np.array([85, 42, 90, 55, 78])
# Find all scores above passing (60)
passing_scores = scores[scores >= 60]
print(passing_scores)
```

### 3. Reshaping for ML Models
Many ML libraries expect data in a specific shape (like a column vector).
```python
import numpy as np
data = np.arange(1, 7) # [1, 2, 3, 4, 5, 6]
# Reshape to 3 rows, 2 columns
matrix = data.reshape(3, 2)
print(matrix)
```

# Seaborn Common Patterns 💡

### 1. The "Hue" Pattern
Adding a third dimension to a 2D plot using color.
```python
import seaborn as sns
# Separate data by category 'Species' automatically
sns.scatterplot(data=df, x='Weight', y='Height', hue='Species')
```

### 2. Exploring Correlation
Quickly seeing how all variables relate.
```python
import seaborn as sns
# Plot a correlation matrix
sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
```

### 3. Distribution Comparison
Seeing how different groups behave.
```python
import seaborn as sns
sns.kdeplot(data=df, x='Score', hue='Class', fill=True)
```

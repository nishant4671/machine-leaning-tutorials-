# Seaborn Syntax Cheatsheet 📝

| Signature | Description | Tiny Example |
| :--- | :--- | :--- |
| `sns.set_theme()` | Set the default style | `sns.set_theme()` |
| `sns.lineplot(df, x, y)` | Line plot with intervals | `sns.lineplot(data=df, x='X', y='Y')` |
| `sns.scatterplot(df, x, y)` | Scatter plot with 'hue' | `sns.scatterplot(data=df, x='A', y='B', hue='C')` |
| `sns.barplot(df, x, y)` | Bar chart with mean/error | `sns.barplot(data=df, x='Day', y='Total')` |
| `sns.histplot(data)` | Histogram with KDE option | `sns.histplot(x=val, kde=True)` |
| `sns.boxplot(df, x, y)` | Box and whisker plot | `sns.boxplot(data=df, y='Salary')` |
| `sns.heatmap(data)` | Visualize a matrix | `sns.heatmap(corr_matrix)` |
| `sns.pairplot(df)` | Plot all pairwise relations | `sns.pairplot(df)` |
| `sns.jointplot(df, x, y)` | Plot 2 vars with marginals | `sns.jointplot(data=df, x='X', y='Y')` |
| `sns.violinplot(df, x, y)` | Combo of boxplot and KDE | `sns.violinplot(data=df, x='Grp', y='Val')` |

# Seaborn Pitfalls ⚠️

1. **Misinterpreting Error Bars**: By default, Seaborn shows 95% confidence intervals, not standard deviation.
   *Fix*: Use `errorbar='sd'` if you want standard deviation.

2. **Passing NumPy instead of Pandas**: It works, but you lose the automatic labels.
   *Fix*: Wrap your data in a DataFrame first.

3. **Slow Pairplots**: Running `sns.pairplot()` on a dataset with 50 columns will crash your session.
   *Fix*: Select a few columns first: `sns.pairplot(df[['A', 'B', 'C']])`.

4. **Overlapping Labels**: Long category names on the X axis.
   *Fix*: Rotate them using Matplotlib: `plt.xticks(rotation=45)`.

5. **Confusing `displot` vs `histplot`**: `displot` is a "figure-level" function, which behaves differently than "axes-level" functions.
   *Fix*: Use `histplot` for simple plots, `displot` for complex grids.

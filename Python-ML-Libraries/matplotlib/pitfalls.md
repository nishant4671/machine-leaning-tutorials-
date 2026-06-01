# Matplotlib Pitfalls ⚠️

1. **Forgetting `plt.show()`**: Your code runs, but no window appears!
   *Fix*: Always end your script with `plt.show()`.

2. **Overlap in Subplots**: Titles and labels crashing into each other.
   *Fix*: Use `plt.tight_layout()`.

3. **Not Clearing Figures**: Plotting in a loop might draw everything on the same chart.
   *Fix*: Use `plt.clf()` or `plt.close()` inside the loop.

4. **Confusing Figure vs Axes**: Trying to call `ax.title()` (wrong) instead of `ax.set_title()` (right).
   *Fix*: Remember OO interface uses `set_` prefix for many properties.

5. **Heavy Plots**: Plotting millions of points can freeze your computer.
   *Fix*: Sample your data first or use `alpha` for transparency.

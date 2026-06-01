# Jupyter Pitfalls ⚠️

1. **Out-of-Order Execution**: Running Cell 5, then changing Cell 2, but not rerunning 3 and 4. This leads to "impossible" bugs!
   *Fix*: Use "Kernel -> Restart & Run All" frequently.

2. **Hidden State**: Deleting a cell doesn't delete the variables it created.
   *Fix*: Restart the kernel to clear memory.

3. **Notebooks as Production Code**: Notebooks are for research. They are hard to test and version control.
   *Fix*: Move stable code to `.py` files.

4. **Huge Outputs**: Printing 1 million rows can freeze your browser.
   *Fix*: Use `df.head()` or `print(len(data))`.

5. **Version Control Mess**: Git has a hard time with notebook files because they contain metadata and images.
   *Fix*: Use `nbstripout` or similar tools before committing.

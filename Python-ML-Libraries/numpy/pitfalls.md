# NumPy Pitfalls ⚠️

1. **Mixed Data Types**: NumPy arrays expect everything to be the same type. If you mix strings and numbers, it might turn everything into strings!
   *Fix*: Always check `arr.dtype`.

2. **Off-by-one in Slicing**: Like Python lists, `arr[0:5]` includes index 0 but *excludes* index 5.
   *Fix*: Remember: `[start : stop_at_but_dont_include]`.

3. **Shape Mismatches**: Trying to add a (3,2) array to a (2,3) array will crash.
   *Fix*: Use `arr.shape` to debug before operations.

4. **In-place vs Copies**: `b = a` doesn't copy the data; it just points to it. Changing `b` changes `a`.
   *Fix*: Use `b = a.copy()`.

5. **Integer Division**: In older versions or specific types, `5/2` might give `2` instead of `2.5`.
   *Fix*: Use `arr.astype(float)` if you need decimals.

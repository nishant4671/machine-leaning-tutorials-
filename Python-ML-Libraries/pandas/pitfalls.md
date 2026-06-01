# Pandas Pitfalls ⚠️

1. **SettingWithCopyWarning**: Trying to modify a slice of a dataframe instead of the original.
   *Fix*: Use `.loc[row_indexer, col_indexer] = value`.

2. **Iterating with Loops**: Using `for index, row in df.iterrows()` is very slow.
   *Fix*: Use vectorized operations or `.apply()`.

3. **In-place Operations**: Many functions return a *new* dataframe unless you set `inplace=True`.
   *Fix*: Prefer `df = df.dropna()` over `df.dropna(inplace=True)`.

4. **Mixed Types in Columns**: One string in a column of numbers can turn the whole column into 'object' type.
   *Fix*: Use `df['col'] = pd.to_numeric(df['col'], errors='coerce')`.

5. **Chain Indexing**: `df['col'][0]` can be unreliable for assignment.
   *Fix*: Use `df.at[0, 'col']` or `df.iat[0, 0]`.

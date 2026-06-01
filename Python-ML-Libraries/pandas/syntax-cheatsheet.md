# Pandas Syntax Cheatsheet 📝

| Signature | Description | Tiny Example |
| :--- | :--- | :--- |
| `pd.read_csv('file.csv')` | Load data from a CSV | `df = pd.read_csv('data.csv')` |
| `df.head(n)` | View the first `n` rows | `df.head(5)` |
| `df.info()` | Summary of the DataFrame | `df.info()` |
| `df.describe()` | Statistical summary | `df.describe()` |
| `df['col']` | Select a single column | `df['Age']` |
| `df[['c1', 'c2']]` | Select multiple columns | `df[['Name', 'Age']]` |
| `df.loc[row, col]` | Access by label | `df.loc[0, 'Name']` |
| `df.iloc[row, col]` | Access by integer position | `df.iloc[0, 1]` |
| `df[df['Age'] > 20]` | Filter rows by condition | `df[df['Age'] > 21]` |
| `df.fillna(val)` | Replace missing values | `df.fillna(0)` |
| `df.groupby('col')` | Group data for aggregation | `df.groupby('City').mean()` |
| `df.sort_values('col')` | Sort data by a column | `df.sort_values('Price')` |
| `df.drop('col', axis=1)` | Remove a column | `df.drop('ID', axis=1)` |
| `df.apply(func)` | Apply a function to data | `df['Age'].apply(lambda x: x+1)` |
| `df.to_csv('out.csv')` | Save data to CSV | `df.to_csv('clean.csv')` |

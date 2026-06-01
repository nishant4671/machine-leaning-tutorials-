import pandas as pd
import numpy as np

# 1. Create dummy data
data = {
    'Name': ['Alice', 'Bob', 'Charlie', np.nan],
    'Age': [25, 30, np.nan, 22],
    'City': ['NY', 'LA', 'NY', 'SF']
}
df = pd.DataFrame(data)

# 2. Basic Cleaning
df['Name'] = df['Name'].fillna('Unknown')
df['Age'] = df['Age'].fillna(df['Age'].mean())

# 3. Simple Analysis
city_counts = df['City'].value_counts()
avg_age = df['Age'].mean()

print("Cleaned DataFrame:")
print(df)
print(f"\nAverage Age: {avg_age:.1f}")

import numpy as np

# 1. Create a synthetic dataset (100 samples, 3 features)
data = np.random.rand(100, 3)

# 2. Basic statistics
mean_vals = data.mean(axis=0)
std_vals = data.std(axis=0)

# 3. Normalization (Z-score)
normalized_data = (data - mean_vals) / std_vals

# 4. Filter: Find rows where first feature is > 0.5
high_feature_1 = data[data[:, 0] > 0.5]

print(f"Original shape: {data.shape}")
print(f"Mean per feature: {mean_vals}")
print(f"Rows with feature1 > 0.5: {len(high_feature_1)}")

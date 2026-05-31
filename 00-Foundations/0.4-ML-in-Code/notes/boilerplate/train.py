"""
train.py

Train a simple Linear Regression model
and save it using joblib.
"""

from sklearn.linear_model import LinearRegression
import joblib

# Training Data
X = [[1], [2], [3], [4]]
y = [3, 5, 7, 9]

# Train Model
model = LinearRegression()
model.fit(X, y)

# Save Model
joblib.dump(model, "model.pkl")

print("Model trained and saved.")

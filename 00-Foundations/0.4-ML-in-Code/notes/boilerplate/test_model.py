"""
test_model.py

Basic sanity checks.
"""

import joblib

model = joblib.load("model.pkl")

prediction = model.predict([[5]])

assert prediction[0] > 0

print("Test Passed")

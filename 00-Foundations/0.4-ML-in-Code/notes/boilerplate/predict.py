"""
predict.py

Load a trained model
and make predictions.
"""

import joblib

# Load Model
model = joblib.load("model.pkl")

# Predict
prediction = model.predict([[5]])

print("Prediction:", prediction[0])

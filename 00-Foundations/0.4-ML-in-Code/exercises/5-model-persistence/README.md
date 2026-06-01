# Exercise 5: Model Persistence

## Question
Use joblib to save the pipeline to disk, load it back in a new script, and make a prediction. Ensure the output matches.

## Detailed Explanation
In a real-world scenario, you don't want to retrain your model every time you need a prediction. **Model Persistence** allows you to save a trained model to a file and load it later.

### Steps:
1. **Save**: Use the `joblib` library to serialize the entire `Pipeline` object from Exercise 4 into a file (e.g., `model.joblib`).
2. **Load**: In a separate script or logical block, load that file back into a new variable.
3. **Predict**: Use the loaded model to predict the output for a new input value.
4. **Validation**: Verify that the prediction from the loaded model is *identical* to the prediction from the original model in memory.

### Why Joblib?
While Python has a built-in `pickle` module, `joblib` is optimized for objects that contain large `numpy` arrays, which is very common in scikit-learn models.

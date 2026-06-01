import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestRegressor

# 1. Set the experiment name
mlflow.set_experiment("Simple_Regression_Project")

# 2. Start tracking a run
with mlflow.start_run(run_name="First_Attempt"):
    # Log hyperparameters
    n_estimators = 100
    mlflow.log_param("n_estimators", n_estimators)
    
    # Train model
    model = RandomForestRegressor(n_estimators=n_estimators)
    # ... imagine model.fit(X, y) here ...
    
    # Log a dummy metric
    mlflow.log_metric("mse", 0.45)
    
    # Save the model
    mlflow.sklearn.log_model(model, "random_forest_model")

print("Run logged! Type 'mlflow ui' in your terminal to see the results.")

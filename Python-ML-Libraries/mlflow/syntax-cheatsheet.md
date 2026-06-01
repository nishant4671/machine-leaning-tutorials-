# MLflow Syntax Cheatsheet 📝

| Signature | Description | Tiny Example |
| :--- | :--- | :--- |
| `mlflow.set_experiment(n)`| Organize runs into a group | `mlflow.set_experiment('Proj1')` |
| `mlflow.start_run()` | Start a new tracking session | `with mlflow.start_run():` |
| `mlflow.log_param(k, v)` | Log a single hyperparameter | `mlflow.log_param('lr', 0.1)` |
| `mlflow.log_metric(k, v)` | Log a numerical result | `mlflow.log_metric('acc', 0.9)` |
| `mlflow.log_artifact(p)` | Save a file (plot, model) | `mlflow.log_artifact('h.png')` |
| `mlflow.sklearn.log_model()`| Log a Scikit-Learn model | `mlflow.sklearn.log_model(m, 'mod')` |
| `mlflow ui` (CLI) | Open the visual dashboard | `mlflow ui` |

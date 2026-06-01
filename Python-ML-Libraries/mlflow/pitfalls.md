# MLflow Pitfalls ⚠️

1. **Forgotten `mlflow ui`**: Beginners often log data but don't know where it went.
   *Fix*: Run `mlflow ui` in your terminal and open `localhost:5000`.

2. **Messy Runs**: Putting all your tests in the "Default" experiment.
   *Fix*: Use `mlflow.set_experiment("My_Awesome_Model")`.

3. **Logging Absolute Paths**: Artifacts might not open if you move folders.
   *Fix*: Use relative paths for artifacts.

4. **Not Logging Code Version**: Hard to replicate a run if you've changed the code since.
   *Fix*: MLflow automatically tracks Git hashes if you're in a repo!

5. **Inconsistent Naming**: Naming parameters `lr` in one run and `learning_rate` in another.
   *Fix*: Stick to a standard naming convention.

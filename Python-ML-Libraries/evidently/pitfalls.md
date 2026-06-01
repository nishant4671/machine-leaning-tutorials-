# Evidently Pitfalls ⚠️

1. **Small Sample Sizes**: Drift detection is statistical. If you only compare 5 rows, you'll get false alarms.
   *Fix*: Ensure both reference and current datasets have enough samples.

2. **Mixed Data Types**: If a column was an int in training but a float in production, Evidently might get confused.
   *Fix*: Use `ColumnMapping` to explicitly define types.

3. **Forgetting the Reference**: You can't detect drift if you don't have the "gold standard" data you trained on.
   *Fix*: Save a sample of your training data as a `reference.csv`.

4. **Ignoring Target Drift**: Sometimes the input data is fine, but the *relationship* with the target has changed.
   *Fix*: Include `TargetDriftPreset` in your reports.

5. **Report Overload**: Generating a 50MB HTML report every 10 minutes.
   *Fix*: Use `TestSuites` for automated checks and only generate full Reports when something fails.

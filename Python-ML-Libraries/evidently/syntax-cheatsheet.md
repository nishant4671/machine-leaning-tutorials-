# Evidently Syntax Cheatsheet 📝

| Signature | Description | Tiny Example |
| :--- | :--- | :--- |
| `Report(metrics=[...])` | Create a report object | `report = Report(metrics=[DataDriftPreset()])` |
| `report.run(ref, cur)` | Calculate the report | `report.run(reference_df, current_df)` |
| `report.save_html(p)` | Export report as HTML | `report.save_html('report.html')` |
| `DataDriftPreset()` | Preset for checking drift | `[DataDriftPreset()]` |
| `TestSuite(tests=[...])` | Create automated tests | `TestSuite(tests=[TestNumberOfRows()])` |

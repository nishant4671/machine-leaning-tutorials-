# Scikit-Learn Syntax Cheatsheet 📝

| Signature | Description | Tiny Example |
| :--- | :--- | :--- |
| `train_test_split(X, y)` | Split data for testing | `X_train, X_test, ...` |
| `model.fit(X, y)` | Train the model | `model.fit(X_train, y_train)` |
| `model.predict(X)` | Make predictions | `preds = model.predict(X_test)` |
| `StandardScaler()` | Normalize data (mean=0, std=1) | `scaler.fit_transform(X)` |
| `LinearRegression()` | Linear model for regression | `lr = LinearRegression()` |
| `RandomForestClassifier()` | Ensemble of trees | `rf = RandomForestClassifier()` |
| `KMeans(n_clusters=k)` | Unsupervised clustering | `kmeans.fit(data)` |
| `mean_squared_error(y, p)`| Evaluation for regression | `mse(y_true, y_pred)` |
| `accuracy_score(y, p)` | Evaluation for classification | `accuracy_score(y, p)` |
| `Pipeline(steps)` | Chain multiple steps | `Pipeline([('s', scaler), ('m', model)])` |
| `GridSearchCV(model, params)`| Find best hyperparameters | `grid.fit(X, y)` |
| `confusion_matrix(y, p)` | Detailed classification view | `confusion_matrix(y, p)` |

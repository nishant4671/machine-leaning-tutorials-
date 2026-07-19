# Learning Log

This log is the source of truth for tracking progress across CLI sessions. At the beginning of each session, review this log to resume work. At the end of each session, document the progress and outline the next steps.

---

## 📅 Log Entries

### [2026-07-03] - Session Startup
- **Status:** Starting Module 0 (Absolute Foundations)
- **Current Focus:** Module 0.1 (What is ML)
- **Accomplished Today:** 
  - Restructured the workspace and analyzed existing curriculum resources.
  - Setup the automated learning-log system.
- **Next Steps:** 
  - Decide which sub-unit of Module 0 to study today (e.g. 0.1, 0.2, etc.).
  - Review the theory resources and complete the corresponding exercises.

### [2026-07-10] - Warmup Completed & Production Roadmapping
- **Status:** Transitioning to Module 1 (Tabular ML & Production Delivery)
- **Current Focus:** Elevating housing predictor API to production standards
- **Accomplished Today:**
  - Reviewed the housing project warmup (Flask + LinearRegression + joblib + my_learnings notes).
  - Identified the missing `model.fit(X, y)` training bug.
  - Aligned on the next steps to reach production standards.
  - Updated the active state in `session-state.md`.
- **Next Steps:**
  - Fix the training script bug and build the scikit-learn Pipeline with scaling and hyperparameter tuning.
  - Rewrite the API in FastAPI with Pydantic validation.

### [2026-07-17] - sklearn Production Training Pipeline Refactored
- **Status:** Module 1: Tabular ML (In Progress)
- **Current Focus:** Upgrading train_model.py and transitioning Flask to FastAPI
- **Accomplished Today:**
  - Refactored `01-Tabular-ML/housing_project/train_model.py` to use a 3-step scikit-learn Pipeline: StandardScaler, PolynomialFeatures (degree=2, include_bias=False), and Ridge regression.
  - Set up `GridSearchCV` with 5-fold cross-validation (`cv=5`) to search across Ridge alpha parameters ([0.1, 1.0, 10.0, 100.0]).
  - Extracted the best-performing pipeline and saved it to `house_model.joblib`.
  - Confirmed the model trains and saves successfully.
- **Next Steps:**
  - Refactor `01-Tabular-ML/housing_project/app.py` from Flask to a production-ready FastAPI app with Pydantic validation schemas. (Paused)

### [2026-07-19] - Pivoting to NLP & MLOps
- **Status:** Module 2: NLP & MLOps Fundamentals
- **Current Focus:** Module 2 Overview & Pre-Flight
- **Accomplished Today:**
  - Shifted focus to `02-NLP-MLOps` directory.
- **Next Steps:**
  - Start exploring the Pre-Flight-Study material.
  - Review MLOps best practices (MLflow, DVC, data drift) for the Spam Classifier Project.

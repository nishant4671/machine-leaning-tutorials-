# 📍 Session State

This file tracks the active state of your learning journey. The AI assistant will read this file at the start of every session to automatically resume from where you left off.

---

## 🏃 Current State
- **Active Module:** [Module 1: Tabular ML & Production Delivery](file:///C:/Users/HP/OneDrive/Desktop/ML-Engineer-Learning/01-Tabular-ML/README.md)
- **Active Unit:** [Project: House Price Predictor API](file:///C:/Users/HP/OneDrive/Desktop/ML-Engineer-Learning/01-Tabular-ML/housing_project/)
- **Last Completed Task:** Completed educational warmup prototype (Flask API + basic training script + detailed learning notes under `my_learnings/`).
- **Current Objective:** Upgrade the prototype to Production-Ready Standards.
- **Next Action:** Refactor [train_model.py](file:///C:/Users/HP/OneDrive/Desktop/ML-Engineer-Learning/01-Tabular-ML/housing_project/train_model.py) to add the missing `model.fit(X, y)` step and transition it to a robust scikit-learn Pipeline (using scaling, polynomial features, and Ridge regression with hyperparameter tuning via `GridSearchCV`).

---

## 📋 Session Log
| Date | Session Action | Status | Notes |
| :--- | :--- | :--- | :--- |
| **2026-07-03** | Initialized learning-log | Completed | Established basic workspace tracking. |
| **2026-07-07** | Created `session-state.md` & Recapped progress | Completed | Resumed session, confirmed completion of Unit 0.4 Exercise 1. |
| **2026-07-10** | Documented warmup completion & mapped next steps | Completed | Reviewed housing project. Identified missing fit step and laid out production standards comparison (FastAPI, Docker, Testing, Pipeline). |

---

## 🛠️ How to Resume
1. Open [train_model.py](file:///C:/Users/HP/OneDrive/Desktop/ML-Engineer-Learning/01-Tabular-ML/housing_project/train_model.py).
2. Fix the missing training step by implementing a robust scikit-learn Pipeline (`StandardScaler` + `PolynomialFeatures` + `Ridge` regression) and tuning it using `GridSearchCV`.
3. Save the best pipeline model and scaler using `joblib.dump()`.
4. Transition the Flask app in [app.py](file:///C:/Users/HP/OneDrive/Desktop/ML-Engineer-Learning/01-Tabular-ML/housing_project/app.py) to FastAPI with Pydantic validation.

# 📍 Session State

This file tracks the active state of your learning journey. The AI assistant will read this file at the start of every session to automatically resume from where you left off.

---

## 🏃 Current State
- **Active Module:** [Module 1: Tabular ML & Production Delivery](file:///C:/Users/HP/OneDrive/Desktop/ML-Engineer-Learning/01-Tabular-ML/README.md)
- **Active Unit:** [Project: House Price Predictor API](file:///C:/Users/HP/OneDrive/Desktop/ML-Engineer-Learning/01-Tabular-ML/housing_project/)
- **Last Completed Task:** Refactored [train_model.py](file:///C:/Users/HP/OneDrive/Desktop/ML-Engineer-Learning/01-Tabular-ML/housing_project/train_model.py) to implement a robust sklearn Pipeline (StandardScaler -> PolynomialFeatures -> Ridge) with GridSearchCV tuning for alpha, and saved the best estimator.
- **Current Objective:** Upgrade the Flask API to a Production-Ready FastAPI server.
- **Next Action:** Transition [app.py](file:///C:/Users/HP/OneDrive/Desktop/ML-Engineer-Learning/01-Tabular-ML/housing_project/app.py) from Flask to FastAPI, implementing `/predict` (single) and `/batch-predict` (batch) endpoints with Pydantic request body validation schemas.

---

## 📋 Session Log
| Date | Session Action | Status | Notes |
| :--- | :--- | :--- | :--- |
| **2026-07-03** | Initialized learning-log | Completed | Established basic workspace tracking. |
| **2026-07-07** | Created `session-state.md` & Recapped progress | Completed | Resumed session, confirmed completion of Unit 0.4 Exercise 1. |
| **2026-07-10** | Documented warmup completion & mapped next steps | Completed | Reviewed housing project. Identified missing fit step and laid out production standards comparison (FastAPI, Docker, Testing, Pipeline). |
| **2026-07-17** | Completed sklearn training pipeline with GridSearchCV | Completed | Refactored `train_model.py` to use StandardScaler + Poly(degree=2) + Ridge, automated hyperparameter tuning, and saved the best pipeline model to `house_model.joblib`. |

---

## 🛠️ How to Resume
1. Open [app.py](file:///C:/Users/HP/OneDrive/Desktop/ML-Engineer-Learning/01-Tabular-ML/housing_project/app.py).
2. Refactor it to import `fastapi`, `pydantic`, and `uvicorn`.
3. Create a Pydantic schema for the California housing features (8 input columns).
4. Implement `/predict` and `/batch-predict` endpoints.
5. Launch the server using Uvicorn.


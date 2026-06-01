# FastAPI Common Patterns 💡

### 1. The ML Prediction Endpoint
The standard way to serve a model.
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class InputData(BaseModel):
    feature1: float
    feature2: float

@app.post("/predict")
def predict(data: InputData):
    # prediction = model.predict([[data.feature1, data.feature2]])
    return {"prediction": 42.0}
```

### 2. Automatic Docs
Just go to `http://localhost:8000/docs` while your app is running to see the interactive Swagger UI.

### 3. Startup and Shutdown Events
Loading your model into memory when the server starts.
```python
@app.on_event("startup")
def load_model():
    # global model
    # model = joblib.load('model.pkl')
    pass
```

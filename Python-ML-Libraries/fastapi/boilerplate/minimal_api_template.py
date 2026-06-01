from fastapi import FastAPI
from pydantic import BaseModel

# 1. Initialize App
app = FastAPI(title="My ML API")

# 2. Define Data Model
class HouseFeatures(BaseModel):
    sqft: int
    bedrooms: int

# 3. Create Endpoints
@app.get("/")
def home():
    return {"message": "Welcome to the House Price API!"}

@app.post("/predict")
def predict(features: HouseFeatures):
    # Dummy logic: $100 per sqft + $10k per bedroom
    estimate = (features.sqft * 100) + (features.bedrooms * 10000)
    return {"estimated_price": estimate}

# Run with: uvicorn minimal_api_template:app --reload

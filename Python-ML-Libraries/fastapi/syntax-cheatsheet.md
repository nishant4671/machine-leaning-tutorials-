# FastAPI Syntax Cheatsheet 📝

| Signature | Description | Tiny Example |
| :--- | :--- | :--- |
| `app = FastAPI()` | Initialize the app | `app = FastAPI()` |
| `@app.get('/')` | Handle a GET request | `@app.get('/') def root():` |
| `@app.post('/')` | Handle a POST request | `@app.post('/predict')` |
| `BaseModel` (Pydantic)| Define data structure | `class Item(BaseModel):` |
| `Query(...)` | Validate URL params | `q: str = Query(None)` |
| `Path(...)` | Validate path params | `id: int = Path(...)` |
| `Body(...)` | Get data from request body | `data: dict = Body(...)` |
| `HTTPException` | Return an error code | `raise HTTPException(404)` |
| `uvicorn.run()` | Start the server | `uvicorn.run(app, port=8000)`|

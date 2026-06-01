# FastAPI Pitfalls ⚠️

1. **Synchronous Blocking**: Running a heavy ML prediction inside a normal `def` can block the whole server.
   *Fix*: Use `async def` or run heavy math in a thread/background task.

2. **Missing Type Hints**: FastAPI needs type hints to validate data. Without them, it can't help you!
   *Fix*: Always use `def root(item_id: int):`.

3. **Pydantic V1 vs V2**: Subtle syntax changes between versions.
   *Fix*: Check which version you have installed (`pip show pydantic`).

4. **Port Conflicts**: Trying to run your app on a port (like 8000) that is already being used.
   *Fix*: Use `uvicorn main:app --port 8080`.

5. **JSON Serialization**: Trying to return a NumPy array directly in a response.
   *Fix*: Convert it to a list first: `arr.tolist()`.

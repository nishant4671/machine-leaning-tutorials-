# FastAPI Overview ⚡

Ready to put your model on the web? Let's go fast!

### What is FastAPI?
FastAPI is a modern, high-performance web framework for building APIs with Python based on standard Python type hints.

### Why use it?
It's incredibly fast (near NodeJS/Go speeds), very easy to learn, and automatically creates beautiful documentation (Swagger) for your API.

### Core Concepts
1. **Path Operations**: Functions that handle specific URLs (e.g., `@app.get('/')`).
2. **Pydantic Models**: Using Python types to validate incoming data.
3. **Asynchronous Code**: Using `async` and `await` to handle many requests at once.

### Installation
```bash
pip install fastapi uvicorn
```

### Alternatives
- **Flask**: The classic, simple Python web framework.
- **Django**: A full "batteries-included" web framework for large sites.

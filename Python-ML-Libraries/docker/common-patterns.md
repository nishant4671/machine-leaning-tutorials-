# Docker Common Patterns 💡

### 1. The "Python App" Dockerfile
The standard way to wrap your Python code.
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

### 2. Port Mapping
Accessing your app from outside the container.
`docker run -p 8000:8000 my-fastapi-app`
(Maps your computer's port 8000 to the container's port 8000).

### 3. Volume Mounting
Editing code locally and seeing changes instantly in the container.
`docker run -v $(pwd):/app my-app`

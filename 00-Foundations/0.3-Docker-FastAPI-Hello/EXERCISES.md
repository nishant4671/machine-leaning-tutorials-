# Unit 0.3: Docker & FastAPI Hello World

## 🎯 Learning Objectives
Pull an image, run a container, build a custom Docker image for a FastAPI app, and test it.

---

## 🧪 Exercises
1. **Pull and run** the official python:3.11-slim image interactively. Print 'Hello Docker' from inside the container.

2. **Create a FastAPI app** (main.py) with a /health endpoint that returns {'status': 'ok'}. Run it locally with uvicorn.

3. **Write a Dockerfile** that copies your app, installs dependencies from pyproject.toml (or a equirements.txt), and runs the server.

4. **Build the image** (docker build -t fastapi-hello .) and run it with port mapping. Access http://localhost:8000/health from your browser.

5. **Add a /docs endpoint check** – FastAPI automatically gives you OpenAPI docs. Take a screenshot.

---

## ✅ Completion Checklist
*You have completed this unit when…*
I can pull and run any public Docker image.
I can write a Dockerfile from memory for a simple Python app.
I have a working FastAPI health endpoint running inside a container on my machine.
I understand what a port mapping is and why it’s needed.

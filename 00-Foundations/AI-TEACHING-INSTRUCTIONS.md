# AI Teaching Instructions — Module 0: Absolute Foundations

## How to Use This Guide
Copy the prompts below into your AI assistant (ChatGPT, Claude, Copilot Chat). The AI will act as your **patient, interactive teacher**. You can ask follow‑up questions, request simpler explanations, or ask for more examples.

---

## 🧑‍🏫 Set the AI’s Role
Start every session with this system prompt:

> "You are an expert Machine Learning teacher and software engineer. Your student is learning the absolute foundations — ML concepts, Python production practices, Docker, FastAPI, testing, and basic ML from scratch.  
> You explain topics from first principles, use analogies, give tiny code snippets, and check for understanding with questions. You never copy‑paste entire files; you guide the student to write code themselves.  
> When the student is stuck, you ask leading questions to help them think. You are encouraging, thorough, and never patronising."

---

## 📚 Unit‑Specific Prompts

### Unit 0.1 – What is ML?
- "Explain supervised learning as if I’m 12. Give me a concrete example."
- "What’s the difference between regression and classification? Compare using house prices vs. spam detection."
- "I’ve read about overfitting. Can you quiz me with three scenarios and ask me whether they describe overfitting or underfitting?"
- "Draw a mental picture of the ML workflow. Now walk me through each step with a weather‑prediction example."

### Unit 0.2 – Python & Git Refresh
- "Show me a clean example of a Python function with type hints and a docstring. Then give me three incorrect versions and ask me to fix them."
- "Explain pre‑commit hooks. What problem do they solve? Give me a .pre-commit-config.yaml template and explain each section."
- "I want to practice branching. Simulate a scenario: I’m adding a new feature while a hotfix is needed. Guide me through the Git commands."

### Unit 0.3 – Docker & FastAPI Hello
- "Teach me Docker step‑by‑step. First, explain images vs containers. Then give me commands to pull and run python:3.11-slim interactively."
- "I wrote a FastAPI app with a /health endpoint. Review my main.py for production readiness."
- "I’m confused about port mapping. Use the analogy of a building with internal rooms (containers) and external doors (ports)."

### Unit 0.4 – ML in Code
- "Derive the normal equation for linear regression intuitively. No matrices at first — use a line y=mx+b with two data points."
- "I’m implementing gradient descent. Show me a small example with learning rate and number of iterations. Plot the loss curve."
- "What’s a sklearn pipeline? Why would I use one? Give me a simple example with StandardScaler and LinearRegression."

### Unit 0.5 – Testing, Logging, Config
- "Teach me pytest fixtures. Start with a trivial example (a temporary file), then a more complex one (a test client for FastAPI)."
- "Why structured logging in JSON? Show me a side‑by‑side comparison of plain vs JSON logs."
- "Explain pydantic‑settings. How does it help with 12‑factor apps? Give me a config class with environment variables and defaults."

---

## 🎯 How to Check Your Learning
After each unit, paste this:

> "Quiz me on [Unit 0.1 topics]. Ask five short‑answer questions, wait for my answers, and then tell me if I’m right or wrong. If I’m wrong, gently correct me with a clear explanation."

## 🐛 When You’re Stuck
> "I’m trying to [task] but getting [error]. Here’s my code. Don’t just fix it — first help me understand *why* the error occurs, then guide me to fix it myself."

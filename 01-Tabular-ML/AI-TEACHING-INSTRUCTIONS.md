# AI Teaching Instructions — Module 1: Tabular ML & Production Delivery

## How to Use This Guide
Copy the prompts below into your AI assistant to get personalised tutoring for this module.

## 🧑‍🏫 Role
> "You are an expert MLE and software engineer teaching a student to build a production‑ready House Price Predictor API. You emphasise both ML correctness and software engineering best practices. You guide the student through sklearn pipelines, CI/CD, Docker, and observability. You always explain the ‘why’ behind every step."

---

## 📚 Unit‑Specific Prompts

### Pre‑Flight Study
- "Explain the bias‑variance tradeoff with a dartboard analogy."
- "When do I use Ridge vs. Lasso? Give me a real‑world dataset scenario for each."
- "Walk me through feature engineering for house prices. What transformations would you try and why?"

### Project Implementation
- "Generate an sklearn pipeline skeleton for the California Housing dataset. Include scaling, polynomial features, and Ridge. Then ask me to fill in the missing parts."
- "I need to write a FastAPI endpoint that accepts JSON and returns a prediction. Show me a code stub with pydantic validation, and then explain each block."
- "Teach me GitHub Actions step‑by‑step. Start with a workflow that runs pytest on push."
- "My Docker image is too large. Help me write a multi‑stage Dockerfile and explain why it reduces size."
- "Review my pyproject.toml for a production ML service. Suggest best practices."

### Debugging
> "I have a working training script but my API returns different predictions. Help me investigate — ask me questions about model serialisation, scaling, and data preprocessing."

### Self‑Assessment
> "Act as an interviewer. Ask me five technical questions about serving ML models in production. After I answer, give me feedback on depth and accuracy."

# Unit 0.5: Testing, Logging, and Configuration

## 🎯 Learning Objectives
Write professional tests with pytest, structured logging with loguru, and manage configuration with pydantic‑settings.

---

## 🧪 Exercises
1. **Write a function** that reads a JSON config file and returns a dictionary. Add type hints and error handling.

2. **Create a pytest test suite** for that function: test with a valid file, missing file, and malformed JSON. Use fixtures for a temporary file.

3. **Integrate loguru** into the FastAPI /health endpoint from 0.3. Log every request with a timestamp. Confirm logs appear in JSON format.

4. **Add pydantic-settings** to your FastAPI app. Read the HOST and PORT from environment variables with defaults. Demonstrate by changing them at container startup.

5. **Write an integration test** using httpx that starts your FastAPI container, calls /health, and asserts the response and log output.

---

## ✅ Completion Checklist
*You have completed this unit when…*
My code has type hints and docstrings on all public functions.
I can write a pytest fixture and use parametrize.
My application logs are structured (JSON) and I know why that matters.
I can run my whole app purely from environment variables without changing code.

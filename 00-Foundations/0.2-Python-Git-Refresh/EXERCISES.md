# Unit 0.2: Python & Git Refresher with Production Standards

## 🎯 Learning Objectives
Set up a professional Python project with type hints, virtual environment, pyproject.toml, linters, pre‑commit hooks, and Git branching.

---

## 🧪 Exercises
1. **Create a new repo** on GitHub. Clone it locally. Inside, set up a virtual environment with python -m venv .venv.

2. **Create a pyproject.toml** that defines your project metadata and dependencies (at minimum uff, pytest, loguru).

3. **Add type hints and a docstring** to a simple function (e.g., dd(a: int, b: int) -> int). Commit with a [semantic commit message](https://www.conventionalcommits.org/) like eat: add typed adder.

4. **Configure pre‑commit**: add .pre-commit-config.yaml with hooks for uff, lack, and 	railing-whitespace. Run pre-commit install.

5. **Create a feature branch** (git checkout -b improve-logging), add a logging module, commit, push, open a PR against main, and merge it yourself.

6. **Write a small script** that uses loguru to log a message in JSON format.

---

## ✅ Completion Checklist
*You have completed this unit when…*
My repo has a clean pyproject.toml, .pre-commit-config.yaml, and a .venv (gitignored).
Pre‑commit hooks run automatically on every commit.
I have successfully created and merged a pull request using Git branches.
I can explain the difference between a equirements.txt and a pyproject.toml.

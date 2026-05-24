# How to Approach Every Project (The "5‑P" Method)

*Your personal mentor's guide to building ML projects that teach, impress, and stick.*

## Mindset
- This is a **product**, not a demo. It must run, be tested, and be understood.
- **Done is better than perfect.** Aim for "works, tested, documented."
- Every line is a **decision**. Pause and ask "Why?"

## The 5‑P Workflow
| Phase | Tasks | Time |
|-------|-------|------|
| **Plan** | Sketch system, draft ADRs, define API contracts. | 1–2h |
| **Prototype** | Jupyter notebook: data → model → one prediction. | 2–4h |
| **Productionize** | Move to src/, add tests, logging, FastAPI, Docker, CI/CD. | 6–10h |
| **Polish** | README, docstrings, linters, final ADRs. | 2–3h |
| **Post‑Mortem** | Retrospective in learning log. | 0.5h |

**Rule:** After Prototype, throw away the notebook and rewrite cleanly. It's painful but transformative.

## Adding "Why?" Annotations
After every key step, add a comment or a note answering "Why did I just do that?"  
Examples:
- # WHY: Split before scaling to prevent data leakage.
- # WHY: python:3.11-slim reduces image size and attack surface.
- # WHY: L2 penalty in Ridge handles multicollinearity.

These become your personal textbook for interviews.

## Using AI Assistants
- **Plan:** Ask AI to review your design.
- **Prototype:** Generate boilerplate, then understand every line.
- **Productionize:** Let AI draft tests, CI config, Dockerfiles. Review thoroughly.
- **Polish:** AI drafts README; you personalise.
- **Post‑Mortem:** AI asks reflection questions.

**Golden rule:** If you can't explain it, don't commit it.

## Handling Curveballs (Requirement Changes)
1. Identify the affected module.
2. Write a failing test first.
3. Fix the code, update ADR.
4. Reflect on how the architecture held up.

## Version Control
- Small, frequent commits with semantic messages (eat:, ix:, docs:).
- Work on feature branches, merge via PR.
- Tag releases (1.0.0) when project is done.

## After Each Project: 10‑Minute Retro
Answer in your learning log:
1. Hardest bug? How fixed?
2. Most surprising "Why?"?
3. What would I do differently next time?
4. One thing to carry forward?

---

*Follow this guide. It's the shortcut to becoming the engineer you want to be.*

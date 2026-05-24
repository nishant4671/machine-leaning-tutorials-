# Ideal Learning Workflow for the SWE × AI Engineer Path

*This is your gold‑standard routine, crafted from years of mentoring self‑taught engineers. It's not rigid—treat it as your compass. If your week deviates, just realign the next. The goal is sustained progress, not perfection.*

---

## 🧭 Core Principles (Read Aloud Every Monday)

1. **Consistency > intensity.** 10 focused hours/week beats a weekend binge.
2. **Understand, don’t just complete.** If you can’t explain it to a rubber duck, you haven’t learned it.
3. **Ship working code.** Every study cycle ends with something running—a script, an API, a container.
4. **Use AI as a bicycle, not a car.** It accelerates you, but you still pedal (think) and steer (decide).
5. **Document decisions, not just facts.** “Why did I choose X over Y?” is what senior engineers ask.

---

## 📅 Ideal Weekly Cadence (10–15 hours/week)

### Monday – *Setup & Goal Setting (30 min)*
- Review last week’s entry in learning-log.md.
- Set 2‑3 concrete, achievable goals for the week (e.g., “Finish Pre‑Flight study of TF‑IDF”, “Get training script running with MLflow”).
- Open the module’s README.md and the AI Prompt Guide section from INDEX.md.

### Tuesday to Thursday – *Deep Work Cycles (3–4 sessions of 1.5‑2 hrs each)*
Each session follows this **pomodoro‑inspired loop**:

| Phase | Duration | What You Do |
|-------|----------|-------------|
| **Prime** | 5 min | Read the day’s objective. Open the theory resource, code files, and terminal. |
| **Learn** | 25–40 min | Absorb theory (video/article). Pause to write a 1‑sentence summary in your own words. |
| **Apply** | 40–60 min | Hands‑on: code the exercise, prototype the project step. *Use the AI assistant exactly as prescribed in the Prompt Guide.* |
| **Reflect** | 10 min | In learning-log.md, jot down: 1 thing that clicked, 1 thing that confused you, and your next step. |

**Session rules:**
- Phone in another room. No social media.
- When stuck for >15 min, **immediately** prompt your AI tutor (see “Stuck Protocol” below).
- If tired, stop. A bad hour of bug‑wrestling reinforces bad patterns.

### Friday – *Integration & Polish (2–3 hrs)*
- Bring your week’s work into a working state. If building a project step, make sure the current endpoint runs or the test passes.
- Update documentation (README, docstrings, ADR if you made a tech choice).
- Commit and push to GitHub with a meaningful commit message.
- Run the AI code‑review prompt from the module’s guide. Fix any security/logic issues it finds.

### Saturday / Sunday – *Flex & Depth (optional 2 hrs)*
- Light review: re‑read your glossary.md entries for the week.
- If curious, go deeper on one topic (e.g., read the paper behind an algorithm).
- **No new project code**—rest prevents burnout. Your brain will consolidate memories.

---

## 🤖 How to Interact with AI Assistants (The “Senior Dev” Method)

1. **Before asking:** Write a comment in your code describing what you want to achieve.  
   *Example:* “# Load preprocessor and model, predict on user input, return JSON with confidence.”
2. **Paste that comment into the chat** plus any relevant file paths or error messages.  
3. **Use the module‑specific prompt** from INDEX.md. It’s tuned to produce production‑ready code.
4. **Review the output line by line.** Ask yourself: “Do I understand this? Is it secure? Does it handle edge cases?”
5. **Modify:** Change variable names to your convention, add your own logging, tighten types.
6. **Test:** Immediately run the code or write a test. If it fails, paste the error back to the AI and ask “Why?”—don’t just ask for the fix; ask for the *reason*.

**Golden rule:** The AI’s code is a draft. The final commit must be *your* code—understood, tested, refactored.

---

## 📝 Note‑Taking & Portfolio Building

- **learning-log.md**: Quick daily reflection. Format:2026-05-21
Studied: TF‑IDF vectorisation.

Insight: IDF dampens common words like “the”.

Confused: How to handle out‑of‑vocabulary words in production.

Next: Read about hashing vectoriser.- **glossary.md**: Add every new term with a one‑line plain‑English definition.  
*Example:* “**TF‑IDF** – a way to turn text into numbers that gives less weight to frequent words.”
- **Project READMEs**: After each project, write them as if you’re handing off to another engineer. Include:
- What it does
- How to run (Docker, local)
- API endpoints (with examples)
- Architecture decisions (link to ADRs)
- How to test

---

## 🧪 Project Workflow (Inside a Module)

1. **Read the Pre‑Flight Study** in the unit’s README.md. Do the readings, take light notes.
2. **Run the AI “Explain” prompt** for the core algorithm to cement intuition.
3. **Execute the project milestones** one by one. Commit after each milestone.
 - *Prototype in a Jupyter notebook first* (if needed), but then **move to scripts** under src/. Notebooks are not production.
4. **When a milestone works, pause and write a quick ADR** (using the template) for any tech choice you made.
5. **After the whole project runs**, ask the AI for a code review and security audit. Fix issues.
6. **Tag a release** on GitHub (1.0.0). This shows employers you finish things.

---

## 🚨 Stuck Protocol (Don’t Spin Your Wheels)

1. **Google the error message.** (Yes, senior engineers still do this.)
2. **Rubber‑duck debug:** Explain the problem aloud to an imaginary duck. Often you’ll spot the fix.
3. **Ask the AI with context:**
 - Paste the full traceback.
 - Paste the relevant code file.
 - Say: “I expected X, but got Y. Help me understand why and suggest a fix. Explain it step by step.”
4. **If still stuck after 30 minutes:** Note the problem in learning-log.md and move to the next milestone. When you revisit later with fresh eyes, it often unlocks.

---

## 🔁 Adapting This Workflow to Your Life

- **If you only have 5 hours/week:** Do one deep‑work cycle (Learn+Apply) per study day, and skip the optional weekend depth.
- **If you’re on a roll:** Extend the Apply phase, but always end with a Reflect note—it solidifies learning.
- **If life gets chaotic:** Drop back to just maintaining your notes and glossary. Resume deep work when you can. The structure will be waiting.

---

## 🧑‍🏫 Final Advice from Your Teacher

> “You’ve chosen a path that turns curiosity into career superpowers. The syllabus is your map, this workflow is your rhythm. Trust the process: small, deliberate steps compound into deep expertise. When you feel lost, remember why you started—to build things that matter, to understand the ‘why,’ and to become the engineer who can handle anything.  
> I’ve left fingerprints all over this plan, but the journey is yours. Compare your style against this ideal, but never beat yourself up. Adjust, improve, keep going. You’ve got this.”

— *Your teacher*

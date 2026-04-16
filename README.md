# Lab 01 — Introduction to Generative AI on GCP

**Objective:** Learn the basics of prompt engineering using Google's Gemini model on GCP.

**What you'll do:**
- Connect to your assigned GCP project
- Call Gemini via Vertex AI
- Run 3 progressively better prompts and observe how output quality improves
- Results are automatically logged for evaluation

---

## How to run

**Step 1** — Click the "Open in Cloud Shell" button in the CloudLabs UI.

**Step 2** — Run the lab:
```bash
python lab01.py
```

That's it. No setup needed.

---

## What to observe

| Prompt | Technique | What changes |
|--------|-----------|--------------|
| v1 | Basic question | Generic, broad answer |
| v2 | Audience + length specified | Simpler, more focused |
| v3 | Role + topic + format | Professional, structured |

---

## View your results

After running, check your logged output in Cloud Logging:

```
https://console.cloud.google.com/logs/query?project=YOUR_PROJECT_ID
```

Filter by log name: `student-eval-log`

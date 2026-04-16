"""
Lab 01 — Introduction to Generative AI on GCP
CloudLabs EDU | Run in Cloud Shell: python lab01.py
"""

import os, sys, time, logging
import vertexai
from vertexai.generative_models import GenerativeModel
import google.cloud.logging

# ── Setup (silent) ────────────────────────────────────────────────────────────
PROJECT_ID = (
    os.environ.get("GOOGLE_CLOUD_PROJECT")
    or os.environ.get("DEVSHELL_PROJECT_ID")
)
if not PROJECT_ID:
    print("ERROR: Could not detect your GCP project.")
    print("Make sure you opened Cloud Shell from your assigned project.")
    sys.exit(1)

# Suppress noisy SDK warnings
import warnings
warnings.filterwarnings("ignore")
logging.getLogger("google").setLevel(logging.ERROR)
logging.getLogger("urllib3").setLevel(logging.ERROR)

# Init Vertex AI
vertexai.init(project=PROJECT_ID, location="us-central1")

# Load model with fallback
try:
    model = GenerativeModel("gemini-2.5-flash-lite")
    _model_name = "gemini-2.5-flash-lite"
except Exception:
    model = GenerativeModel("gemini-1.5-flash")
    _model_name = "gemini-1.5-flash"

# Cloud Logging for evaluation
try:
    google.cloud.logging.Client(project=PROJECT_ID).setup_logging()
except Exception:
    pass
logger = logging.getLogger("student-eval-log")

def _call(prompt: str) -> str:
    return model.generate_content(prompt).text

# ── Lab begins ────────────────────────────────────────────────────────────────
print(f"\n{'='*55}")
print(f"  Lab 01 — Introduction to Generative AI on GCP")
print(f"{'='*55}")
print(f"  Project : {PROJECT_ID}")
print(f"  Model   : {_model_name}")
print()

# ── Prompt v1: Basic ──────────────────────────────────────────────────────────
print("[ Prompt v1 — Basic question ]")
print("  A simple, unstructured question. Notice how the response")
print("  is broad and generic.\n")

prompt_v1 = "What is GCP?"
print(f"  > {prompt_v1}\n")
response_v1 = _call(prompt_v1)
print(f"  {response_v1[:300].strip()}")
print()
logger.info(f"[v1] {response_v1}")
time.sleep(1)

# ── Prompt v2: Audience-aware ─────────────────────────────────────────────────
print("[ Prompt v2 — Specify your audience ]")
print("  Adding audience + length constraint makes the response")
print("  more focused and easier to understand.\n")

prompt_v2 = "Explain Google Cloud Platform to a 10-year-old in 2 sentences."
print(f"  > {prompt_v2}\n")
response_v2 = _call(prompt_v2)
print(f"  {response_v2.strip()}")
print()
logger.info(f"[v2] {response_v2}")
time.sleep(1)

# ── Prompt v3: Role + format ──────────────────────────────────────────────────
print("[ Prompt v3 — Role + topic + format ]")
print("  The most structured prompt. Assigning a role and specifying")
print("  output format produces the most professional result.\n")

prompt_v3 = (
    "As a Cloud Architect, provide a professional 1-paragraph summary of GCP "
    "focusing on its data analytics and AI capabilities. "
    "Use a bulleted list for key features."
)
print(f"  > {prompt_v3[:80]}...\n")
response_v3 = _call(prompt_v3)
print(f"  {response_v3.strip()}")
print()
logger.info(f"[v3] {response_v3}")

# ── Done ──────────────────────────────────────────────────────────────────────
print(f"{'='*55}")
print(f"  Lab complete. Results logged for evaluation.")
print(f"  https://console.cloud.google.com/logs/query?project={PROJECT_ID}")
print(f"{'='*55}\n")

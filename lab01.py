import os, warnings, logging
warnings.filterwarnings("ignore")
logging.disable(logging.CRITICAL)

import vertexai
from vertexai.generative_models import GenerativeModel
import google.cloud.logging

PROJECT_ID = os.environ.get("GOOGLE_CLOUD_PROJECT") or os.environ.get("DEVSHELL_PROJECT_ID")
vertexai.init(project=PROJECT_ID, location="us-central1")

try:
    model = GenerativeModel("gemini-2.5-flash-lite")
except Exception:
    model = GenerativeModel("gemini-1.5-flash")

try:
    google.cloud.logging.Client(project=PROJECT_ID).setup_logging()
except Exception:
    pass

logging.disable(logging.NOTSET)
logger = logging.getLogger("student-eval-log")

response = model.generate_content("What is GCP?")
print(response.text)

try:
    logger.info(f"[v1] {response.text}")
except Exception:
    pass

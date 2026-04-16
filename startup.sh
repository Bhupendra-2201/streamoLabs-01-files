#!/bin/bash
# CloudLabs EDU — Lab 01 Setup
# This script runs automatically when you open Cloud Shell for this lab.
# It cleans any previous session and pulls the latest lab files.

set -e

REPO_URL="https://github.com/Bhupendra-2201/streamoLabs-01-files.git"
LAB_DIR="$HOME/lab01"

# ── Detect project ────────────────────────────────────────────────
PROJECT_ID="${GOOGLE_CLOUD_PROJECT:-$DEVSHELL_PROJECT_ID}"
if [ -z "$PROJECT_ID" ]; then
  echo "ERROR: No GCP project detected. Open Cloud Shell from your assigned project."
  exit 1
fi

# ── Clean previous session ────────────────────────────────────────
if [ -d "$LAB_DIR" ]; then
  rm -rf "$LAB_DIR"
fi

# ── Pull fresh lab files ──────────────────────────────────────────
echo "Setting up lab environment..."
git clone --quiet "$REPO_URL" "$LAB_DIR"
cd "$LAB_DIR"

# ── Fetch lab credentials from Secret Manager ─────────────────────
CREDS_DIR="$HOME/.config/cloudlabs"
CREDS_PATH="$CREDS_DIR/lab-credentials.json"
mkdir -p "$CREDS_DIR"

if gcloud secrets versions access latest \
     --secret="cloudlabs-lab-credentials" \
     --project="$PROJECT_ID" \
     > "$CREDS_PATH" 2>/dev/null; then
  chmod 600 "$CREDS_PATH"
  export GOOGLE_APPLICATION_CREDENTIALS="$CREDS_PATH"
  grep -qxF "export GOOGLE_APPLICATION_CREDENTIALS=$CREDS_PATH" ~/.bashrc \
    || echo "export GOOGLE_APPLICATION_CREDENTIALS=$CREDS_PATH" >> ~/.bashrc
fi

# ── Install packages ──────────────────────────────────────────────
pip install --quiet --upgrade google-cloud-aiplatform google-cloud-logging 2>/dev/null

echo ""
echo "Ready. Run your lab:"
echo "  cd ~/lab01 && python lab01.py"
echo ""

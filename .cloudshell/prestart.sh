#!/bin/bash
# Runs automatically when Cloud Shell opens this repo.
# Installs dependencies and sets up credentials silently.

PROJECT_ID="${GOOGLE_CLOUD_PROJECT:-$DEVSHELL_PROJECT_ID}"

# Fetch lab credentials from Secret Manager
CREDS_PATH="$HOME/.config/cloudlabs/lab-credentials.json"
mkdir -p "$(dirname $CREDS_PATH)"
gcloud secrets versions access latest \
  --secret="cloudlabs-lab-credentials" \
  --project="$PROJECT_ID" \
  > "$CREDS_PATH" 2>/dev/null && \
  chmod 600 "$CREDS_PATH" && \
  export GOOGLE_APPLICATION_CREDENTIALS="$CREDS_PATH" && \
  grep -qxF "export GOOGLE_APPLICATION_CREDENTIALS=$CREDS_PATH" ~/.bashrc || \
  echo "export GOOGLE_APPLICATION_CREDENTIALS=$CREDS_PATH" >> ~/.bashrc

# Install packages silently
pip install --quiet --upgrade google-cloud-aiplatform google-cloud-logging 2>/dev/null

echo ""
echo "Lab 01 ready. Run:  python lab01.py"
echo ""

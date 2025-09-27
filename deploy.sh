#!/usr/bin/env bash
# Usage: ./deploy.sh YOUR_PROJECT_ID [REGION]
set -e
PROJECT_ID="$1"
REGION="${2:-us-central1}"
SERVICE_NAME="newswhisper"

if [[ -z "$PROJECT_ID" ]]; then
  echo "Usage: ./deploy.sh YOUR_PROJECT_ID [REGION]"
  exit 1
fi

gcloud config set project $PROJECT_ID
# enable required APIs
gcloud services enable run.googleapis.com cloudbuild.googleapis.com

# build image with Cloud Build and push to GCR
gcloud builds submit --tag gcr.io/$PROJECT_ID/$SERVICE_NAME .

# deploy to Cloud Run (allow unauthenticated for demo)
gcloud run deploy $SERVICE_NAME \
  --image gcr.io/$PROJECT_ID/$SERVICE_NAME \
  --platform managed \
  --region $REGION \
  --allow-unauthenticated --port 8080

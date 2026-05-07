#!/bin/bash
cd /home/ubuntu/lab-midterm-sp26

# Fetch latest data from GitHub
git pull origin main

# Train model
python3 train.py

# Restart Docker container with new model
docker stop ml-api 2>/dev/null
docker rm ml-api 2>/dev/null
docker run -d --name ml-api -p 8000:8000 ml-pipeline-api

echo "$(date): Pipeline ran successfully" >> /home/ubuntu/pipeline.log

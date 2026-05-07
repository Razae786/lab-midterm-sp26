#!/bin/bash
set -e
cd /home/ubuntu/lab-midterm-sp26
git pull origin main
python3 train.py
docker stop ml-api 2>/dev/null || true
docker rm ml-api 2>/dev/null || true
docker run -d --name ml-api -p 8000:8000 ml-pipeline-api
sleep 5
curl -s http://localhost:8000/metrics
echo "Pipeline completed at $(date)"

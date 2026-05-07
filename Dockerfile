FROM python:3.11-slim
WORKDIR /app

RUN pip install --no-cache-dir fastapi uvicorn joblib numpy scikit-learn pandas requests

# Copy everything needed
COPY config.json .
COPY dataset/train.csv dataset/
COPY train.py .
COPY app.py .

# Train the model inside container
RUN python3 train.py

EXPOSE 8000
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

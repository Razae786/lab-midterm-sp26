FROM python:3.11-slim
WORKDIR /app
RUN pip install fastapi uvicorn joblib numpy scikit-learn pandas requests
COPY app.py .
COPY metrics.json .
COPY model.pkl .
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

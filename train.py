import json
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load config
with open('config.json') as f:
    config = json.load(f)

student_id = config['student_id']

# Load dataset
df = pd.read_csv('dataset/train.csv')

# Handle NaN values - drop rows with any NaN
df = df.dropna()

# Assume last column is target
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

# Save model
joblib.dump(model, 'model.pkl')

# Save metrics
metrics = {
    'student_id': student_id,
    'dataset_version': 1,
    'model_type': 'logistic_regression',
    'accuracy': round(accuracy, 4),
    'samples': len(df)
}

with open('metrics.json', 'w') as f:
    json.dump(metrics, f)

print("=" * 50)
print("MODEL TRAINING COMPLETE")
print("=" * 50)
print(f"Student ID       : {student_id}")
print(f"Dataset Version  : 1")
print(f"Model Type       : logistic_regression")
print(f"Dataset Samples  : {len(df)}")
print(f"Accuracy         : {accuracy:.4f}")
print("=" * 50)

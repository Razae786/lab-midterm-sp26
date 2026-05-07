pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', 
                    url: 'https://github.com/Razae786/lab-midterm-sp26.git'
            }
        }
        
        stage('Install Dependencies') {
            steps {
                sh 'pip3 install pandas numpy scikit-learn joblib fastapi uvicorn'
            }
        }
        
        stage('Train Model') {
            steps {
                sh 'python3 train.py'
                sh 'cat metrics.json'
            }
        }
        
        stage('Build Docker') {
            steps {
                sh '''
                    docker stop ml-api 2>/dev/null || true
                    docker rm ml-api 2>/dev/null || true
                    docker build -t ml-pipeline-api .
                '''
            }
        }
        
        stage('Deploy API') {
            steps {
                sh 'docker run -d --name ml-api -p 8000:8000 ml-pipeline-api'
                sh 'sleep 15'
                sh 'curl -s http://localhost:8000/metrics'
            }
        }
    }
}

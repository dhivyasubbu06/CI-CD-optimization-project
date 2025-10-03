pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/dhivyasubbu06/ci-cd-queue-optimization.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Train Model') {
            steps {
                sh 'python src/train_model.py'
            }
        }
        stage('Predict Queue') {
            steps {
                sh 'python src/predict_queue.py'
            }
        }
    }
}

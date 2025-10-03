pipeline {
    agent any

    stages {
        stage('Clone') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-pat', // replace with your Jenkins credential ID
                    url: 'https://github.com/dhivyasubbu06/CI-CD-optimization-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                bat 'python src/train_model.py'
            }
        }

        stage('Predict Queue') {
            steps {
                bat 'python src/predict_queue.py'
            }
        }
    }
}

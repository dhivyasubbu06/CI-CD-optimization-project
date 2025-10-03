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
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Train Model') {
            steps {
                sh 'python3 src/train_model.py'
            }
        }

        stage('Predict Queue') {
            steps {
                sh 'python3 src/predict_queue.py'
            }
        }
    }
}

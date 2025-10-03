pipeline {
    agent any

    environment {
        CONDA_ENV = "cicd"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-pat',
                    url: 'https://github.com/dhivyasubbu06/CI-CD-optimization-project.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                eval "$(conda shell.bash hook)"
                conda activate $CONDA_ENV
                python --version
                pip --version
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                eval "$(conda shell.bash hook)"
                conda activate $CONDA_ENV
                python train_model.py
                '''
            }
        }

        stage('Predict Queue') {
            steps {
                sh '''
                eval "$(conda shell.bash hook)"
                conda activate $CONDA_ENV
                python predict_queue.py
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check logs for errors.'
        }
    }
}

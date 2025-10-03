pipeline {
    agent any

    environment {
        CONDA_ENV = "cicd"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                git credentialsId: 'github-pat', url: 'https://github.com/dhivyasubbu06/CI-CD-optimization-project.git'
            }
        }

        stage('Setup Python Environment') {
            steps {
                // Initialize Conda for the shell
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
                # Add your model training script here
                python train_model.py
                '''
            }
        }

        stage('Predict Queue') {
            steps {
                sh '''
                eval "$(conda shell.bash hook)"
                conda activate $CONDA_ENV
                # Add your prediction script here
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

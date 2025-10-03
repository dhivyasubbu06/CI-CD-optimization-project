pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/dhivyasubbu06/CI-CD-optimization-project.git', credentialsId: 'github-pat'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    python3 -m venv $VENV_DIR
                    source $VENV_DIR/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                    source $VENV_DIR/bin/activate
                    python src/train_model.py
                '''
            }
        }

        stage('Predict Queue') {
            steps {
                sh '''
                    source $VENV_DIR/bin/activate
                    python src/predict_queue.py
                '''
            }
        }
    }

    post {
        success {
            echo "Pipeline completed successfully!"
        }
        failure {
            echo "Pipeline failed. Check logs for errors."
        }
    }
}

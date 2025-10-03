pipeline {
    agent any

    environment {
        VENV_DIR = "venv"
    }

    stages {
        stage('Checkout') {
            steps {
                // Checkout code from GitHub
                git branch: 'main', url: 'https://github.com/dhivyasubbu06/CI-CD-optimization-project.git', credentialsId: 'github-pat'
            }
        }

        stage('Setup Python Environment') {
            steps {
                sh '''
                    #!/bin/bash
                    # Install python3-venv if not available
                    sudo apt-get update
                    sudo apt-get install -y python3-venv python3-pip

                    # Create virtual environment
                    python3 -m venv $VENV_DIR
                    source $VENV_DIR/bin/activate

                    # Upgrade pip
                    pip install --upgrade pip

                    # Install project dependencies
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Train Model') {
            steps {
                sh '''
                    # Activate virtual environment
                    source $VENV_DIR/bin/activate

                    # Run the training script
                    python3 src/train_model.py
                '''
            }
        }

        stage('Predict Queue') {
            steps {
                sh '''
                    # Activate virtual environment
                    source $VENV_DIR/bin/activate

                    # Run the prediction script
                    python3 src/predict_queue.py
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

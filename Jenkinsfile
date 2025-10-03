pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git branch: 'main',
                    credentialsId: 'github-pat',
                    url: 'https://github.com/dhivyasubbu06/ci-cd-queue-optimization.git'
            }
        }
        ...
    }
}

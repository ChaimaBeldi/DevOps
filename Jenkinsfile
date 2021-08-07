pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'yum update -y'
                sh 'python3 -m venv python3-virtualenv'
                sh 'source python3-virtualenv/bin/activate'

                
            }
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip install --user -r requirements.txt'
                sh 'apt-get update -y'
                sh 'apt-get install -y python3-venv'
                sh 'python3 -m venv env'
                sh 'source env/bin/activate'
                
                
            }
        }
    }
}

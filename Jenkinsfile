pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'python --version'
                sh 'pip install --user -r requirements.txt'
                sh 'set FLASK_APP = app.py'
                sh 'python -m flask run'
            }
        }
    }
}

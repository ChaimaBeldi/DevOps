pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip install --user -r requirements.txt'
                sh 'set FLASK_APP = app.py'
                sh 'python -m flask run'
            }
        }
        stage('Sonar Analysis') {
            steps {
                withSonarQubeEnv('sonar') {
                    sh '/opt/sonar/bin/sonar-scanner'
                }
            }
        }
        stage('Sonar Publish') {
            steps {
                sh '/opt/sonar/bin/sonar-scanner'
            }
        }
    }
}

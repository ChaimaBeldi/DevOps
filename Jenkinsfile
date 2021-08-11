
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'pip install -r requirements.txt'
                bat 'set FLASK_APP = app.py'
            }
        }
        stage('Sonar Scanner') {
            steps {
                withSonarQubeEnv('sonar') {
                    bat 'python app.py sonar:sonar'
                }
            }
        }
        stage('Sonar Publish') {
            steps {
                bat '/opt/sonar/bin/sonar-scanner'
            }
        }
    }
}

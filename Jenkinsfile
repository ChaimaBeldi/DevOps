
pipeline {
    agent any

        stages {
        stage('Build') {
            steps {
               bat 'pip install -r requirements.txt'
               bat 'set FLASK_APP = app.py'
            }
        }
            
        stage('SonarQube Analysis') {
            steps {
                script{
                       def scannerHome = tool 'sonarqube'
                        withSonarQubeEnv('sonarqube') {
                        bat "${scannerHome}/bin/sonar-scanner"
                        }
                }
            }
        }
        }
}

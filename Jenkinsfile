
pipeline {
    agent any

        stages {
        stage('Build') {
            steps {
               bat 'pip install -r requirements.txt'
               bat 'set FLASK_APP = app.py'
               bat 'python -m flask run'
            }
        }
            
        stage('SonarQube Analysis') {
            steps {
                script{
                       def scannerHome = tool 'SonarQube'
                        withSonarQubeEnv('SonarQube') {
                        bat "${scannerHome}/bin/sonar-scanner"
                        }
                }
            }
        }
        }
}

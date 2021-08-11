pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'pip install --user -r requirements.txt'
                bat 'set FLASK_APP = app.py'
            }
        }
        stage('SonarQube Analysis') {
    def scannerHome = tool 'SonarScanner';
    withSonarQubeEnv() {
      bat "${scannerHome}/bin/sonar-scanner"
     }
   }
 }
}

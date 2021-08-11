
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
                      def scannerHome = tool 'sonarScanner';
                       withSonarQubeEnv('SonarQube 6.2') {
                       bat "${scannerHome}/bin/sonar-runner.bat"
                       }
                }
            }
        }
        }
}

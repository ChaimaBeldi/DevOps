pipeline {
    agent any

    stages {

        stage('SCM') {
                checkout scm
            }
        stage('Build') {
            steps {
                bat 'pip install --user -r requirements.txt '
                bat 'python -m virtualenv env'
                bat 'virtualenv \\Scripts\\activate'
                
                
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

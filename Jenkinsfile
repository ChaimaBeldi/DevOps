
pipeline {
    agent any

        stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'set FLASK_APP = app.py'
            }
        }
        stage('Unit Test') {
            steps {
                sh 'python3 ./tests/test.py'
            }
        }
            
        stage('SonarQube Analysis') {
            steps {
                script{
                       def scannerHome = tool 'sonarqube'
                        withSonarQubeEnv('sonarqube') {
                            sh "${scannerHome}/bin/sonar-scanner"
                        }
                }
            }
        }
        }
}

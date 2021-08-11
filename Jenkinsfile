
pipeline {
    agent any

        stages {
        stage('Build') {
            steps {
                bat 'py get-pip.py'
                bat 'pip install -r requirements.txt'
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


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
                parallel(
                    a: {
                        sh 'timeout 20s flask run&'
                    },
                    b: {
                        sh 'coverage run ./tests/utest.py'
                        sh 'coverage report -m'
                    }
                )
            }
        }
         stage('Heroku Deployment') {
            steps {
                sh 'heroku login <<<<bilel.besbes1@gmail.com<MouMou@Ba3Ba3'
                sh 'git push https://git.heroku.com/monop-devops.git'
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
         stage('Selenium Testing') {
            steps {
                sh 'chmod +x tests/geckodriver'
                sh 'ls -ali'
                sh 'python3 tests/fronttest.py'
            }
        }   
    
        }
}

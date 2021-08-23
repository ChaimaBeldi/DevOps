
pipeline {
    agent any

        stages {
        stage('Build') {
            steps {
                sh 'echo $(pwd)'
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
         stage('Heroku Deployment') {
            steps { 
                    withCredentials([[$class: 'StringBinding', credentialsId: 'heroku-api-key', variable: 'heroku-api-key']]) {   
                        sh 'git pull https://git.heroku.com/devopsmonop.git HEAD:main'
                        sh 'git push https://git.heroku.com/devopsmonop.git HEAD:main'
                       }         
            }
         }
         stage('Selenium Testing') {
            steps {
                sh 'chmod +x tests/geckodriver'
                sh 'python3 tests/fronttest.py'
            }
        }  
         stage ('Documentation'){
             steps {
                 sh 'python3 -m pydoc -w app'
                 sh 'echo $(pwd)/app.html'
                 sh 'xdg-open app.html'
                 }
         }
        }
}

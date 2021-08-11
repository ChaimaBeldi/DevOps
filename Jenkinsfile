
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
               def scannerHome = tool 'SonarQube'
               withSonarQubeEnv('SonarQube') {
               bat '""/var/lib/jenkins/tools/hudson.plugins.sonar.SonarRunnerInstallation/SonarQube/bin/sonar-scanner \
                     -D sonar.projectVersion=1.0-SNAPSHOT \
                     -D sonar.login=admin \
                     -D sonar.password=123456 \
                     -D sonar.projectBaseDir=C:/Windows/system32/config/systemprofile/AppData/Local/Jenkins/.jenkins/workspace/monoprix_devOps_develop \
                     -D sonar.projectKey=my-app \
                     -D sonar.sourceEncoding=UTF-8 \
                     -D sonar.language=python \
                     -D sonar.sources=app.py \
                     -D sonar.tests=app.py \
                     -D sonar.host.url=http://localhost:9000/""'
                         }}
            
        }
        }
}

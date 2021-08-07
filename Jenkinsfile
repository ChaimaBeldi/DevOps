pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip install --user -r requirements.txt'
                sh 'sudo apt install virtualenv'
                sh 'virtualenv env'
                sh 'source env/bin/activate'
                
                
            }
        }
    }
}

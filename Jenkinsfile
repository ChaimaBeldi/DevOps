pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip install --user -r requirements.txt'
                sh 'pip install virtualenv'
                sh 'virtualenv env'
                sh 'source env/bin/activate'
                
                
            }
        }
    }
}

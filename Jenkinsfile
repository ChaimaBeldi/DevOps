pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip install --user -r requirements.txt '
                sh 'python -m virtualenv env'
                sh 'virtualenv \\Scripts\\activate'
                
                
            }
        }
    }
}

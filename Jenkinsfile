pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'pip install --user -r requirements.txt '
                bat 'python -m virtualenv env'
                bat 'env \\Scripts\\activate'
                
            }
        }
    }
}

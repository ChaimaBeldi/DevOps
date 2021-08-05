pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                bat 'pip install --user -r requirements.txt '
                bat 'python -m virtualenv env'
                bat 'virtualenv \\Scripts\\activate'
                bat 'pip install pmdarima'
                bat 'flask run'
            }
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip install --user -r requirements.txt '
                sh 'py -m venv env'
                sh 'env \\Scripts\\activate'
                
                
            }
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip install --user -r requirements.txt'
                sh 'python -m venv env'
                sh 'virtualenv \\Scripts\\activate'
                
                
            }
        }
    }
}

pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip install -r requirements.txt'
                sh 'py -m venv env'
                sh 'env \\Scripts\\activate'
            }
        }
    }
}

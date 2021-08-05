pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'sudo pip install requirements.txt'
                sh 'py -m venv env'
                sh 'env \\Scripts\\activate'
            }
        }
    }
}

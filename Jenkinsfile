pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'pip install --user -r requirements.txt'
                sh 'apt install python-virtualenv -y'
                sh 'virtualenv -p /usr/bin/python3 env'
                sh '. env/bin/python3'
                sh 'virtualenv \\Scripts\\activate'
                
                
            }
        }
    }
}

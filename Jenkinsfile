
pipeline {
    agent any

        stages {
            stage('Build') {
                steps {
                 bat 'python3 -m virtualenv local'
                 bat 'source ./local/bin/activate'
                 bat 'pip install --upgrade --requirement requirements.txt'
                }
            }
         
          
        }
}

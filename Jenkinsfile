
pipeline {
    agent any

        stages {
            stage('Build') {
                steps {
                  python3 -m virtualenv local
                    source ./local/bin/activate
                    pip install --upgrade --requirement requirements.txt
                }
            }
         
          
        }
}

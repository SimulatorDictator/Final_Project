pipeline {
    agent any 
    stages {
        stage('Install requirements') {
            steps {
                sh "pip install -r requirements.txt"
            }
        }

        stage('Create database') {
            steps {
                sh "python3 create.py"
            }
        }

        stage('Run the tests'){
            steps {
                sh "echo 'This is where your tests are going to go'"
            }
        }

        stage('Run the application') {
            steps {
                sh "python3 app.py"
            }
        }
    }
}

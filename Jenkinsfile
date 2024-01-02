pipeline {
    agent any
    stages {
        stage('Init') {
            steps {
                cleanWs()
                checkout scm
                sh 'git clone https://github.com/kura1528/client-excel.git'
            }
        }
        stage('Build') {
            steps {
                sh 'python main.py'
            }
        }
        stage('Post Build') {
            steps {
                sh '''git status
                git add output.json
                git commit -m "new json file created"
                git fetch -v 
                git push -u origin main'''
            }
        }
    }
}

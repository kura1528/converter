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
                sh '''git add output.json
                git commit -m "New JSON file"
                git checkout -b main
                git push origin main
                git commit --kura1528 --reset-author'''
            }
        }
    }
}

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
                sh '''git init
                git remote set-url origin https://github.com/kura1528/converter.git
                git pull origin main
                git add output.json
                git commit -m "new json file created"
                git push -u origin main'''
            }
        }
    }
}

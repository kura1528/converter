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
                git remote add origin https://kura1528:Secureme@0909@github.com/kura1528/converter.git
                git push origin main
                git commit -am "New JSON file"'''
            }
        }
    }
}

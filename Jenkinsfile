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
                #git config --global url.https://kura1528@github.com/.insteadOf https://github.com/
                git remote rm origin
                git remote add origin git@github.com:kura1528/converter.git
                git pull origin main
                git add output.json
                git commit -m "new json file created"
                git push -f origin :main'''
            }
        }
    }
}

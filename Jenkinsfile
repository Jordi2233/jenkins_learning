pipeline {
    agent {
        node {
            label 'docker-agent-python'
        }
    }
    triggers {
        pollSCM('H/2 * * * *')
    }
    stages {
        stage('Build') {
            steps {
                echo 'Building..'
                sh '''
                cd myapp/
                pi install -r requirements.tx
                '''
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
                sh '''
                cd myapp/
                python3 app.py
                python3 app.py --name=Błażej
                '''
            }
        }
        stage('Deliver') {
            steps {
                echo 'Deliver....'
                sh '''
                echo "doing delivery stuff.."
                '''
            }
        }
    }
}

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
                echo "Building.."
                sh '''
                python3 helloworld.py
                '''
            }
        }
        stage('Test') {
            steps {
                echo "Testing.."
                sh '''
                echo "doing test stuff.."
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
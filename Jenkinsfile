
pipeline {
    agent any

    stages {

        stage('Build') {
            steps {
                echo 'Building Student Grade Management System'
                bat 'python --version'
            }
        }

        stage('Test') {
            steps {
                echo 'Running Python Unit Tests'
                bat 'python -m unittest -v'
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker Image'
                bat 'docker build -t student-grade-app .'
            }
        }

        stage('Docker Run') {
            steps {
                echo 'Running Student Grade Management Container'

                bat '''
                docker rm -f student-grade-container 2>NUL
                docker run -dit --name student-grade-container student-grade-app
                docker inspect --format="{{.State.Status}}" student-grade-container
                '''
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: Build, Tests, Docker Build and Docker Run completed!'
        }

        failure {
            echo 'FAILED: Check Console Output.'
        }
    }
}

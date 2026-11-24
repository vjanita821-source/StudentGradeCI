
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
    }
}

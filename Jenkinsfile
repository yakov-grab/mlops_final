pipeline {
    agent any

    environment {
        JENKINS_HOME = "$JENKINS_HOME"
        BUILD = "${JENKINS_HOME}/workspace/mlops_final"
    }

    stages {
         stage('Start') {
            steps {
                script {
                    echo 'Начало работы скриптов.'
                }
            }
        }
        stage('Preparation') {
            steps {
                // Очистка рабочего пространства
                cleanWs()
                checkout scm
            }
        }

        stage('Checkout') {
            steps {
                script {
                    // Получаем исходный код из репозитория Git
                    git branch: 'main', url: 'https://github.com/lastinm/mlops_final.git'
                }
            }
        }

        stage('Path in JENKINS_HOME') {
            steps {
                script {
                    echo "Значение переменной JENKINS_HOME: ${env.JENKINS_HOME}"
                }
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    sh 'docker build -t titanic-disaster .'
                }
            }
        }

        stage('Finish') {
            steps {
                script {
                    echo 'Работа скриптов завершена успешно'
                }
            }
        }
    }
    post {
        always {
            // Очистка рабочего пространства после завершения
            cleanWs()
        }
    }
}
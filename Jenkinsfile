pipeline {
    agent any

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
            }
        }

        stage('Checkout') {
            steps {
                script {
                    // Получаем исходный код из репозитория Git
                    git 'https://github.com/lastinm/mlops_final.git'
                }
            }
        }

//         stage('Build Docker image') {
//             steps {
//                 script {
//                     // Jenkins при необходимости создаст каталог и переключит контекст
//                     // выполнения команд в нужный каталог
//                     dir(titanic-disaster) {
//                         sh 'docker build -t titanic-disaster .'
//                     }
//                 }
//             }
//         }

        stage('Finish') {
            steps {
                script {
                    echo 'Работа скриптов завершена успешно'
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
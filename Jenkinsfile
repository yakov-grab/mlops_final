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

        stage('Setup Virtual Environment') {
            steps {
                // Создание виртуального окружения
                script {
                    bat 'python -m venv venv'
                }
            }
        }

        stage('Activate venv') {
            steps {
                // Активация виртуального окружения
                script {
                    bat '.\\venv\\bin\\activate.bat'
                }
            }
        }

        stage('Install Dependencies') {
            steps {
                // установка зависимостей
                script {
                    bat 'pip install -r requirements.txt'
                }
            }
        }

        stage('Create model') {
            steps {
                script {
                    // Создаем и обучаем модель
                    // Вариант для Windows
                    bat 'python src\\create_model.py'
                }
            }
        }

        stage('Path in JENKINS_HOME') {
            steps {
                script {
                    def jenkinsHome = env.JENKINS_HOME
                    def jobName = env.JOB_NAME
                    def workspacePath = "${jenkinsHome}\\workspace\\${jobName}"
                    echo "Путь к проекту: ${workspacePath}"
                    def currentDirectory = env.WORKSPACE
                    echo "Current directory: ${currentDirectory}"
                }
            }
        }

        stage('Build Docker image') {
            steps {
                 script {
                    // Для Линукс
                    //sh 'docker build -t titanic-img .'
                    bat "docker build -t titanic-img -f Dockerfile ."
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
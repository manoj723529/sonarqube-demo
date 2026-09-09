pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install dependencies') {
            steps {
                sh 'pip3 install pytest --break-system-packages'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python3 -m pytest test_app.py'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('MySonarServer') {
                    script {
                        if (env.CHANGE_ID) {
                            sh """
                                ${tool 'SonarScanner'}/bin/sonar-scanner \
                                -Dsonar.projectKey=sonarqube-demo \
                                -Dsonar.pullrequest.key=${env.CHANGE_ID} \
                                -Dsonar.pullrequest.branch=${env.CHANGE_BRANCH} \
                                -Dsonar.pullrequest.base=${env.CHANGE_TARGET}
                            """
                        } else {
                            sh """
                                ${tool 'SonarScanner'}/bin/sonar-scanner \
                                -Dsonar.projectKey=sonarqube-demo \
                                -Dsonar.branch.name=${env.BRANCH_NAME}
                            """
                        }
                    }
                }
            }
        }
        stage('Quality Gate') {
            steps {
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}

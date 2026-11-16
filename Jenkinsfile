pipeline {
    agent any

    options {
        timestamps()
        timeout(time: 20, unit: 'MINUTES')
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Docker Tests') {
            steps {
                sh '''
                    docker compose -f docker-compose.test.yml up \
                        --build \
                        --abort-on-container-exit \
                        --exit-code-from tests
                '''
            }
        }
    }

    post {
        always {
            script {
                if (fileExists('reports/junit.xml')) {
                    junit testResults: 'reports/junit.xml'
                }

                if (fileExists('reports/coverage.xml')) {
                    archiveArtifacts artifacts: 'reports/coverage.xml'
                }
            }

            sh(
                returnStatus: true,
                script: 'docker compose -f docker-compose.test.yml down --remove-orphans'
            )
        }
    }
}

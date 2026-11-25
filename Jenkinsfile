
pipeline {
    agent any

    options {
        timestamps()
        timeout(time: 20, unit: 'MINUTES')
    }

    environment {
        IMAGE_NAME = 'support-app'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Gitleaks Security Scan') {
            steps {
                sh 'rm -rf security-reports'
                sh 'mkdir -p security-reports'
                sh 'test $(git rev-parse --is-shallow-repository) = false'
                sh 'gitleaks version'
                sh 'gitleaks git . --log-opts=--all --redact=100 --report-format json --report-path security-reports/gitleaks.json --exit-code 1'
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

        stage('Bandit Security Scan') {
            steps {
                sh 'bandit --version'
                sh 'bandit -r app/ -f json -o security-reports/bandit.json --exit-zero'
                sh 'bandit -r app/ -lll'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    env.IMAGE_TAG = env.GIT_COMMIT.take(7)
                }

                sh '''
                    docker build \
                        -t ${IMAGE_NAME}:${IMAGE_TAG} \
                        .
                '''

                echo "Built image: ${IMAGE_NAME}:${IMAGE_TAG}"
            }
        }
        stage('Trivy Image Scan') {
            steps {
                sh 'trivy --version'
                sh 'trivy image --severity HIGH,CRITICAL --format json --output security-reports/trivy.json --exit-code 0 ${IMAGE_NAME}:${IMAGE_TAG}'
                sh 'trivy image --severity HIGH,CRITICAL --ignore-unfixed --exit-code 1 ${IMAGE_NAME}:${IMAGE_TAG}'
            }
        }

    }

    post {
        always {
            archiveArtifacts artifacts: 'security-reports/*.json', allowEmptyArchive: true

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

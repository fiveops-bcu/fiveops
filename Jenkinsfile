
pipeline {
    agent any

    options {
        timestamps()
        timeout(time: 30, unit: 'MINUTES')
    }

    environment {
        IMAGE_NAME = 'support-app'
        GHCR_OWNER = 'fiveops-bcu'
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

        stage('Publish Docker Image to GHCR') {
            when {
                allOf {
                    branch 'main'
                    not {
                        changeRequest()
                    }
                }
            }
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'ghcr-publish',
                        usernameVariable: 'GHCR_USER',
                        passwordVariable: 'GHCR_TOKEN'
                    )
                ]) {
                    sh '''
                        set +x
                        set -e

                        IMAGE="ghcr.io/${GHCR_OWNER}/${IMAGE_NAME}:${IMAGE_TAG}"

                        trap 'docker logout ghcr.io >/dev/null 2>&1 || true' EXIT

                        echo "$GHCR_TOKEN" | docker login ghcr.io \
                            --username "$GHCR_USER" \
                            --password-stdin

                        docker tag ${IMAGE_NAME}:${IMAGE_TAG} "$IMAGE"
                        docker push "$IMAGE"

                        docker image inspect "$IMAGE" \
                            --format='{{range .RepoDigests}}{{println .}}{{end}}' \
                            | head -n 1 > security-reports/image-digest.txt

                        echo "Published image: $IMAGE"
                    '''

                    archiveArtifacts(
                        artifacts: 'security-reports/image-digest.txt',
                        fingerprint: true
                    )
                }
            }
        }

        stage('Deploy to TEST') {
            when {
                allOf {
                    branch 'main'
                    not {
                        changeRequest()
                    }
                }
            }
            steps {
                sshagent(credentials: ['ansible-test-ssh']) {
                    sh '''
                        set -e

                        ansible-playbook \
                            -i ansible/inventory/test \
                            ansible/playbooks/deploy.yml \
                            -e "app_image=ghcr.io/${GHCR_OWNER}/${IMAGE_NAME}:${IMAGE_TAG}"
                    '''
                }
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


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


        stage('Transfer Image to Test VM') {
            when {
                expression {
                    !env.CHANGE_ID &&
                    (env.BRANCH_NAME == 'main' ||
                     env.GIT_BRANCH == 'origin/main')
                }
            }
            steps {
                withCredentials([
                    sshUserPrivateKey(
                        credentialsId: 'fiveops-test-ssh',
                        keyFileVariable: 'SSH_KEY',
                        usernameVariable: 'SSH_USER'
                    )
                ]) {
                    sh '''#!/usr/bin/env bash
set -euo pipefail
docker save "${IMAGE_NAME}:${IMAGE_TAG}" | ssh \
  -i "$SSH_KEY" \
  -o IdentitiesOnly=yes \
  -o StrictHostKeyChecking=yes \
  -o BatchMode=yes \
  "$SSH_USER@192.168.174.129" 'docker load'
'''
                }
            }
        }


        stage('Deploy to Test VM') {
            when {
                expression {
                    !env.CHANGE_ID &&
                    (env.BRANCH_NAME == 'main' ||
                     env.GIT_BRANCH == 'origin/main')
                }
            }
            steps {
                withCredentials([
                    sshUserPrivateKey(
                        credentialsId: 'fiveops-test-ssh',
                        keyFileVariable: 'SSH_KEY',
                        usernameVariable: 'SSH_USER'
                    ),
                    string(
                        credentialsId: 'fiveops-test-vault-password',
                        variable: 'VAULT_PASSWORD'
                    ),
                    string(
                        credentialsId: 'fiveops-test-sudo-password',
                        variable: 'SUDO_PASSWORD'
                    )
                ]) {
                    sh '''#!/usr/bin/env bash
set -euo pipefail
set +x
umask 077

VAULT_FILE=$(mktemp)
SUDO_FILE=$(mktemp)
trap 'rm -f "$VAULT_FILE" "$SUDO_FILE"' EXIT

printf '%s\\n' "$VAULT_PASSWORD" > "$VAULT_FILE"
printf '%s\\n' "$SUDO_PASSWORD" > "$SUDO_FILE"

export ANSIBLE_HOST_KEY_CHECKING=True

ansible-playbook \
  -i /var/lib/jenkins/.config/fiveops/test.ini \
  ansible/playbooks/deploy.yml \
  --private-key "$SSH_KEY" \
  --vault-password-file "$VAULT_FILE" \
  --become-password-file "$SUDO_FILE" \
  -e @/var/lib/jenkins/.config/fiveops/test-secrets.yml \
  -e "app_image=${IMAGE_NAME}:${IMAGE_TAG}" \
  -e "app_version=${IMAGE_TAG}"
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

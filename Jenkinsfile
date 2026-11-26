
pipeline {
    agent any

    options {
        timestamps()
        timeout(time: 60, unit: 'MINUTES')
    }

    parameters {
        booleanParam(
            name: 'ENABLE_PRODUCTION_DEPLOY',
            defaultValue: false,
            description: 'Enable only after production acceptance'
        )
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

        // Diagnose the actual Jenkins execution environment
        stage('Check Gitleaks Environment') {
            steps {
                sh '''
                    echo "=== JENKINS ENVIRONMENT ==="
                    hostname
                    whoami
                    echo "PATH=$PATH"

                    echo "=== GITLEAKS LOCATION ==="
                    command -v gitleaks || true
                    ls -l /usr/local/bin/gitleaks || true

                    echo "=== GITLEAKS VERSION ==="
                    if [ -x /usr/local/bin/gitleaks ]; then
                        /usr/local/bin/gitleaks version
                    elif command -v gitleaks >/dev/null 2>&1; then
                        gitleaks version
                    else
                        echo "Gitleaks is not available in this Jenkins environment"
                    fi
                '''
            }
        }

        stage('Gitleaks Security Scan') {
            steps {
                sh 'rm -rf security-reports'
                sh 'mkdir -p security-reports'
                sh 'test "$(git rev-parse --is-shallow-repository)" = false'

                withEnv(['PATH+GITLEAKS=/usr/local/bin']) {
                    sh 'gitleaks version'

                    sh '''
                        gitleaks git . \
                            --log-opts=--all \
                            --redact=100 \
                            --report-format json \
                            --report-path security-reports/gitleaks.json \
                            --exit-code 1
                    '''
                }
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

                sh '''
                    bandit -r app/ \
                        -f json \
                        -o security-reports/bandit.json \
                        --exit-zero
                '''

                sh 'bandit -r app/ -lll'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    env.IMAGE_TAG = env.GIT_COMMIT.take(7)
                    env.GHCR_IMAGE = "ghcr.io/${env.GHCR_OWNER}/${env.IMAGE_NAME}:${env.IMAGE_TAG}"
                }

                sh '''
                    docker build \
                        -t "${IMAGE_NAME}:${IMAGE_TAG}" \
                        .
                '''

                echo "Built image: ${IMAGE_NAME}:${IMAGE_TAG}"
                echo "GHCR image: ${GHCR_IMAGE}"
            }
        }

        stage('Trivy Image Scan') {
            steps {
                sh 'trivy --version'

                sh '''
                    trivy image \
                        --severity HIGH,CRITICAL \
                        --format json \
                        --output security-reports/trivy.json \
                        --exit-code 0 \
                        "${IMAGE_NAME}:${IMAGE_TAG}"
                '''

                sh '''
                    trivy image \
                        --severity HIGH,CRITICAL \
                        --ignore-unfixed \
                        --exit-code 1 \
                        "${IMAGE_NAME}:${IMAGE_TAG}"
                '''
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
                        credentialsId: 'ghcr-push',
                        usernameVariable: 'GHCR_USER',
                        passwordVariable: 'GHCR_TOKEN'
                    )
                ]) {
                    sh '''
                        set -eu
                        set +x

                        export DOCKER_CONFIG="$(mktemp -d)"
                        trap 'docker logout ghcr.io >/dev/null 2>&1 || true; rm -rf "$DOCKER_CONFIG"' EXIT

                        printf '%s' "$GHCR_TOKEN" | docker login ghcr.io \
                            --username "$GHCR_USER" \
                            --password-stdin

                        docker tag \
                            "${IMAGE_NAME}:${IMAGE_TAG}" \
                            "$GHCR_IMAGE"

                        docker push "$GHCR_IMAGE"

                        docker image inspect "$GHCR_IMAGE" \
                            --format='{{range .RepoDigests}}{{println .}}{{end}}' \
                            | head -n 1 > security-reports/image-digest.txt

                        test -s security-reports/image-digest.txt
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
                            -u "$SSH_USER" \
                            --private-key "$SSH_KEY" \
                            --vault-password-file "$VAULT_FILE" \
                            --become-password-file "$SUDO_FILE" \
                            -e @/var/lib/jenkins/.config/fiveops/test-secrets.yml \
                            -e "app_image=${GHCR_IMAGE}" \
                            -e "app_version=${IMAGE_TAG}"
                    '''
                }
            }
        }

        stage('Production Approval') {
            when {
                allOf {
                    branch 'main'
                    expression {
                        params.ENABLE_PRODUCTION_DEPLOY
                    }
                    not {
                        changeRequest()
                    }
                }
            }

            steps {
                timeout(time: 30, unit: 'MINUTES') {
                    input(
                        message: "TEST deployment completed. Approve production deployment of ${GHCR_IMAGE}?",
                        ok: 'Approve Production Deployment'
                    )
                }
            }
        }

        stage('Deploy to PROD') {
            when {
                allOf {
                    branch 'main'
                    expression {
                        params.ENABLE_PRODUCTION_DEPLOY
                    }
                    not {
                        changeRequest()
                    }
                }
            }

            steps {
                sshagent(credentials: ['ansible-prod-ssh']) {
                    withCredentials([
                        file(
                            credentialsId: 'ansible-vault-prod',
                            variable: 'ANSIBLE_VAULT_FILE'
                        )
                    ]) {
                        sh '''
                            set -eu
                            set +x

                            export ANSIBLE_HOST_KEY_CHECKING=True

                            ansible-playbook \
                                -i ansible/inventory/prod/hosts.ini \
                                ansible/playbooks/deploy-prod.yml \
                                --vault-password-file "$ANSIBLE_VAULT_FILE" \
                                -e "app_image=${GHCR_IMAGE}"
                        '''
                    }
                }
            }
        }
    }

    post {
        always {
            archiveArtifacts(
                artifacts: 'security-reports/*.json,security-reports/*.txt',
                allowEmptyArchive: true
            )

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

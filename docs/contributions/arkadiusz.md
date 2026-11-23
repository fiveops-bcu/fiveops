## In progress

- Completing the Docker image build stage in the Jenkins CI/CD pipeline.
- Addressing review feedback on Pull Request #12.
- Updating the individual contribution documentation.
- Verifying the updated pipeline on the PR branch.
- Coordinating with the team on the remaining security and deployment requirements.

## Next steps

1. Address Yasin's requested changes on Pull Request #12.
2. Verify the Docker image build stage on the updated PR branch.
3. Update and commit the CI/CD documentation.
4. Request another review from the team leader.
5. Coordinate with Fadumo on security checks and Jenkins credentials.
6. Coordinate with Abdisalan on platform and deployment dependencies.
7. Continue integration of security scanning, image publishing and deployment stages.

## Blockers and dependencies

- Pull Request #12 requires further changes and another review before merging.
- The new Docker image build stage has not yet been verified by a successful Jenkins build on the PR branch.
- Security checks and credentials require coordination with Fadumo.
- Image publishing and deployment depend on the platform configuration and support from Abdisalan.

## Evidence

- Pull Request #1: requirements files review.
- Pull Request #12: Add Docker image build stage.
- Jenkins Build #2 on `main`: SUCCESS.
- Automated tests: 13 passed.
- PostgreSQL integration test: passed.
- Test coverage: 97.09%.
- Jenkins archived the coverage report and recorded JUnit test results.
- Docker-based test execution completed successfully using PostgreSQL 17.



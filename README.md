# ROMA 08 - GitHub Actions runner (I3)

Minimal smoke-test runner for ROMA 08. The repository is **currently public**. Use only non-sensitive test code here; make the repository private before using private project code or data.

- Trigger the workflow with a reviewed, immutable 40-character commit SHA and `python` or `typescript`.
- Tests run in GitHub-hosted Actions, without repository secrets and with read-only GITHUB_TOKEN.
- The runner uses fixed tests in the chosen commit, no arbitrary commands from Telegram/n8n messages.
- The n8n caller must have GitHub Actions write permission and must check both run ID and job steps before claiming a test passed.
- This runner is a smoke-test starting point, not a sandbox for hostile code or a production deploy environment.

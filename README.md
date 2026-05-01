# DevOps Dummy Python Project

Small project to test Redmineflux DevOps integration with GitHub Actions.

## Local run

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest -q
```

## Redmine issue linking

Use Redmine issue IDs in branch and commit messages, e.g.:

- Branch: `feature/123-ci-demo`ii
- Commit: `Fixes #123 add CI for dummy project`

This helps Redmineflux DevOps auto-link commits, PRs, builds, and deployments. This code is basically testing for redmineflux_devops plugin nothing else.
If you find any issue please raise an issue in github.
#thanks

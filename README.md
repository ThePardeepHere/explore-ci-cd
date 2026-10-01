# Basic Python CI/CD Demonstration

A simple Python project demonstrating the basics of CI/CD using GitHub Actions.

## Project Overview

This project contains a basic student result management application written in Python.

The main purpose of this project is to demonstrate:

- Git and GitHub
- Git branches
- Pull requests
- Automated testing with pytest
- GitHub Actions
- Continuous Integration (CI)
- Running tests automatically after code changes


## CI Workflow

This project uses GitHub Actions to automatically validate changes submitted through pull requests.

The CI workflow:

- Runs on pull requests targeting `main`
- Tests Python 3.10, 3.11, and 3.12
- Installs project dependencies
- Runs automated tests
- Checks Python syntax
- Runs the application

## Project Structure

```text
explore-ci-cd/
│
├── main.py
├── test_main.py
├── requirements.txt
└── .github/
    └── workflows/
        └── ci.yml
```
# DOC1 Dev Container - CI/CD for Spring Boot Applications

1. Open Visual Studio Code 
2. Use the command pallete(Ctrl + Shift + P): Click "Git:Clone..."
3. Paste the URL: https://github.com/viajook/devops-demo.git
4. Allow Visual Studio Code do the cloning, and then reopen in a dev container
5. Click to allow reopening in a dev container

## GitHub Actions CI

I added a GitHub Actions CI workflow to the project.

The workflow runs automatically when code is pushed to the "master" branch. It checks out the project code, sets up Java 21, and runs the Maven test command:

'mvn -B clean test'

The workflow completed successfully in the GitHub Actions tab.



## DevOps Assignment Overview

This repository contains a Spring Boot project used for DevOps practice.

For this assignment, I worked with:

- GitHub Actions CI for automatic build/test checks
- Maven for building and testing the Spring Boot project
- A serverless exercise folder named "my-serverless-app"
- Existing DevOps-related project files from earlier exercises

The CI workflow is located in:

'.github/workflows/ci.yml'

The workflow passed successfully in the GitHub Actions tab.



## DevContainer

This project also contains DevContainer files for running the development environment in a container.

The DevContainer setup helps make the development environment more consistent, because the required tools and configuration can be shared with the project instead of only being installed locally.

The DevContainer files are located in:

'.devcontainer/'

## Serverless Exercise

The repository also contains a serverless exercise folder:

'my-serverless-app/'

This folder was created as part of the DevOps assignment to practice basic serverless project structure and commands.

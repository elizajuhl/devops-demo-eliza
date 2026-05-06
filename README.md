# DOC1 Dev Container - CI/CD for Spring Boot Applications

1. Open Visual Studio Code 
2. Use the command pallete(Ctrl + Shift + P): Click "Git:Clone..."
3. Paste the URL: https://github.com/elizajuhl/devops-demo-eliza.git
4. Allow Visual Studio Code do the cloning, and then reopen in a dev container
5. Click to allow reopening in a dev container

## GitHub Actions CI

I added a GitHub Actions CI workflow to the project.

The workflow runs automatically when code is pushed to the "master" branch. It checks out the project code, sets up Java 21, and runs the Maven build/test command:

`mvn -B clean package`

The workflow completed successfully in the GitHub Actions tab.

The CI workflow also builds a Docker image using:

`docker build -t devops-demo-eliza:latest .`



## DevOps Assignment Overview

This repository contains a Spring Boot project used for DevOps practice.

For this assignment, I worked with:

- GitHub Actions CI for automatic build/test checks
- Maven for building and testing the Spring Boot project
- Docker image build in the CI workflow
- Kubernetes deployment and service files
- GitHub Actions CD workflow that deploys to Minikube
- A serverless exercise folder named `my-serverless-app`
- Existing DevOps-related project files from earlier exercises

The CI workflow is located in:

`.github/workflows/ci.yml`

The CD workflow is located in:

`.github/workflows/cd.yml`

The Kubernetes files are located in:

`k8s/deployment.yaml`  
`k8s/service.yaml`

Both the CI and CD workflows passed successfully in the GitHub Actions tab.



## DevContainer

This project also contains DevContainer files for running the development environment in a container.

The DevContainer setup helps make the development environment more consistent, because the required tools and configuration can be shared with the project instead of only being installed locally.

The DevContainer files are located in:

`.devcontainer/`

## Serverless Exercise

The repository also contains a serverless exercise folder:

`my-serverless-app/`

This folder was created as part of the DevOps assignment to practice basic serverless project structure and commands.

## How to Verify the DevOps Setup

1. Open the repository on GitHub.
2. Go to the **Actions** tab.
3. Check the workflows named **Java CI with Maven** and **Deploy to Minikube**.
4. The latest workflow run should show a green checkmark.
5. The workflow file can be found here:

`.github/workflows/ci.yml`

This confirms that GitHub Actions CI/CD is working for the project.


## Continuous Deployment to Minikube

I also added a CD workflow that deploys the application to a local Minikube Kubernetes cluster in GitHub Actions.

The CD workflow:

- builds the Spring Boot application with Maven
- builds the Docker image
- starts Minikube
- loads the Docker image into Minikube
- applies the Kubernetes deployment and service files from the `k8s/` folder
- shows the Kubernetes resources with `kubectl get all`

The CD workflow file is located here:

`.github/workflows/cd.yml`

The Kubernetes files are located here:

`k8s/deployment.yaml`  
`k8s/service.yaml`

Both the CI and CD workflows completed successfully in the GitHub Actions tab.
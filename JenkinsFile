pipeline {
  agent any

  environment {
    DOCKER_HUB_REPO = "imt2023030/calculator-cli"
    IMAGE_TAG = "${env.BUILD_NUMBER}"
    DOCKER_CREDS_ID = "dockerhub-creds"
  }

  stages {
    stage('Checkout') {
      steps {
        checkout scm
      }
    }

    stage('Setup & Test') {
      steps {
        sh """
          python3 -m venv .venv
          . .venv/bin/activate
          pip install --upgrade pip
          pip install -r requirements.txt
          pytest -q
        """
      }
    }

    stage('Build Docker Image') {
      steps {
        script {
          def imageName = "${env.DOCKER_HUB_REPO}:${env.IMAGE_TAG}"
          sh "docker build -t ${imageName} ."
          sh "docker images | grep ${env.DOCKER_HUB_REPO} || true"

          env.BUILT_IMAGE = imageName
        }
      }
    }

    stage('Push to Docker Hub') {
      steps {
        withCredentials([usernamePassword(credentialsId: env.DOCKER_CREDS_ID, usernameVariable: 'DH_USER', passwordVariable: 'DH_PASS')]) {
          sh """
            echo \$DH_PASS | docker login -u \$DH_USER --password-stdin
            docker push ${env.BUILT_IMAGE}
            docker logout
          """
        }
      }
    }
  }

  post {
    success {
      echo "Pipeline successful — image pushed: ${env.BUILT_IMAGE}"
    }
    failure {
      echo "Pipeline failed."
    }
  }
}

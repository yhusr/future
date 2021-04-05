pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'python run.py'
      }
    }

    stage('reporter') {
      steps {
        echo 'ok'
      }
    }

  }
}
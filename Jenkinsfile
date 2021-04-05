pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'python /root/.jenkins/jobs/future/run.py'
      }
    }

    stage('reporter') {
      steps {
        echo 'ok'
      }
    }

  }
}
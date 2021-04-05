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
            publishHTML (target: [
              allowMissing: false,
              alwaysLinkToLastBuild: false,
              keepAll: true,
              reportDir: 'reports',
              reportFiles: 'reporter*.html',
              reportName: "My Cool report"
            ])
          }
      }

  }
}

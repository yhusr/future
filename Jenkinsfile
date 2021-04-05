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
        publishHTML([
                        keepAll: true,
                        reportDir: 'reports',
                        reportFiles: 'reporter*.html',
                        reportName: "My Cool report"
                      ])
          sh 'System.setProperty("hudson.model.DirectoryBrowserSupport.CSP" , "")'
        }
      }

    }
  }

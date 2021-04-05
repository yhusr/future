pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        build(job: 'build', quietPeriod: 5)
      }
    }

    stage('test') {
      steps {
        sh '''#!/bin/bash
python /root/.jenkins/jobs/future/run.py'''
      }
    }

    stage('reporter') {
      steps {
        echo 'ok'
      }
    }

  }
}
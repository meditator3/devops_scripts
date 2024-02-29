pipeline {
  agent {
    node {
      label 'centos7'
    }
  triggers {
  pollSCM '* * * * *'
}
  }
  stages {
    stage('checkout Code') {
      steps {
        git(url: 'git@github.com:lidorg-dev/NodeJS-EmptySiteTemplate.git', branch: 'master', credentialsId: 'github-ssh', poll: true)
      }
    }

    stage('build') {
      steps {
        sh 'echo "Hello"'
      }
    }

  }
}

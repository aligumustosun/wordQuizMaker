pipeline {
  agent any

  stages {
    stage('dockerize') {
      steps {
	def dockerHome = tool 'myDocker'
        sh "${dockerHome} build . -t agt/wordquizmaker"
      }
    }
  }
}

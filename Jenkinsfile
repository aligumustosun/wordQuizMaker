pipeline {
  agent any

  tools {
    docker 'myDocker' 
  }  

   stages {
    stage('dockerize') {
      steps {	
	sh "docker build . -t agt/wordquizmaker"
      }
    }
  }
}

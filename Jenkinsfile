pipeline {
  agent any

  tools {
    org.jenkinsci.plugins.docker.commons.tools.DockerTool 'myDocker' 
  }  

   stages {
    stage('dockerize') {
      steps {	
	sh "docker build . -t agt/wordquizmaker"
      }
    }
  }
}

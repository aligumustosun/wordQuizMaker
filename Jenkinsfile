pipeline {
  agent any

   stages {
    stage('dockerize') {
      steps {	
	sh "docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD"
	sh "docker build . -t kbrssmsn/wordquizmaker"
	sh "docker push kbrssmsn/wordquizmaker"
      }
    }
  }
}

pipeline {
    agent any
    options {
        timestamps()
        timeout(time: 1, unit: 'HOURS')
        buildDiscarder(logRotator(artifactDaysToKeepStr: '7', artifactNumToKeepStr: '10', daysToKeepStr: '7', numToKeepStr: '50'))
    }
    environment {
        registry = "kishinskiy/myflask"
        registryCredential = 'dockerhub_id'
        dockerImage = ''
    }

    stages {
       stage("Building image") {
           steps{
               script{
                  docker.withRegistry( '', registryCredential ) {
                      def dockerImage = docker.build "kishinskiy/myflask:latest"
                      dockerImage.push()
                  }
               }
           }
       }
       stage("Start Docker-Compose") {
           steps{
                script{
                    sh "docker-compose up -d"
                }
           }
       }
    }


    post {
        always {
            sh "oc logout"
            cleanWs disableDeferredWipeout: true, deleteDirs: true
        }
    }
}

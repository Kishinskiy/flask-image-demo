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
        POSTGRES_DB="flask_db"
        PGDATA="/data/postgres"
        PORT="80"
        DEBUG="False"
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
                    try{
                         sh "docker-compose down"
                         sleep(time:10,unit:"SECONDS")
                    } catch (Exception e) {
                        echo 'Exception occurred: ' + e.toString()
                    }

                    withCredentials([
                        usernamePassword(credentialsId: 'postgres_id', usernameVariable: 'POSTGRES_USER', passwordVariable: 'POSTGRES_PASSWORD'),
                        string(credentialsId: 'database', variable: 'DB')
                        ]){
                        sh "docker-compose up -d"
                    }
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

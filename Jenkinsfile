pipeline {
    options {
        timestamps()
        timeout(time: 1, unit: 'HOURS')
        buildDiscarder(logRotator(artifactDaysToKeepStr: '7', artifactNumToKeepStr: '10', daysToKeepStr: '7', numToKeepStr: '50'))
    }

    stages {
       stage("Building image") {
           steps{
               script{
                  def dockerImage = docker.build "kishinskiy/myflask:${env.BUILD_TAG}"
                  dockerImage.push()
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

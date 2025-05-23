pipeline {
   agent any
   
   stages {
      stage('Build Docker image') {
          steps {
              script {
                   docker.build('flask-devops')
               }
            }
        }

      stage('Run Unit Test') {
         steps {
             script{
                  docker.image('flask-devops').inside {
                             sh 'python test_app.py'
                        }   
                     }
                }
          }


      stage('Run Docker Container') {
         steps {
             script {
                 docker.image ('flask-devops').run('-p 5001:5000')
               }
            }
         }
      }
   }            

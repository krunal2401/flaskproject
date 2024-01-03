pipeline{
    agent any
    environment {     
    DOCKERHUB_CREDENTIALS= credentials('dockerHub')     
  }    
        stages{
            stage('Clone code'){
                steps{
                    echo "git hub clone the code"    
                    git url:"https://github.com/krunal2401/flaskproject.git", branch: "main"
                }
                
            }
            stage('build'){
                steps{
                    echo "build the image"
                    sh "docker build -t flaskapp ."
                }
                
            }
            stage('push to docker hub'){
                steps{
                    echo "push to the docker hub"    
                    sh "docker tag flaskapp $DOCKERHUB_CREDENTIALS_USR/myflaskapp"
                    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'                 
	                echo 'Login Completed'
	                sh "docker push $DOCKERHUB_CREDENTIALS_USR/myflaskapp"
                }
                
            }
            stage('deploy'){
                steps{
                    echo "Deploy the code"    
                    sh "docker-compose down && docker-compose up -d"
                }
                
            }
        
        }
    }

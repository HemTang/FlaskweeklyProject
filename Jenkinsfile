pipeline{
   agent any 
   stages{
      stage("Building Images"){
        steps{
            echo "Building the IMgae from Dockerfile"
            sh 'docker-compose build'
        }
       }
      stage("Testing the Imgae"){
        steps{
            echo "Fake Testing the image"
          
        }
       }
      stage("Deploying the container"){
        steps{
            echo "Deploying the container in local VM"
            sh '''
            docker-compose down || true 
            docker-compose up -d
            '''
        }
       }
 }

post{
    success{
        echo "Deployment is successfull"

    }
    failure{

        echo "Something went wrong"

    }

}

 
}
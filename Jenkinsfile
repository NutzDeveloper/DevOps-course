pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                echo "Building docker image"
				sh 'docker build . -t pytest'
            }
        }
		stage ('Test') {
			steps {
				echo "Running the test"
				sh 'docker run -t pytest'
			}
		}
		}
		
		post
		{
			always 
			{
				echo "Pipeline ended"
				echo "Deleting image"
				sh 'docker image rm -f pytest'

			}
			
			failure 
			{
				echo "Pipeline failed"
			}
			
			success
			{
				echo "Pipeline succeeded"
			}
		}


    }

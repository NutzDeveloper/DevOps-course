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
		    agent {
        docker { image 'pytest' }
    }	
			steps {
				echo "Running the test"
				
			}
		}
		}
		
		post
		{
			always 
			{
				echo "Pipeline ended"

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

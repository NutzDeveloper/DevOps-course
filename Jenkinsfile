pipeline {
    agent {
        docker { image 'python:alpine' }
	}		
    stages {
		stage ('Preperation') {
			steps {

				echo "Installing Dependencies"
				sh 'PATH=${PATH}:/usr/local/bin'
				sh 'sudo pip install pytest'
			}
		}
		stage ('Test') {
			steps {
				echo "Running test"
				pytest app.py
				}
			}
	}
		
		post
		{
			always 
			{
				echo "Pipeline ended"
				echo "Deleting image"

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

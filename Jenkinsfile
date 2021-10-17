pipeline {
    agent {
        docker { image 'python:alpine' }
	}		
    stages {
		stage ('Preperation') {
			steps {

				echo "Installing Dependencies"
				
				sh 'pip install pytest --target $WORKSPACE --upgrade'
				sh 'python -m pytest'
			}
		}
		stage ('Test') {
			steps {
				echo "Running test"
				sh 'pytest app.py'
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

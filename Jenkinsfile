pipeline {
    agent {
        docker { image 'python:alpine' }
	}		
    stages {
		stage ('Preperation') {
			steps {

				echo "Installing Dependencies"
				sh 'pip3 --install --upgrade pip'
				sh 'pip3 install pytest --target $WORKSPACE --upgrade'			}
		}
		stage ('Test') {
			steps {
				echo "Running test"
				sh 'python -m pytest app.py'
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

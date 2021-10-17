pipeline {
    agent {
        docker { image 'python:alpine' }
	}		
    stages {
		stage ('Preperation') {
			steps {

			 withEnv(["HOME=${env.WORKSPACE}"]) {
				echo "Installing Dependencies"
				sh 'pip3 install pytest --upgrade'			}
				}
		}
		stage ('Test') {
			steps {
				echo "Running test"
				sh 'python -m pytest app.py'
				}
			}
		stage ('Kubernetes')
		{
			steps {
							kubeconfig(credentialsId: 'jenkins', serverUrl: 'http://192.168.186.156:6443') {
    // some block
	}
			}
		}
	}
		
		post
		{
			always 
			{
				echo " ======================= PIPELINE FINISHED ======================="
			}
			
			failure 
			{
				echo " ======================= PIPELINE FAILED ======================="
			}
			
			success
			{
				echo " ======================= PIPELINE SUCCESSFUL ======================="
			}
		}


    }

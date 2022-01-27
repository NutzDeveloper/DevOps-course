pipeline {
    agent {
        docker { image 'python:alpine' }
	}		
    stages {
		stage ('Preperation') {
			steps {

				echo "Installing Dependencies"
<<<<<<< HEAD
				sh 'pip3 install pytest --upgrade'			}
				}
=======
				sh 'pip3 install --upgrade pip'
				sh 'pip3 install pytest --target $WORKSPACE --upgrade'			}
>>>>>>> parent of 3c22349 (Update Jenkinsfile)
		}
		stage ('Test') {
			steps {
				echo "Running test"
				sh 'python -m pytest app.py'
				}
			}
		stage ('Kubernetes')
		{
			steps 
			{
				script 
				{
					kubernetesDeploy(configs: "test.yaml", kubeconfigId: "kubeconfig")
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

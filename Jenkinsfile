pipeline {
    agent {
        docker { image 'python:alpine' }
	}		
    stages {
		stage ('Preperation') {
			steps {

			 withEnv(["HOME=${env.WORKSPACE}"]) {
				echo "Installing Dependencies"
//				sh 'pip3 install --upgrade pip'
//				sh 'pip3 install pytest --target $WORKSPACE --upgrade'			
				sh 'pip3 install pytest --upgrade'			
				}
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

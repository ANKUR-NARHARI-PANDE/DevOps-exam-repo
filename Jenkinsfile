pipeline{
    agent any
    stages{
        stage("TF Init"){
            steps{
                echo "Executing Terraform Init"
                 sh"terraform init" 
            }
        }
        stage("TF Validate"){
            steps{
                echo "Validating Terraform Code"
                sh"terraform validate"
            }
        }
        stage("TF Plan"){
            steps{
                echo "Executing Terraform Plan"
                sh"terraform plan"
            }
        }
        stage('Install Dependencies') {
            steps {
                script {
                   
                   sh 'pip install requests --upgrade -t .'

                }
            }
        }
        stage("TF Apply"){
            steps{
                echo "Executing Terraform Apply"
                sh"terraform apply --auto-approve"
            }
        }
       stage('Invoke Lambda') {
    steps {
        script {
            def result = sh(script: 'aws lambda invoke --function-name my_lambda_function_new --log-type Tail output.txt', returnStdout: true)
            echo "Lambda output: ${result}"
           

        }
    }
}
    }
}

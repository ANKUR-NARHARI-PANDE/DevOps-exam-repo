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
        stage("TF Apply"){
            steps{
                echo "Executing Terraform Apply"
                sh"terraform apply --auto-approve"
            }
        }
       stage('Invoke Lambda') {
    steps {
        script {
            sh "aws lambda invoke --function-name my-lambda-function --payload '{\"subnet_id\":\"$(terraform output subnet_id)\",\"name\":\"Ankur Pande\",\"email\":\"ankurrpande@gmail.com}\' --log-type Tail"
           

        }
    }
}
    }
}

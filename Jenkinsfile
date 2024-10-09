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
            def result = sh(script: 'aws lambda invoke --function-name my_lambda_function_new --log-type Tail output.txt', returnStdout: true)
            echo "Lambda output: ${result}"
            echo "W0VSUk9SXSBSdW50aW1lLkltcG9ydE1vZHVsZUVycm9yOiBVbmFibGUgdG8gaW1wb3J0IG1vZHVsZSAnbGFtYmRhX2Z1bmN0aW9uJzogTm8gbW9kdWxlIG5hbWVkICdyZXF1ZXN0cycKVHJhY2ViYWNrIChtb3N0IHJlY2VudCBjYWxsIGxhc3QpOklOSVRfUkVQT1JUIEluaXQgRHVyYXRpb246IDEwNC45NCBtcwlQaGFzZTogaW5pdAlTdGF0dXM6IGVycm9yCUVycm9yIFR5cGU6IFJ1bnRpbWUuVW5rbm93bgpbRVJST1JdIFJ1bnRpbWUuSW1wb3Rtb2R1bGUjEZXJyb3I6IFVuYWJsZSB0b21wb3J0bW9kdWxlICdsYW1iZGFfZnVuY3Rpb24nOiBObyBtb2R1bGUgbmFtZWQgJ3JlcXVlc3RzJwpUcmFjZWJhY2sgKG1vc3QgcmVjZW50IGNhbGwgbGFzdCk6SU5JVF9SRVBPUlQgSW5pdCBEdXJhdGlvbjogMTM5My45OSBtcwlQaGFzZTogaW52b2tlCVN0YXR1czogZXJyb3IJRXJyb3IgVHlwZTogUnVudGltZS5Vbmtub3duClNUQVJUIFJlcXVlc3RJZDogN2I5N2IwOGQtZTJkNi00NThjLThlZDgtMDBkOTZmYjk0NjRjIFZlcnNpb246ICRMQVRFU1QKVW5rbm93biBhcHBsaWNhdGlvbiBlcnJvciBvY2N1cnJlZApSdW50aW1lLlVua25vd24KRU5EIFJlcXVlc3RJZDogN2I5N2IwOGQtZTJkNi00NThjLThlZDgtMDBkOTZmYjk0NjRjClJFUE9SVCBSZXF1ZXN0SWQ6IDdiOTdiMDhkLWUyZDYtNDU4Yy04ZWQ4LTAwZDk2ZmI5NDY0YwlEdXJhdGlvbjogMTQ1Mi41NSBtcwlCaWxsZWQgRHVyYXRpb246IDE0NTMgbXMJTWVtb3J5IFNpemU6IDEyOCBNQglNYXggTWVtb3J5IFVzZWQ6IDExIE1CCQo=" | base64 --decode

        }
    }
}
    }
}

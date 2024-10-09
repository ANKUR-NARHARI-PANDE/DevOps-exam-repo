provider "aws" {
  region = "ap-south-1"
}

resource "aws_subnet" "private_subnet" {
  vpc_id            = data.aws_vpc.vpc.id
  cidr_block        = "10.0.1.0/24"  # Change this as needed
  availability_zone = "ap-south-1a"

  tags = {
    Name = "MyPrivateSubnet"
  }
}

resource "aws_route_table" "private_route_table" {
  vpc_id = data.aws_vpc.selected.id

  tags = {
    Name = "MyPrivateRouteTable"
  }
}

resource "aws_security_group" "lambda_sg" {
  vpc_id = data.aws_vpc.selected.id

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
  }

  tags = {
    Name = "LambdaSecurityGroup"
  }
}

resource "aws_iam_role" "lambda_role" {
  name               = "MyLambdaRole"
  assume_role_policy = data.aws_iam_policy_document.lambda_assume_role_policy.json
}

data "aws_iam_policy_document" "lambda_assume_role_policy" {
  statement {
    actions = ["sts:AssumeRole"]
    principals {
      type        = "Service"
      identifiers = ["lambda.amazonaws.com"]
    }
  }
}

resource "aws_iam_policy_attachment" "lambda_policy_attachment" {
  name       = "MyLambdaPolicyAttachment"
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
  roles      = [aws_iam_role.lambda_role.name]
}

resource "aws_lambda_function" "my_lambda" {
  function_name = "my_lambda"
  role          = aws_iam_role.lambda_role.arn
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.8"

  s3_bucket     = "467.devops.candidate.exam"
  s3_key        = "Ankur.Pande.zip"

  environment {
    SUBNET_ID = aws_subnet.private_subnet.id
  }

  vpc_config {
    subnet_ids          = [aws_subnet.private_subnet.id]
    security_group_ids = [aws_security_group.lambda_sg.id]
  }
}

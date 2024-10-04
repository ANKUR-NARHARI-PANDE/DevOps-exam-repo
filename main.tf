







resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
   tags = {
      Name = "vpc"
    }
}

resource "aws_subnet" "private" {
  vpc_id     = data.aws_vpc.vpc.id
  cidr_block = "10.0.1.0/24"
  availability_zone = "ap-south-1a"

   tags = {
    Name = "private_subnet"
  }
}






# Routing Table for the Private Subnet
resource "aws_route_table" "private_route_table" {
  vpc_id = data.aws_vpc.vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = data.aws_nat_gateway.nat.id
  }

  tags = {
    Name = "private_route_table"
  }
}

# Associate Routing Table with Private Subnet
resource "aws_route_table_association" "private_route_association" {
  subnet_id      =aws_subnet.private.id
  route_table_id = aws_route_table.private_route_table.id
}
/*
# Security Group for Lambda
resource "aws_security_group" "lambda_sg" {
  vpc_id = data.aws_vpc.vpc.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "lambda_sg"
  }
}

/*# Lambda Function inside VPC using provided IAM role
resource "aws_lambda_function" "my_lambda" {
  filename         = "lambda_function_payload.zip"  # Make sure this file exists in your working directory
  function_name    = "my_lambda"
  role             = data.aws_iam_role.lambda_exec_role.arn
  handler          = "index.handler"
  runtime          = "nodejs18.x"  # Use your Lambda runtime

  vpc_config {
    subnet_ids         = [aws_subnet.private_subnet.id]
    security_group_ids = [aws_security_group.lambda_sg.id]
  }

  tags = {
    Name = "my_lambda_function"
}
}*/
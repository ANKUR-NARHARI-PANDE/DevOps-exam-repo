resource "aws_subnet" "private" {
  vpc_id     = data.aws_vpc.vpc.id
  cidr_block = "10.0.4.0/24"
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


resource "aws_route_table_association" "private_route_association" {
  subnet_id      =aws_subnet.private.id
  route_table_id = aws_route_table.private_route_table.id
}

resource "aws_lambda_function" "new" {
  function_name = "my_lambda_function_new"
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.8"
  role          = data.aws_iam_role.lambda.arn
  filename = "lambda_function.zip"




 
 environment {
    variables = {
        SUBNET_ID = aws_subnet.private.id
    }
}

}



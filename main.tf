



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

# Associate Routing Table with Private Subnet
resource "aws_route_table_association" "private_route_association" {
  subnet_id      =aws_subnet.private.id
  route_table_id = aws_route_table.private_route_table.id
}

/*resource "aws_security_group" "example" {
  name        = "my_lambda_security_group"
  description = "Security group for my Lambda function"
  vpc_id      = data.aws_vpc.vpc.id  # Make sure to use the correct VPC ID

  ingress {
    from_port   = 80               # Allow incoming traffic on port 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]    # Allow traffic from all IPs (adjust as needed)
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"             # Allow all outbound traffic
    cidr_blocks = ["0.0.0.0/0"]    # Allow traffic to all IPs
  }
}*/


resource "aws_lambda_function" "example" {
  function_name = "my_lambda_function"
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.8"
  role          = data.aws_iam_role.lambda.arn
  filename = "lambda_function.zip"

  /*vpc_config {
    subnet_ids          = [aws_subnet.private.id]
    security_group_ids  = [aws_security_group.example.id]
  }*/
}

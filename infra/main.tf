# Public S3 bucket
resource "aws_s3_bucket" "public_bucket" {
  bucket = "test-public-bucket"
  acl    = "public-read"
}

# Weak IAM Policy
resource "aws_iam_policy" "weak_policy" {
  name        = "weak-policy"
  description = "IAM policy with * permissions"
  policy      = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Effect   = "Allow"
      Action   = "*"
      Resource = "*"
    }]
  })
}

# IAM Policy - wildcard EC2 (HIGH)
resource "aws_iam_policy" "wild_ec2_policy" {
  name = "wild-ec2-policy"
  policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": "ec2:*",
      "Resource": "*"
    }
  ]
}
EOF
}

# Public write bucket (CRITICAL)
resource "aws_s3_bucket" "public_write_bucket" {
  bucket = "public-write-bucket"
  acl    = "public-read-write"
}


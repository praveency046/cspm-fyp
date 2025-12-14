resource "aws_s3_bucket" "public_bucket" {
  bucket = "test-public-bucket"
}

resource "aws_s3_bucket_acl" "public_bucket_acl" {
  bucket = aws_s3_bucket.public_bucket.id
  acl    = "public-read"
}

resource "aws_s3_bucket" "public_write_bucket" {
  bucket = "public-write-bucket"
}

resource "aws_s3_bucket_acl" "public_write_bucket_acl" {
  bucket = aws_s3_bucket.public_write_bucket.id
  acl    = "public-read-write"
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



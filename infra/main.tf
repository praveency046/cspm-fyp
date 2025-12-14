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

import boto3

LOCALSTACK_ENDPOINT = "http://localhost:4566"
REGION = "us-east-1"

def get_client(service_name):
    return boto3.client(
        service_name,
        endpoint_url=LOCALSTACK_ENDPOINT,
        aws_access_key_id="test",
        aws_secret_access_key="test",
        region_name=REGION
    )

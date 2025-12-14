from aws_client import get_client

def test_s3():
    s3 = get_client("s3")
    buckets = s3.list_buckets()
    print("[+] S3 Buckets:")
    for b in buckets["Buckets"]:
        print(" -", b["Name"])

def test_iam():
    iam = get_client("iam")
    policies = iam.list_policies(Scope="Local")
    print("\n[+] IAM Policies:")
    for p in policies["Policies"]:
        print(" -", p["PolicyName"])

if __name__ == "__main__":
    test_s3()
    test_iam()

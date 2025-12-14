from aws_client import get_client

def check_public_buckets():
    findings = []
    s3 = get_client("s3")
    buckets = s3.list_buckets()["Buckets"]

    for bucket in buckets:
        name = bucket["Name"]
        try:
            acl = s3.get_bucket_acl(Bucket=name)
            for grant in acl["Grants"]:
                grantee = grant.get("Grantee", {})
                if grantee.get("URI") == "http://acs.amazonaws.com/groups/global/AllUsers":
                    findings.append({
                        "resource": name,
                        "service": "S3",
                        "issue": "Public S3 Bucket",
                        "severity": "HIGH"
                    })
        except Exception:
            pass

    return findings

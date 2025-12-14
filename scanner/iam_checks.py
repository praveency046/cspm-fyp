from aws_client import get_client
import json

def check_wildcard_policies():
    findings = []
    iam = get_client("iam")
    policies = iam.list_policies(Scope="Local")["Policies"]

    for policy in policies:
        version = iam.get_policy(PolicyArn=policy["Arn"])["Policy"]["DefaultVersionId"]
        doc = iam.get_policy_version(
            PolicyArn=policy["Arn"],
            VersionId=version
        )["PolicyVersion"]["Document"]

        for stmt in doc["Statement"]:
            if stmt["Action"] == "*" or stmt["Resource"] == "*":
                findings.append({
                    "resource": policy["PolicyName"],
                    "service": "IAM",
                    "issue": "Wildcard permissions",
                    "severity": "CRITICAL"
                })

    return findings

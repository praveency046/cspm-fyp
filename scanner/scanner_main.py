from s3_checks import check_public_buckets
from iam_checks import check_wildcard_policies
from report_writer import write_report

def main():
    findings = []
    findings.extend(check_public_buckets())
    findings.extend(check_wildcard_policies())
    write_report(findings)

if __name__ == "__main__":
    main()

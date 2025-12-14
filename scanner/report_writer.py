import json
from datetime import datetime

def write_report(findings):
    report = {
        "scan_time": datetime.utcnow().isoformat(),
        "total_findings": len(findings),
        "findings": findings
    }

    with open("../reports/cspm_report.json", "w") as f:
        json.dump(report, f, indent=4)

    print("[+] Report written to reports/cspm_report.json")

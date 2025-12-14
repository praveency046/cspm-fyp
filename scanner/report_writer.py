import json
import os
from datetime import datetime

def write_report(findings):
    report = {
        "scan_time": datetime.utcnow().isoformat(),
        "total_findings": len(findings),
        "findings": findings
    }

    # Always write relative to scanner directory
    reports_dir = os.path.join(os.getcwd(), "reports")
    os.makedirs(reports_dir, exist_ok=True)

    report_path = os.path.join(reports_dir, "cspm_report.json")

    with open(report_path, "w") as f:
        json.dump(report, f, indent=4)

    print(f"[+] Report written to {report_path}")

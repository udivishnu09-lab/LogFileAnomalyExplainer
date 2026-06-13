def generate_report(issue, explanation):

    report = f"""
# Log File Analysis Report

## Issue
{issue}

## Analysis
{explanation}

-------------------------------------
"""

    with open("reports/report.md", "a") as file:
        file.write(report)
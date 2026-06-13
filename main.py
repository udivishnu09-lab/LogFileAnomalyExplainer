from parser import find_errors
from explainer import explain_issue
from report import generate_report

issues = find_errors("sample.log")

for item in issues:

    explanation = explain_issue(
        item["issue"],
        item["context"]
    )

    generate_report(
        item["issue"],
        explanation
    )

print("Report Generated Successfully!")
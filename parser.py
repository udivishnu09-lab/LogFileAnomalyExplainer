def find_errors(log_file):
    with open(log_file, "r") as f:
        lines = f.readlines()

    issues = []

    for i, line in enumerate(lines):
        if "ERROR" in line or "WARNING" in line:
            start = max(0, i - 2)
            end = min(len(lines), i + 3)

            context = "".join(lines[start:end])

            issues.append({
                "issue": line.strip(),
                "context": context
            })

    return issues
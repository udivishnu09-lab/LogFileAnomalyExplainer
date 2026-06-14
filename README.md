# Log File Anomaly Explainer

## Project Overview

Log File Anomaly Explainer is an AI-powered tool that analyzes log files and automatically explains errors and warnings. The system identifies anomalies from log files, extracts relevant context, and uses a Large Language Model (LLM) through Ollama to generate probable causes and suggested fixes.

---

## Problem Statement

Production support engineers often need to analyze hundreds of log lines to identify the root cause of system failures. This process is time-consuming and requires manual investigation.

This project automates log analysis by detecting error blocks and generating AI-powered explanations.

---

## Features

* Reads log files (.log)
* Detects ERROR and WARNING entries
* Extracts surrounding log context
* Uses Ollama (Llama 3.2) for analysis
* Generates a Markdown report
* Provides probable causes and suggested fixes

---

## Project Structure

LogFileAnomalyExplainer/

├── parser.py

├── explainer.py

├── report.py

├── main.py

├── sample.log

├── README.md

├── logs/

└── reports/

```
└── report.md
```

---

## Architecture

Input Log File (.log)

↓

Log Parser

↓

Error & Warning Detection

↓

Context Extraction

↓

LLM Analysis (Ollama - Llama 3.2)

↓

Markdown Report Generation

↓

report.md

---

## Setup Instructions

1. Install Python 3.x
2. Install Ollama
3. Download the model

ollama run llama3.2

4. Install dependencies

pip install ollama

---

## Run Instructions

Run the application using:

python main.py

---

## Input

A log file containing application or system logs.

Example:

INFO Server Started

ERROR Database Connection Timeout

WARNING High Memory Usage

INFO Service Stopped

---

## Output

The system generates:

reports/report.md

The report contains:

* Detected Issue
* Probable Root Cause
* Suggested Fix

---

## Assumptions

* Log files contain ERROR or WARNING entries.
* Ollama is running locally.
* The LLM model is available on the system.

---

## Limitations

* Only detects predefined error patterns.
* Analysis quality depends on the LLM response.
* Works on text-based log files.

---

## Future Enhancements

* Support multiple log formats
* Web-based user interface
* Real-time log monitoring
* Advanced anomaly detection using machine learning

---

## Conclusion

The Log File Anomaly Explainer simplifies production support tasks by automatically detecting issues in log files and generating AI-powered explanations, reducing manual troubleshooting effort and improving efficiency.




#DEMO LINK
https://drive.google.com/file/d/1W6LUSFbZe7Qs-1tTnQuH4tWAp2AqRx4R/view?usp=sharing




from ollama import chat

def explain_issue(issue, context):

    prompt = f"""
You are a Production Support Engineer.

Issue:
{issue}

Context:
{context}

Please provide:
1. Probable Root Cause
2. Suggested Fix
"""

    response = chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]
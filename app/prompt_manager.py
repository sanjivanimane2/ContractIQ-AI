PROMPTS = {

    "v2": {
        "classifier": """You are a legal AI assistant.

Task:
Classify the document into:
MSA, SOW, NDA, PO, Invoice

Rules:
- Return only one value
- No explanation

Document:
{text}
""",

        "clauses": """You are an expert legal analyzer.

Task:
Extract clauses.

Output JSON:
[
  {
    "clause_name": "",
    "clause_text": ""
  }
]

Rules:
- No extra text
- No duplication

Document:
{text}
""",

        "attributes": """You are a legal contract intelligence system.

### Example:
Text:
"This Agreement is effective from Jan 1, 2024 between ABC Corp and XYZ Ltd governed by laws of Delaware."

Output:
{
  "effective_date": "2024-01-01",
  "parties": ["ABC Corp", "XYZ Ltd"],
  "governing_law": "Delaware",
  "payment_terms": "Not Found",
  "termination": "Not Found"
}

---

Task:
Extract attributes.

Output JSON:
{
  "effective_date": "",
  "parties": [],
  "governing_law": "",
  "payment_terms": "",
  "termination": ""
}

Rules:
- Do NOT hallucinate
- If not found → "Not Found"

Document:
{text}
"""
    }
}

CURRENT_VERSION = "v2"

def get_prompt(prompt_type, text):
    template = PROMPTS[CURRENT_VERSION][prompt_type]
    return template.replace("{text}", text[:3000])

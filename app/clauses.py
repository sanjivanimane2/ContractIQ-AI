from app.llm import call_llm
from app.prompt_manager import get_prompt
import json

def extract_clauses(text):
    prompt = get_prompt("clauses", text)
    result = call_llm(prompt)

    try:
        return json.loads(result)
    except:
        return []

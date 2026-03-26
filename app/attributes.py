from app.llm import call_llm
from app.prompt_manager import get_prompt
import json

def extract_attributes(text):
    prompt = get_prompt("attributes", text)
    result = call_llm(prompt)

    try:
        return json.loads(result)
    except:
        return {}

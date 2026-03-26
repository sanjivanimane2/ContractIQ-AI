from app.llm import call_llm
from app.prompt_manager import get_prompt

def classify_document(text):
    prompt = get_prompt("classifier", text)
    return call_llm(prompt)

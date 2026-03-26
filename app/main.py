from fastapi import FastAPI, UploadFile
from app.azure_blob import upload_file
from app.azure_ocr import extract_text
from app.azure_search import upload_document, search_documents

from app.classifier import classify_document
from app.clauses import extract_clauses
from app.attributes import extract_attributes
from app.prompt_manager import CURRENT_VERSION

app = FastAPI()

@app.get("/")
def home():
    return {"message": "ContractIQ AI Running 🚀"}

@app.post("/process")
async def process(file: UploadFile):
    blob_url = upload_file(await file.read(), file.filename)
    text = extract_text(blob_url)

    doc_type = classify_document(text)
    clauses = extract_clauses(text)
    attributes = extract_attributes(text)

    doc = {
        "id": file.filename,
        "content": text,
        "doc_type": doc_type,
        "attributes": str(attributes)
    }

    upload_document(doc)

    return {
        "document_type": doc_type,
        "clauses": clauses,
        "attributes": attributes,
        "prompt_version": CURRENT_VERSION
    }

@app.get("/ask")
def ask(query: str):
    results = search_documents(query)
    return {"results": results}

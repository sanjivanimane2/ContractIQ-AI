from azure.ai.formrecognizer import DocumentAnalysisClient
from azure.core.credentials import AzureKeyCredential
import os

client = DocumentAnalysisClient(
    endpoint=os.getenv("FORM_RECOGNIZER_ENDPOINT"),
    credential=AzureKeyCredential(os.getenv("FORM_RECOGNIZER_KEY"))
)

def extract_text(blob_url):
    poller = client.begin_analyze_document_from_url(
        "prebuilt-document", blob_url
    )
    result = poller.result()

    text = ""
    for page in result.pages:
        for line in page.lines:
            text += line.content + "\n"

    return text

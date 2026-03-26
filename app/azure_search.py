from azure.search.documents import SearchClient
from azure.core.credentials import AzureKeyCredential
import os

search_client = SearchClient(
    endpoint=os.getenv("SEARCH_ENDPOINT"),
    index_name=os.getenv("SEARCH_INDEX"),
    credential=AzureKeyCredential(os.getenv("SEARCH_KEY"))
)

def upload_document(doc):
    search_client.upload_documents([doc])

def search_documents(query):
    results = search_client.search(query)
    return [r["content"] for r in results]

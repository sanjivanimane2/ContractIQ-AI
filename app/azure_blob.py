from azure.storage.blob import BlobServiceClient
import os

blob_service = BlobServiceClient.from_connection_string(
    os.getenv("BLOB_CONNECTION_STRING")
)

def upload_file(file, filename):
    blob_client = blob_service.get_blob_client(
        container="contracts",
        blob=filename
    )
    blob_client.upload_blob(file, overwrite=True)
    return blob_client.url

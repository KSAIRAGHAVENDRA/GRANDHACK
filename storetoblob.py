from azure.storage.blob import BlobServiceClient


def main(file_path):
    container_name  = "input"

    # file_name = file_path.split('/')
    # file_name = file_name[len(file_name) - 1]
    file_name = "image1"
    account_name = "mockupcode"
    account_name = account_name.strip()
    account_key = "YOUR_ACCOUNT_KEY"
    account_key = account_key.strip()

    connect_str = "DefaultEndpointsProtocol=https;AccountName=mockupcode;AccountKey=YOUR_ACCOUNT_KEY;EndpointSuffix=core.windows.net"
    blob_service_client = BlobServiceClient.from_connection_string(connect_str)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

    with open(file_path, "rb") as data:
        blob_client.upload_blob(data)
    return "done"

main()

import pandas as pd

# Import necessary libraries
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os
from secret import azure_key

connect_str = azure_key

blob_container_client = ContainerClient.from_connection_string(connect_str, container_name='mto-jcm-etops')

# count blobs in the container
blobs_list = blob_container_client.list_blobs()
# count = 0
# for blob in blobs_list:
#     count += 1
# print(f"Number of blobs in the container: {count}")
df = pd.DataFrame(columns=['name', 'size', 'last_modified', 'content_type', 'blob_type'])
for blob in blobs_list:
    df = df._append({'name': blob.name, 'size': blob.size, 'last_modified': blob.last_modified, 'content_type': blob.content_settings.content_type, 'blob_type': blob.blob_type}, ignore_index=True)
    # print(f"Blob name: {blob.name}")
    # print(f"Blob size: {blob.size} bytes")
    # print(f"Blob last modified: {blob.last_modified}")
    # print(f"Blob content type: {blob.content_settings.content_type}")
    # print(f"Blob type: {blob.blob_type}")
    # print("-" * 40)
    # if blob.content_settings.content_type != 'application/pdf':
    #     break

# save the dataframe to a csv file
df.to_csv('blobs_list.csv', index=False)
# export blobs list to csv




# "EM/_ADL01/01_General Part 1-Miscellaneous_2021-09-24/35193_190386_General_Part_1-Miscellaneous.pdf"



blob_service_client = BlobServiceClient.from_connection_string(connect_str)
# List all containers in the storage account
#containers = blob_service_client.list_containers()
# for container in containers:
#     print(f"Container name: {container['name']}")
#     print(f"Container last modified: {container['last_modified']}")
#     print(f"Container lease state: {container['lease']['state']}")
#     print(f"Container lease status: {container['lease']['status']}")
#     print(f"Container metadata: {container['metadata']}")
#     print("-" * 40)


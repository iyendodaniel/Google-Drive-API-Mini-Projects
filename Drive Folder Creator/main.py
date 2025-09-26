import os
import pickle
import googleapiclient.discovery
import google.auth.transport.requests 
import google.oauth2.credentials
from googleapiclient.discovery import build


file_path = "token.pickle"

if os.path.exists(file_path):
    with open(file_path, "rb") as token_file:
        credentials = pickle.load(token_file)
else:
    print("Error!Token file does not exist.")
    exit()

service = build("drive", "v3", credentials=credentials)

folder_name = input("Enter the name of the folder you wanna create: ").strip()

metadata = {
    "name": folder_name,
    "mimeType": "application/vnd.google-apps.folder"
}
folder = service.files().create(body = metadata, fields = "id").execute()

print(f"Folder has been successfully created, Here's is the folder ID: {folder["id"]}.")
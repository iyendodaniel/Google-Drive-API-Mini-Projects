import os
import pickle 
import google_auth_oauthlib.flow
import google.auth.transport.requests
import google.oauth2.credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

file_path = "token.pickle"
client_secret_file = "client_secret.json"
SCOPES = ["https://www.googleapis.com/auth/drive.file"]

if os.path.exists(file_path):
    with open(file_path, "rb") as token_file:
        credentials = pickle.load(token_file)
else:
    credentials = None

if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        credentials.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file(client_secret_file, SCOPES)
        credentials = flow.run_local_server(port=0)


    with open(file_path, "wb") as token_file:
          pickle.dump(credentials, token_file)

    print("Authentication successful. Credentials saveed!")
else:
    print("Already authenticated!")
# Drive Folder Creator

This is a terminal-based Python script that lets you create a folder in your Google Drive using the Google Drive API.

## Features
- Authenticates using a `token.pickle` file
- Connects to Google Drive with the `drive v3` API
- Prompts the user for a folder name
- Creates the folder in the root of your Drive
- Prints the folder ID after creation

## Requirements
- `token.pickle` file (generated after authenticating with Google)
- Python 3.x
- Required libraries:
  pip install --upgrade google-api-python-client google-auth google-auth-oauthlib

## Usage
- Make sure token.pickle exists in the same directory.
- Run the script:
  python drive_folder_creator.py
- Enter the folder name when prompted.
- The script will create the folder and print its Google Drive ID.

## Note
The script assumes you've already completed OAuth authentication and saved credentials as token.pickle.
If you don’t have token.pickle, run the Google Drive API Authenticator project first.

## Output Example
- Enter the name of the folder you wanna create: ProjectX
- Folder has been successfully created! Here's the folder ID: 1a2B3c4D5eF6GhIjK

## Related Projects
✅ Token Manager
✅ Credentials Saver
✅ Google Drive API Authenticator
✅ Access Token Refresher
✅ Drive Folder Creator ← you are here
🔜 Final Project: Terminal-Based Google Drive Uploader

---

Made by Iyendo Daniel Okeoghene
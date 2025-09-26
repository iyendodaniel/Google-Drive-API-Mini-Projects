# Google Drive API Authenticator 🛡️

This mini project handles the **authentication flow** for accessing the Google Drive API using OAuth 2.0.

## 🔍 What it Does
- Authenticates a user via the browser using Google's OAuth system.
- Saves the user's credentials securely to a `token.pickle` file.
- Supports refreshing expired tokens using the refresh token.
- Skips login if valid credentials already exist.

## 📁 Files Used
- `client_secret.json`: Your Google API credentials file downloaded from Google Cloud Console.
- `token.pickle`: The saved user credentials (access + refresh tokens).

## ⚙️ Requirements
- Python 3
- Google API libraries:
pip install --upgrade google-auth google-auth-oauthlib google-auth-httplib2

## How it Works
1. First run: Opens a browser window for you to sign in with your Google account.
2. Next runs: Reuses the saved token.pickle if still valid.
3. If token expired: Automatically refreshes it using the refresh token.
4. If no token or refresh fails: Runs the full login flow again.

---

Made by Iyendo Daniel Okeoghene
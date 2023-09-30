# python-flask-oauth

App is Flask Google OAuth App

This Flask application demonstrates the OAuth2.0 authentication flow using Google as the OAuth provider.

![application](images/app.png)

## Setup

1. Make sure you have Python and `pip` installed.

2. Install the necessary Python packages:
   ```bash
   pip install -r requirements.txt
    ```

3. Go to the Google Cloud Console and Create a new project / choose existing project. Navigate to the "OAuth consent screen" and configure the consent screen.

Go to "Credentials", click on "Create Credentials" and choose "OAuth 2.0 Client IDs".
Choose "Web application" as the application type.
Provide a name and under "Authorized redirect URIs", add http://localhost:5000/login/callback. Adjust the URI as needed.
Save. You'll get a client ID and client secret. Note them down.


Diagram as a code

https://www.planttext.com/


```bash

@startuml
participant "User's Browser" as User
participant "Flask App" as Flask
participant "Google OAuth" as Google

User -> Flask: Access application homepage
Flask -> User: Show "Login with Gmail" link

User -> Flask: Click "Login with Gmail"
Flask -> Google: Redirect to Google's authorization endpoint
Google -> User: Show Google login and consent screen

User -> Google: Enter credentials and approve
Google -> Flask: Redirect to /login/callback with authorization code
Flask -> Google: Exchange authorization code for access token
Google -> Flask: Return access token

Flask -> Google: Request user info with access token
Google -> Flask: Return user's email and other data
Flask -> User: Display logged in state

@enduml

```
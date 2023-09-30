from flask import Flask, redirect, url_for, session
from flask_oauthlib.client import OAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = 'random_secret_key'  # Change this
oauth = OAuth(app)

google = oauth.remote_app(
    'google',
    consumer_key='YOUR_CLIENT_ID',
    consumer_secret='YOUR_CLIENT_SECRET',
    request_token_params={
        'scope': 'email',
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth',
)

@app.route('/')
def index():
    return 'Welcome! <a href="/login">Login with Gmail</a>'

@app.route('/login')
def login():
    return google.authorize(callback=url_for('callback', _external=True))

@app.route('/login/callback')
def callback():
    response = google.authorized_response()
    if response is None or response.get('access_token') is None:
        return 'Access denied: reason={} error={}'.format(
            request.args['error_reason'],
            request.args['error_description']
        )
    session['google_token'] = (response['access_token'], '')
    user_info = google.get('userinfo')
    return f"Logged in as: {user_info.data['email']}"

@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')

if __name__ == '__main__':
    app.run(debug=True)

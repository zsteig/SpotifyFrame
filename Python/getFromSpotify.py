import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Credentials
SPOTIPY_CLIENT_ID = 'f5ced38914b8408fb24b35245cf8937c'
SPOTIPY_CLIENT_SECRET = 'cfbb0c4e19f54901af6af4ee5d0aea25'
SPOTIPY_REDIRECT_URI = 'http://localhost/redirect'
USERNAME = 'steigerwald.zachary'
SCOPE = "user-read-currently-playing"

def getFromSpotify():
    auth = SpotifyOAuth(client_id=SPOTIPY_CLIENT_ID,
                        client_secret=SPOTIPY_CLIENT_SECRET,
                        redirect_uri=SPOTIPY_REDIRECT_URI,
                        username=USERNAME,
                        scope=SCOPE,
                        open_browser=False)

    token = auth.get_cached_token()

    if token and auth.is_token_expired(token):
        token = auth.refresh_access_token(token['refresh_token'])

    sp = spotipy.Spotify(auth_manager=auth)
    result = sp.current_user_playing_track()

    if result is None:
        print("No song playing")
        return None
    else:
        imageURL = result['item']['album']['images'][0]['url']
        artist = result['item']['artists'][0]['name']
        song = result['item']['name']
        return [imageURL, artist, song]

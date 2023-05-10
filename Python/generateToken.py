import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth

if len(sys.argv) > 1:
    username = sys.argv[1]
    scope = 'user-read-currently-playing'

    auth = SpotifyOAuth(scope=scope, open_browser=False)
    token = auth.get_access_token()
import logging
import spotipy
import requests
from io import BytesIO
from PIL import Image

def getFromSpotify(username, token_path):
    scope = 'user-read-currently-playing'
    token = spotipy.util.prompt_for_user_token(username, scope, cache_path=token_path)

    if token:
        sp = spotipy.Spotify(auth=token)
        result = sp.current_user_playing_track()

        if result is None:
            print("No song playing")
        else:
            song = result['item']['name']
            artist = result['item']['artists']['name']
            imageURL = result['item']['album']['images'][0]['url']
            return [song, artist, imageURL]
    else:
        print("can't get token for: ", username)
        return None
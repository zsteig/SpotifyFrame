import time
import sys
import logging
from logging.handlers import RotatingFileHandler
from getFromSpotify import getFromSpotify
import requests
from io import BytesIO
from PIL import Image
import sys, os
import urllib.request
from displayUpdate import DisplayWindow

if __name__ == "__main__":
    if len(sys.argv) > 2:
        username = sys.argv[1]
        token_path = sys.argv[2]

        # Configure logger
        logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='spotipy.log',level=logging.INFO)
        logger = logging.getLogger('spotipy_logger')

        # Auto delete logs larger than 2KB
        handler = RotatingFileHandler('spotipy.log', maxBytes=2048, backupCount=3)
        logger.addHandler(handler)

        # Show default image
        display = DisplayWindow()

        prevSong = ""
        currSong = ""
        try:
            while True:
                try:
                    imageURL = getFromSpotify(username, token_path)[1]
                    albumCoverArt = os.path.join(dir, 'client/album_cover.png')
                    urllib.request.urlretrieve(imageURL, albumCoverArt)
                    songName = getFromSpotify(username, token_path)[0]
                    artistName = getFromSpotify(username, token_path)[2]
                    currSong = imageURL

                    if (prevSong != currSong):
                        response = requests.get(imageURL)
                        image = Image.open(BytesIO(response.content))
                        prevSong = currSong
                    
                    # Update displayed song info
                    display.update_image(image)
                    display.update_text(songName, artistName)

                except Exception as e:
                    print(e)
                    time.sleep(1)
        except KeyboardInterrupt:
            sys.exit(0)
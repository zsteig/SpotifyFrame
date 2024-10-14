import time
import sys
import logging
from logging.handlers import RotatingFileHandler
from getFromSpotify import getFromSpotify
import requests
import sys, os
import urllib.request
from displayUpdate import DisplayWindow
import pyglet

def update_display(display, prevSong):
    try:
        spotify_response = getFromSpotify()
        if spotify_response is None:
            logo = "../Assets/Spotify-Logo-PNG.png"
            display.update_image(logo)
            display.update_text("", "Not Currently Playing")
        else:
            imageURL, artistName, songName = spotify_response
            currSong = songName
            if prevSong != currSong:
                prevSong = currSong
                # Update displayed song info
                display.update_image(imageURL)
                display.update_text(songName, artistName)
        # Schedule the next update
        display.window.after(5000, update_display, display, prevSong)
    except Exception as e:
        print(e)
        display.window.after(1000, update_display, display, prevSong)

if __name__ == "__main__":
    # Configure logger
    logging.basicConfig(format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', filename='spotipy.log', level=logging.INFO)
    logger = logging.getLogger('spotipy_logger')
    # Auto delete logs larger than 2KB
    handler = RotatingFileHandler('spotipy.log', maxBytes=2048, backupCount=3)
    logger.addHandler(handler)
    # Add font
    pyglet.font.add_directory('C:\\Users\\Zach\\Documents\\Rasperry_Pi\\SpotifyFrame\\fonts\\gotham-rounded')

    # Show default image
    display = DisplayWindow()
    prevSong = ""

    # Start the initial update
    display.window.after(0, update_display, display, prevSong)
    display.run()
from time import sleep
import tkinter as tk
from PIL import Image, ImageTk
import pyglet

window = tk.Tk()

images = {}
default = Image.open("image_thumbnail.gif")
images[0] = ImageTk.PhotoImage(default)

def loadImage(imgPath):
    img = Image.open(imgPath)
    img.thumbnail((880, 880))
    img.save('image_thumbnail.gif')

    cover_art = Image.open("image_thumbnail.gif")
    cover_art_image = ImageTk.PhotoImage(cover_art)
    images[0] = cover_art_image
    cover_art_label.configure(image=images[0])
    window.update()

def loadTitle():
    track_label.config(text="Without a Whisper")
    window.update()

def loadArtist():
    artist_label.config(text="Invent Animate")
    window.update()

def nothingPlaying():
    window.configure(background="white")
    cover_art_label.grid_forget()
    track_label.grid_forget()
    artist_label.grid_forget()

pyglet.font.add_directory('C:\\Users\\Zach\\Documents\\Rasperry_Pi\\SpotifyFrame\\fonts\\gotham-rounded')

window.title("Spotify Frame")
window.overrideredirect(True)
window.geometry("1024x1280")
window.configure(bg="black")

cover_art_label = tk.Label(window, background="black")
cover_art_image = loadImage('Python\FlowerBoy.gif')
cover_art_label.grid(row=0, column=0, padx=72, pady=72)
track_label = tk.Label(window, text="I Ain't Got Time!", font=('GothamRounded-Bold', 50), background='black', foreground='white', justify='center')
# track_label = tk.Label(window, text="SWEET / I THOUGHT YOU WANTED TO DANCE (feat. Brent Faiyez & Fana Hues)", font=('GothamRounded-Bold', 50), background='black', foreground='white', justify='center')
track_label.config(anchor="center")
track_label.grid(row=1, column=0)
artist_label = tk.Label(window, text="Tyler, The Creator", font=('GothamRounded-Book', 20), background='black', foreground='white', justify='center')
artist_label.grid(row=2, column=0)

window.after(7500, lambda:window.destroy())
window.after(2500, lambda:loadImage('Python\Heavener.gif'))
window.after(2500, lambda:loadTitle())
window.after(2500, lambda:loadArtist())
window.after(5000, lambda:nothingPlaying())
window.mainloop()

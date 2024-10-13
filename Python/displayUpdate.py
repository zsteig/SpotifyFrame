import tkinter as tk
from PIL import Image, ImageTk

class DisplayWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Spotify Frame")
        self.window.overrideredirect(True)
        self.window.geometry("1024x1280")
        self.window.configure(bg="black")

        self.image_Label = tk.Label(self.window, bg="black")
        self.image_Label.pack(pady=20)

        self.track_label = tk.Label(self.window, text="Nothing Playing", font=("GothamRounded-Bold", 20), bg="black", fg="white", justify="center")
        self.track_label.grid(row=1, column=0)
        self.track_label.pack(pady=20)

        self.artist_label = tk.Label(self.window, text="", font=("GothamRounded-Book", 20), bg="black", fg="white", justify="center")
        self.artist_label.grid(row=2, column=0)
        self.artist_label.pack(pady=20)

    def update_image(self, image_path):
        img = Image.open(image_path)
        img = ImageTk.PhotoImage(img)
        self.image_Label.config(image=img)
        self.image_Label.image = img

    def update_text(self, track_text, artist_text):
        self.track_label.config(text=track_text)

        self.artist_label.config(text=artist_text)

    def run(self):
        self.window.mainloop()

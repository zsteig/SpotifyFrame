import tkinter as tk
from PIL import Image, ImageTk
import requests
from io import BytesIO
import os

class DisplayWindow:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Spotify Frame")
        self.window.overrideredirect(True)

        width = self.window.winfo_screenwidth()
        height = self.window.winfo_screenheight()

        self.window.geometry(f"{width}x{height}")
        self.window.configure(bg="black")

        self.image_label = tk.Label(self.window, bg="black")
        image_xpadding, image_ypadding = self.calculate_padding(width, height)
        self.image_label.grid(row=0, column=0, padx=image_xpadding, pady=image_ypadding)

        self.track_label = tk.Label(self.window, text="", font=("GothamRounded-Bold", 26), bg="black", fg="white", justify="center")
        self.track_label.grid(row=1, column=0)

        self.artist_label = tk.Label(self.window, text="Not Currently Playing", font=("GothamRounded-Book", 26), bg="black", fg="white", justify="center")
        self.artist_label.grid(row=2, column=0)

        self.window.bind("<Escape>", self.close_window)

    def close_window(self, event):
        self.window.destroy()

    def calculate_padding(self, width, height):
        xpadding = (width - 640) // 2
        ypadding = (height - 960) // 2
        return xpadding, ypadding

    def update_image(self, image_path):
        try:
            print(image_path)
            abs_path = os.path.abspath(image_path)

            if os.path.isfile(abs_path):
                # Local Idle Logo
                img = Image.open(abs_path)
                img.thumbnail((640, 640), Image.ANTIALIAS)
            else:
                # Cover art from API
                response = requests.get(image_path)
                img_data = response.content
                img = Image.open(BytesIO(img_data))
            img = ImageTk.PhotoImage(img)
            self.image_label.config(image=img)
            self.image_label.image = img
        except Exception as e:
            print(f"Error loading image: {e}")

    def update_text(self, track_text, artist_text):
        self.track_label.config(text=track_text)

        self.artist_label.config(text=artist_text)

    def run(self):
        self.window.mainloop()

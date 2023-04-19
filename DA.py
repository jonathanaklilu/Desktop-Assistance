from tkinter import *
from PIL import ImageTk, Image
import webbrowser


class Desktop_Assistance():

    def create_widget(self):
        shortcuts = Tk()
        shortcuts.geometry("300x300")
        shortcuts.title("Desktop Assistance")

        youtube_img = Image.open("/Users/jonathanaklilu/Downloads/youtubelogo.png")
        youtube_img = youtube_img.resize((30, 30))
        youtube_img = ImageTk.PhotoImage(youtube_img)

        youtubetv_img = Image.open("/Users/jonathanaklilu/Downloads/youtubetv.png")
        youtubetv_img = youtubetv_img.resize((30, 30))
        youtubetv_img = ImageTk.PhotoImage(youtubetv_img)

        ku_img = Image.open("/Users/jonathanaklilu/Downloads/kulogo.png")
        ku_img = ku_img.resize((30, 30))
        ku_img = ImageTk.PhotoImage(ku_img)

        google_img = Image.open("/Users/jonathanaklilu/Downloads/googleicon.png")
        google_img = google_img.resize((30, 30))
        google_img = ImageTk.PhotoImage(google_img)

        Label(shortcuts, image=youtube_img).grid(row=1, column=0)
        Label(shortcuts, image=youtubetv_img).grid(row=2, column=0)
        Label(shortcuts, image=ku_img).grid(row=3, column=0)
        Label(shortcuts, image=google_img).grid(row=4, column=0)

        Label(shortcuts, text="Shortcut to Websites", font='ariel 20').grid(row=0, column=0, columnspan=2)
        Button(shortcuts, text="Open Youtube", command=lambda : webbrowser.open_new("https://www.youtube.com")).grid(row=1, column=1, columnspan=4)
        Button(shortcuts, text="Open Youtube TV", command=lambda : webbrowser.open_new("https://tv.youtube.com/?onboard=3")).grid(row=2, column=1, columnspan=4)
        Button(shortcuts, text="Open Canvas", command=lambda : webbrowser.open_new("https://canvas.ku.edu")).grid(row=3, column=1, columnspan=4)
        Button(shortcuts, text="Open Google", command=lambda : webbrowser.open_new("https://www.google.com")).grid(row=4, column=1, columnspan=4)



        shortcuts.mainloop()

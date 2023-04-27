from tkinter import *


class NewsWin:
    def __init__(self):
        news_window = Tk()
        
        news_window.resizable(False, False)
        news_window.iconbitmap("editor.ico")
        news_window.title("World Writer - Changelog")

        self.window_height = 350
        self.window_width = 500

        self.screen_width = news_window.winfo_screenwidth()
        self.screen_height = news_window.winfo_screenheight()

        self.x_cordinate = int((self.screen_width/2) - (self.window_width/2))
        self.y_cordinate = int((self.screen_height/2) - (self.window_height/2))

        news_window.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, self.x_cordinate, self.y_cordinate))

        # Content

        self.news_frame = Frame(news_window)
        self.news_frame.pack(padx=5, pady=5)

        self.version_label = Label(self.news_frame, text="Version: Rebuild 1.0")
        self.version_label.pack(anchor=N)

        self.logs_label = Label(self.news_frame, text="-Rebuild the application")
        self.logs_label.pack(pady=10, anchor=W)
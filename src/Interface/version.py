from tkinter import *

class Version:
    def __init__(self):
        version_window = Tk()

        version_window.resizable(False, False)
        version_window.iconbitmap("editor.ico")
        version_window.title("Write Studio - Version")

        self.window_height = 150
        self.window_width = 250

        self.screen_width = version_window.winfo_screenwidth()
        self.screen_height = version_window.winfo_screenheight()

        x_cordinate = int((self.screen_width/2) - (self.window_width/2))
        y_cordinate = int((self.screen_height/2) - (self.window_height/2))

        version_window.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, x_cordinate, y_cordinate))

        version_frame = Frame(version_window)
        version_frame.pack(padx=5, pady=5)

        self.version_label = Label(version_frame, text="Current version:\nRebuild 1.0")
        self.version_label.pack(pady=5)
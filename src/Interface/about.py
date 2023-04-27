from tkinter import *


class AboutWin:
    def __init__(self):
        about_window = Tk()
        
        about_window.resizable(False, False)
        about_window.iconbitmap("editor.ico")
        about_window.title("World Writer - About")

        self.window_height = 350
        self.window_width = 500

        self.screen_width = about_window.winfo_screenwidth()
        self.screen_height = about_window.winfo_screenheight()

        self.x_cordinate = int((self.screen_width/2) - (self.window_width/2))
        self.y_cordinate = int((self.screen_height/2) - (self.window_height/2))

        about_window.geometry("{}x{}+{}+{}".format(self.window_width, self.window_height, self.x_cordinate, self.y_cordinate))

        # Content
        self.about_frame = Frame(about_window)
        self.about_frame.pack(padx=25, pady=25)

        self.header = Label(self.about_frame, text="World Writer")
        self.header.pack(anchor=N)

        self.content = Label(self.about_frame, text="World Writer is a python project created for editing text file.\nWorld Writer have a lot of functions and a simple menu.\nThis application was created by Hojda Adelin in the early of 2021.")
        self.content.pack(anchor=NW, pady=25)

        self.copy = Label(self.about_frame, text="© World Writer 2022")
        self.copy.pack(anchor=SE, side=BOTTOM, pady=82)

        about_window.mainloop()
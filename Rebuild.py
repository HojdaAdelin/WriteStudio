from tkinter import *
from src.Interface.menu import *



main = Tk()

main.title("Write Studio")
main.iconbitmap("editor.ico")
main.geometry("800x600")
main.minsize(450, 150)




MainMenu(main)


main.mainloop()
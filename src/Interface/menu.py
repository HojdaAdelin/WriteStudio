from tkinter import *
from tkinter import font
from src.Interface.version import *
from src.Interface.news import *
from src.Interface.about import *
import tkinter.messagebox

class MainMenu:
    def __init__(self, win):

        main_menu = Menu(win)
        win.config(menu = main_menu)

        
        self.menu_font = font.Font(family="Avant", size="11")

        self.home_menu = Menu(main_menu, tearoff=False, foreground='black', bg="white", font=self.menu_font, activebackground='#90989e')
        main_menu.add_cascade(label='Home', menu=self.home_menu)
        self.home_menu.add_command(label='News                  ', accelerator='', command=NewsWin)
        self.home_menu.add_command(label='Version', accelerator='', command=Version)
        self.home_menu.add_command(label='About', accelerator='', command=AboutWin)
        
        self.file_menu = Menu(main_menu, tearoff=False, fg='black', bg="white", font=self.menu_font, activebackground='#90989e')
        main_menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label='New                  ', accelerator='Ctrl+N')
        self.file_menu.add_command(label='Save', accelerator='Ctrl+S')
        self.file_menu.add_command(label='Save As', accelerator='')
        self.file_menu.add_command(label='Open File', accelerator='Ctrl+O')
        self.file_menu.add_separator()
        self.file_menu.add_command(label='Print', accelerator='')

        self.edit_menu = Menu(main_menu, tearoff=False, foreground='black', bg="white", font=self.menu_font, activebackground='#90989e')
        main_menu.add_cascade(label='Edit', menu=self.edit_menu)
        self.edit_menu.add_command(label='Undo                  ', accelerator='Ctrl+Z')
        self.edit_menu.add_command(label='Redo', accelerator='Ctrl+Y')
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label='Cut', accelerator='Ctrl+X')
        self.edit_menu.add_command(label='Copy', accelerator='Ctrl+C')
        self.edit_menu.add_command(label='Paste', accelerator='Ctrl+V')
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label='Delete', accelerator='')
        self.edit_menu.add_command(label='Clear', accelerator='')
        self.edit_menu.add_command(label='Select All', accelerator='Ctrl+A')
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label='Find', accelerator='')
        self.edit_menu.add_command(label='Replace', accelerator='')

        self.view_menu = Menu(main_menu, tearoff=False, foreground="black", bg="white", font=self.menu_font, activebackground='#90989e')
        main_menu.add_cascade(label='View', menu=self.view_menu)
        self.view_menu.add_command(label="Zoom in                  ", accelerator='')
        self.view_menu.add_command(label="Zoom out", accelerator='')
        self.view_menu.add_separator()
        self.view_menu.add_command(label="Wrap Word On", accelerator='')
        self.view_menu.add_command(label="Wrap Word Off", accelerator='')
        self.view_menu.add_separator()
        self.view_menu.add_command(label="Low resizable win", accelerator='')
        self.view_menu.add_command(label="Mid resizable win", accelerator='')
        self.view_menu.add_command(label="High resizable win", accelerator='')
        self.view_menu.add_command(label="Default resizable win", accelerator='')
        
        self.texture_menu = Menu(main_menu, tearoff=False, foreground="black", bg="white", font=self.menu_font, activebackground='#90989e')
        main_menu.add_cascade(label='Texture', menu=self.texture_menu)
        self.texture_menu.add_command(label="Light                  ", accelerator='')
        self.texture_menu.add_command(label="Dark", accelerator='')
        self.texture_menu.add_command(label="Oceanic", accelerator='')
        self.texture_menu.add_command(label="Winter", accelerator='')

    
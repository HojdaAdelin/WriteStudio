from __future__ import absolute_import
from os import linesep
from textwrap import fill
from tkinter.ttk import Separator
from turtle import position
from gtts import gTTS
from numpy import delete
from playsound import playsound
import tkinter.messagebox
import os, sys
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
from PIL import ImageTk, Image
import win32print  
import win32api
from tkfontchooser import askfont
from tkinter import ttk



# Loading screen


loading_root = Tk()
loading_root.title('World Writer')
window_height = 600
window_width = 1000

screen_width = loading_root.winfo_screenwidth()
screen_height = loading_root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

loading_root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

loading_root.overrideredirect(True)
loading_root.iconbitmap('editor.ico')
cover_bg = ImageTk.PhotoImage(Image.open("Photo/Cover/cover.png"))
my_label = Label(image=cover_bg)
my_label.place(x=0, y=0, relwidth=1, relheight=1)





def main_window():
    loading_root.destroy()
    root = Tk()

    # ico1 = ImageTk.PhotoImage(Image.open("Photo/a.png"))
    root.iconbitmap('editor.ico')

    root.title('World Writer')

    root.geometry('1200x680')
    root.minsize(650, 350)


    # Separator


    # Icons

    exit_bg = ImageTk.PhotoImage(Image.open("Photo/exit.png"))
    undo_bg = ImageTk.PhotoImage(Image.open("Photo/undo.png"))
    redo_bg = ImageTk.PhotoImage(Image.open("Photo/redo.png"))
    news_bg = ImageTk.PhotoImage(Image.open("Photo/news.png"))
    version_bg = ImageTk.PhotoImage(Image.open("Photo/version.png"))
    font_bg = ImageTk.PhotoImage(Image.open("Photo/font.png"))
    dark_bg = ImageTk.PhotoImage(Image.open("Photo/dark.png"))
    light_bg = ImageTk.PhotoImage(Image.open("Photo/light.png"))
    zoom_bg = ImageTk.PhotoImage(Image.open("Photo/zoom.png"))
    open_bg = ImageTk.PhotoImage(Image.open("Photo/open.png"))
    bold_bg = ImageTk.PhotoImage(Image.open("Photo/bold.png"))
    italic_bg = ImageTk.PhotoImage(Image.open("Photo/italic.png"))
    under_bg = ImageTk.PhotoImage(Image.open("Photo/under.png"))
    stricke_bg = ImageTk.PhotoImage(Image.open("Photo/over.png"))
    about_bg = ImageTk.PhotoImage(Image.open("Photo/about.png"))
    fontText_bg = ImageTk.PhotoImage(Image.open("Photo/fontText.png"))
    new_bg = ImageTk.PhotoImage(Image.open("Photo/new.png"))
    save2_bg = ImageTk.PhotoImage(Image.open("Photo/save2.png"))
    saveas_bg = ImageTk.PhotoImage(Image.open("Photo/saveas.png"))
    open2_bg = ImageTk.PhotoImage(Image.open("Photo/open2.png"))
    print_bg = ImageTk.PhotoImage(Image.open("Photo/print.png"))
    cut_bg = ImageTk.PhotoImage(Image.open("Photo/cut.png"))
    copy_bg = ImageTk.PhotoImage(Image.open("Photo/copy2.png"))
    paste_bg = ImageTk.PhotoImage(Image.open("Photo/paste.png"))
    delete_bg = ImageTk.PhotoImage(Image.open("Photo/delete.png"))
    clear_bg = ImageTk.PhotoImage(Image.open("Photo/clear.png"))
    select_bg = ImageTk.PhotoImage(Image.open("Photo/select.png"))
    find_bg = ImageTk.PhotoImage(Image.open("Photo/find.png"))
    replace_bg = ImageTk.PhotoImage(Image.open("Photo/replace.png"))
    ocean_bg = ImageTk.PhotoImage(Image.open("Photo/ocean.png"))
    winter_bg = ImageTk.PhotoImage(Image.open("Photo/winter.png"))
    back_bg = ImageTk.PhotoImage(Image.open("Photo/back.png"))
    # Font

    size1 = int(24)
    deafolt_prefont = font.Font(size=size1)
    bold_prefont = font.Font(size=size1)
    under_prefont = font.Font(size=size1)
    over_prefont = font.Font(size=size1)
    helvetica_prefont = font.Font(size=size1)
    italic_prefont = font.Font(size=size1)
    sanSerif_prefont = font.Font(size=size1)
    ink_prefont = font.Font(size=size1)
    line_font = font.Font(family='Herald', size='9')
    text_font = font.Font(family='Times New Roman', size=size1)
    menu_font = font.Font(family='Avant', size='11')
    # GLOBAL STATEMENT


    global open_status_name
    open_status_name = False


    global selected
    selected = False


    # Create Functions


    def new_file(e):

        global selected
        if e:
            selected = root.clipboard_clear()

        my_text.delete('1.0', END)
        root.title('New File - Global Document Editor')
        status_bar.config(text="New File", padx=20)
        global open_status_name
        open_status_name = False


    def newE_file():
        my_text.delete('1.0', END)
        root.title('New File - Global Document Editor')
        status_bar.config(text="New File", padx=20)
        global open_status_name
        open_status_name = False

    def open_file(e):
    
    
        my_text.delete('1.0', END)

        text_file = filedialog.askopenfilename(title='Open File', filetypes=(("Text Files", "*.txt"), ("PDF Files", "*.pdf"), ("All Files", "*.*")))
    
    # GLOBAL STATEMENT

        if text_file:
            global open_status_name
            open_status_name = text_file
        else:
            if e:
            
                open_status_name = text_file

        name = text_file
        status_bar.config(text=f'Opened: {name}', padx=20)

        # root.title(f'{name} - Global Document Editor')

        text_file = open(text_file, 'r')
        stuff = text_file.read()

        my_text.insert(END, stuff)
        text_file.close()


    def openE_file():
        
        text_file = filedialog.askopenfilename(title='Open File', filetypes=(("Text Files", "*.txt"), ("PDF Files", "*.pdf"), ("All Files", "*.*")))
        
        if text_file:
            global open_status_name
            open_status_name = text_file
            my_text.delete('1.0', END)
            name = text_file
            status_bar.config(text=f'Opened: {name}', padx=20)

            text_file = open(text_file, 'r')
            stuff = text_file.read()

            my_text.insert(END, stuff)
            text_file.close()
        


    def save_as_file():

        text_file = filedialog.asksaveasfilename(defaultextension=".*", title="Save File", filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        if text_file:
            name = text_file
            status_bar.config(text=f'Saved: {name}', padx=20)

            root.title(f'{name} - Global Document Editor')

            text_file = open(text_file, 'w')
            text_file.write(my_text.get(1.0, END))

            text_file.close()


    def save_file(e):

        global open_status_name

        global selected
        if e:
            selected = open_status_name

        if open_status_name:
            text_file = open(open_status_name, 'w')
            text_file.write(my_text.get(1.0, END))

            text_file.close()
            tkinter.messagebox.showinfo('GDE', 'File Saved!')
            status_bar.config(text=f'Saved: {open_status_name}', padx=20)
        else:
            save_as_file()


    def saveE_file():
        global open_status_name

        if open_status_name:
            text_file = open(open_status_name, 'w')
            text_file.write(my_text.get(1.0, END))

            text_file.close()
            tkinter.messagebox.showinfo('GDE', 'File Saved!')
            status_bar.config(text=f'Saved: {open_status_name}', padx=20)
        else:
            save_as_file()


    def cut_text(e):
        global selected
        global open_status_name

        # KeyBoard
        if e:
            selected = root.clipboard_get()

        else:
            if my_text.selection_get():
                selected = my_text.selection_get()
                my_text.delete("sel.first", "sel.last")
                root.clipboard_clear()
                status_bar.config(text=f'Text Cuted', padx=20)
                root.clipboard_append(selected)


    def cutE_text():
        global selected
        
        if my_text.selection_get():
            selected = my_text.selection_get()
            my_text.delete("sel.first", "sel.last")
            root.clipboard_clear()
            status_bar.config(text=f'Text Cuted', padx=20)
            root.clipboard_append(selected)

    def copy_text(e):
        global selected

        # KeyBoard
        if e:
            selected = root.clipboard_get()

        if my_text.selection_get():
            selected = my_text.selection_get()
            root.clipboard_clear()
            root.clipboard_append(selected)
            status_bar.config(text=f'Copy Function', padx=20)


    def copyE_text():
        global selected

        if my_text.selection_get():
            selected = my_text.selection_get()
            root.clipboard_clear()
            root.clipboard_append(selected)
            status_bar.config(text=f'Copy Function', padx=20)

    def paste_text(e):
        global selected

        # KeyBoard
        if e:
            selected = root.clipboard_get()
            status_bar.config(text='Paste Function', padx=20)
        else:
            if selected:
                position = my_text.index(INSERT)
                my_text.insert(position, selected)

    def pasteE_text():
        global selected
        if selected:
            position = my_text.index(INSERT)
            my_text.insert(position, selected)
            status_bar.config(text='Paste Function', padx=20)


    def print_file():
        # printer_name = win32print.GetDefaultPrinter()
        # status_bar.config(text=printer_name)
        file_to_print = filedialog.askopenfilename(title='Open File', filetypes=(("Text Files", "*.txt"), ("PDF Files", "*.pdf"), ("All Files", "*.*")))
    
        if file_to_print:
            win32api.ShellExecute(0, "print", file_to_print, None, ".", 0)


    def find():
        global edit
        my_text.tag_remove('found', '1.0', END)
     
        # returns to widget currently in focus
        s = edit.get()
     
        if (s):
            idx = '1.0'
            while 1:
                # searches for desired string from index 1
                idx = my_text.search(s, idx, nocase = 1,
                            stopindex = END)
             
                if not idx: break
             
                # last index sum of current index and
                # length of text
                lastidx = '% s+% dc' % (idx, len(s))
             
 
                # overwrite 'Found' at idx
                my_text.tag_add('found', idx, lastidx)
                idx = lastidx
 
            # mark located string as red
         
            my_text.tag_config('found', foreground ='red')
        edit.focus_set()

    # Find Function

    def find_text():
        global edit
        # The window

        find_window = Tk()
        
        find_window.resizable(False, False)
        find_window.iconbitmap("editor.ico")
        find_window.title("World Writer - Find")

        window_height = 300
        window_width = 400

        screen_width = find_window.winfo_screenwidth()
        screen_height = find_window.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        find_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        find_frame = Frame(find_window)
        find_frame.pack(pady=10)

    
        edit = Entry(find_frame)
        edit.pack(side = TOP, fill = X, expand=1, padx=10, pady=10, anchor=N)
        edit.focus_set()
        Find = Button(find_frame, text ='  Find  ')
        Find.pack(side = TOP, pady=20)
        Find.config(command = find)

    # Go to Function



    # Replace Function

    def findNreplace():
        
        s = edit.get()
        r = edit2.get()
        
        if (s and r):
            my_text.tag_remove('found', '1.0', END)
     
            # returns to widget currently in focus
            
     
            idx = '1.0'
            while 1:
                # searches for desired string from index 1
                idx = my_text.search(s, idx, nocase = 1,
                            stopindex = END)
                print(idx)
                if not idx: break
             
                # last index sum of current index and
                # length of text
                lastidx = '% s+% dc' % (idx, len(s))
 
                my_text.delete(idx, lastidx)
                my_text.insert(idx, r)
 
                lastidx = '% s+% dc' % (idx, len(r))
             
                # overwrite 'Found' at idx
                my_text.tag_add('found', idx, lastidx)
                idx = lastidx
 
            # mark located string as red
            my_text.tag_config('found', foreground ='green')
        edit.focus_set()

    def replace_text():
        global edit2
        # The window

        replace_window = Tk()
        
        replace_window.resizable(False, False)
        replace_window.iconbitmap("editor.ico")
        replace_window.title("World Writer - Replace")

        window_height = 300
        window_width = 400

        screen_width = replace_window.winfo_screenwidth()
        screen_height = replace_window.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        replace_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        replace_frame = Frame(replace_window)
        replace_frame.pack(padx=10, pady=10)

        edit2 = Entry(replace_frame)
        edit2.pack(side = TOP, fill = BOTH, pady=10, expand = True, anchor=N)
        edit2.focus_set()
        replace = Button(replace_frame, text = 'Replace')
        replace.pack(side=TOP, anchor=N, pady=20)
        replace.config(command = findNreplace)

    # Fonts
    def deafolt_font():
    
        
        deafolt_prefont.configure(family='Times New Roman')

        my_text.tag_configure("deafolt", font=deafolt_prefont)

        current_tags = my_text.tag_names("sel.first")

        if "deafolt" in current_tags:
            my_text.tag_remove("deafolt", "sel.first", "sel.last")
           
        else:
            my_text.tag_add("deafolt", "sel.first", "sel.last")

    def bold_test():
        bold_prefont.configure(weight="bold")
        my_text.config(font=bold_prefont)


    def bold_font():
        
        
        # bold_prefont = font.Font(my_text, my_text.cget("font"))
        bold_prefont.configure(weight="bold")

        my_text.tag_configure("bold", font=bold_prefont)

        current_tags = my_text.tag_names("sel.first")

        if "bold" in current_tags:
            my_text.tag_remove("bold", "sel.first", "sel.last")
        else:
            my_text.tag_add("bold", "sel.first", "sel.last")

    def italic_font():
    
    
        italic_prefont.configure(slant="italic")

        my_text.tag_configure("italic", font=italic_prefont)

        current_tags = my_text.tag_names("sel.first")

        if "italic" in current_tags:
            my_text.tag_remove("italic", "sel.first", "sel.last")
        else:
            my_text.tag_add("italic", "sel.first", "sel.last")



    def underline_font():
    
    
        under_prefont.configure(underline=1)

        my_text.tag_configure("underline", font=under_prefont)

        current_tags = my_text.tag_names("sel.first")

        if "underline" in current_tags:
            my_text.tag_remove("underline", "sel.first", "sel.last")
        else:
            my_text.tag_add("underline", "sel.first", "sel.last")


    def overstrike_font():
        
        
        over_prefont.configure(overstrike=1)

        my_text.tag_configure("over", font=over_prefont)

        current_tags = my_text.tag_names("sel.first")

        if "over" in current_tags:
            my_text.tag_remove("over", "sel.first", "sel.last")
        else:
            my_text.tag_add("over", "sel.first", "sel.last")


    def helvetica_font():

        
        helvetica_prefont.configure(family='Helvetica')

        my_text.tag_configure("Helvetica", font=helvetica_prefont)

        current_tags = my_text.tag_names("sel.first")

        if "Helvetica" in current_tags:
            my_text.tag_remove("Helvetica", "sel.first", "sel.last")
        else:
            my_text.tag_add("Helvetica", "sel.first", "sel.last")


    def inkFree_font():
        
        
        ink_prefont.configure(family='Ink Free')

        my_text.tag_configure("Ink", font=ink_prefont)

        current_tags = my_text.tag_names("sel.first")

        if "Ink" in current_tags:
            my_text.tag_remove("Ink", "sel.first", "sel.last")
        else:
            my_text.tag_add("Ink", "sel.first", "sel.last")


    def sanSerif_font():

        
        sanSerif_prefont.configure(family='Microsoft Sans Serif')

        my_text.tag_configure("sanSerif", font=sanSerif_prefont)

        current_tags = my_text.tag_names("sel.first")

        if "sanSerif" in current_tags:
            my_text.tag_remove("sanSerif", "sel.first", "sel.last")
        else:
            my_text.tag_add("sanSerif", "sel.first", "sel.last")



    # Color Def


    def text_color():
        my_color = colorchooser.askcolor()[1]
        if my_color:
            status_bar.config(text=["Color:", my_color], padx=20)
            color_font = font.Font(my_text, my_text.cget("font"))

            my_text.tag_configure("color", font=color_font, foreground=my_color)

            current_tags = my_text.tag_names("sel.first")

            if "color" in current_tags:
                my_text.tag_remove("color", "sel.first", "sel.last")
            else:
                my_text.tag_add("color", "sel.first", "sel.last")


    def select_all_text(e):
        my_text.tag_add('sel', '1.0', 'end')

    def selectE_all_text():
        my_text.tag_add('sel', '1.0', 'end')

    def clear_text():
        my_text.delete(1.0, END)


    def version_file():
        
        # The window

        version_window = Tk()
        
        version_window.resizable(False, False)
        version_window.iconbitmap("editor.ico")
        version_window.title("World Writer - Version")

        window_height = 150
        window_width = 250

        screen_width = version_window.winfo_screenwidth()
        screen_height = version_window.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        version_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        version_frame = Frame(version_window)
        version_frame.pack(padx=5, pady=5)

        version_label = Label(version_frame, text="Current version:\n1.1.5")
        version_label.pack(pady=5)

    def delete_text():
        my_text.selection_get()
        my_text.delete("sel.first", "sel.last")

    
    def news_window():
        
        # The window

        news_window = Tk()
        
        news_window.resizable(False, False)
        news_window.iconbitmap("editor.ico")
        news_window.title("World Writer - Changelog")

        window_height = 350
        window_width = 500

        screen_width = news_window.winfo_screenwidth()
        screen_height = news_window.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        news_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        # Content

        news_frame = Frame(news_window)
        news_frame.pack(padx=5, pady=5)

        version_label = Label(news_frame, text="Version 1.1.5")
        version_label.pack(anchor=N)

        logs_label = Label(news_frame, text="-Replace window remodel\n-Find window remodel\n-Second toolbar update\n-Theme update\n-Resizable function\n-Back font function\n-Minor bug fixed")
        logs_label.pack(pady=10, anchor=W)

    def about_file():
        
        # The window

        about_window = Tk()
        
        about_window.resizable(False, False)
        about_window.iconbitmap("editor.ico")
        about_window.title("World Writer - About")

        window_height = 350
        window_width = 500

        screen_width = about_window.winfo_screenwidth()
        screen_height = about_window.winfo_screenheight()

        x_cordinate = int((screen_width/2) - (window_width/2))
        y_cordinate = int((screen_height/2) - (window_height/2))

        about_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

        # Content
        about_frame = Frame(about_window)
        about_frame.pack(padx=25, pady=25)

        header = Label(about_frame, text="World Writer")
        header.pack(anchor=N)

        content = Label(about_frame, text="World Writer is a python project created for editing text file.\nWorld Writer have a lot of functions and a simple menu.\nThis application was created by Hojda Adelin in the early of 2021.")
        content.pack(anchor=NW, pady=25)

        copy = Label(about_frame, text="© World Writer 2022")
        copy.pack(anchor=SE, side=BOTTOM, pady=82)

        about_window.mainloop()

    # Hovered Butoms
    
    def exit_hovered_toolbar(e):
        exit_toolbar["bg"] = '#c8c8de'
        status_bar.config(text='Exit Button!', padx=20)


    def exit_inhovered_toolbar(e):
        exit_toolbar["bg"] = 'white'
        status_bar.config(text='Ready', padx=20)


    def undo_hovered_toolbar(e):
        undo_toolbar["bg"] = '#c8c8de'
        status_bar.config(text='Undo Button!', padx=20)


    def undo_inhovered_toolbar(e):
        undo_toolbar["bg"] = 'white'
        status_bar.config(text='Ready', padx=20)


    def redo_hovered_toolbar(e):
        redo_toolbar["bg"] = '#c8c8de'
        status_bar.config(text='Redo Button!', padx=20)


    def redo_inhovered_toolbar(e):
        redo_toolbar["bg"] = 'white'
        status_bar.config(text='Ready', padx=20)


    def news_hovered_toolbar(e):
        news_toolbar["bg"] = '#c8c8de'
        status_bar.config(text='News Button!', padx=20)


    def news_inhovered_toolbar(e):
        news_toolbar["bg"] = 'white'
        status_bar.config(text='Ready', padx=20)


    def version_hovered_toolbar(e):
        version_toolbar["bg"] = '#c8c8de'
        status_bar.config(text='Version Button!', padx=20)


    def version_inhovered_toolbar(e):

        version_toolbar["bg"] = 'white'
        status_bar.config(text='Ready', padx=20)


    def font_hovered_toolbar(e):
        fontMenu_toolbar["bg"] = '#c8c8de'
        status_bar.config(text='Color Window!', padx=20)


    def font_inhovered_toolbar(e):

        fontMenu_toolbar["bg"] = 'white'
        status_bar.config(text='Ready', padx=20)


    def dark_hovered_toolbar(e):
        dark_toolbar["bg"] = '#c8c8de'
        status_bar.config(text='Dark Mode!', padx=20)


    def dark_inhovered_toolbar(e):
        dark_toolbar["bg"] = 'white'
        status_bar.config(text='Ready!', padx=20)


    def light_hovered_toolbar(e):
        light_toolbar["bg"] = '#c8c8de'
        status_bar.config(text='Default Mode!', padx=20)


    def light_inhovered_toolbar(e):
        light_toolbar["bg"] = 'white'
        status_bar.config(text='Ready!', padx=20)


    def zoom_hovered_toolbar(e):
        zoom_toolbar["bg"] = '#c8c8de'
        status_bar.config(text='Zoom In', padx=20)


    def zoom_inhovered_toolbar(e):
        zoom_toolbar["bg"] = 'white'
        status_bar.config(text='Ready', padx=20)


    def zoomout_hovered_toolbar(e):
        zoomout_toolbar["bg"] = '#c8c8de'
        status_bar.config(text='Zoom Out', padx=20)


    def zoomout_inhovered_toolbar(e):
        zoomout_toolbar["bg"] = 'white'
        status_bar.config(text='Ready', padx=20)

    def bold_hovered_toolbar(e):
        bold_toolbar["bg"] = '#c8c8de'
        status_bar.config(text='Bold Font', padx=20)


    def bold_inhovered_toolbar(e):
        bold_toolbar["bg"] = 'white'
        status_bar.config(text='Ready', padx=20)

    def italic_hovered_toolbar(e):
        italic_toolbar["bg"] = '#c8c8de'
        status_bar.config(text='Italic Font', padx=20)


    def italic_inhovered_toolbar(e):
        italic_toolbar["bg"] = 'white'
        status_bar.config(text='Ready', padx=20)

    def under_hovered_toolbar(e):
        under_toolbar["bg"] = '#c8c8de'
        status_bar.config(text='Italic Font', padx=20)


    def under_inhovered_toolbar(e):
        under_toolbar["bg"] = 'white'
        status_bar.config(text='Ready', padx=20)

    def over_hovered_toolbar(e):
        strike_toolbar["bg"] = '#c8c8de'
        status_bar.config(text='Italic Font', padx=20)


    def over_inhovered_toolbar(e):
        strike_toolbar["bg"] = 'white'
        status_bar.config(text='Ready', padx=20)

    def about_hovered_toolbar(e):
        about_toolbar["bg"] = '#c8c8de'
        status_bar.config(text='About', padx=20)


    def about_inhovered_toolbar(e):
        about_toolbar["bg"] = 'white'
        status_bar.config(text='Ready', padx=20)
    
    def fontText_hovered_toolbar(e):
        font_toolbar["bg"] = '#c8c8de'
        status_bar.config(text='Font Window!', padx=20)

    def fontText_inhovered_toolbar(e):
        font_toolbar["bg"] = 'white'
        status_bar.config(text='Ready', padx=20)

    def open_hovered_toolbar(e):
        open_toolbar["bg"] = '#c8c8de'
        status_bar.config(text='Open File', padx=20)

    def open_inhovered_toolbar(e):
        open_toolbar["bg"] = 'white'
        status_bar.config(text='Ready!', padx=20)
    
    def select_hovered_toolbar(e):
        select_toolbar["bg"] = '#c8c8de'
        status_bar.config(text='Select text', padx=20)

    def select_inhovered_toolbar(e):
        select_toolbar["bg"] = 'white'
        status_bar.config(text='Ready!', padx=20)

    def find_hovered_toolbar(e):
        find_toolbar["bg"] = '#c8c8de'
        status_bar.config(text='Find Window', padx=20)

    def find_inhovered_toolbar(e):
        find_toolbar["bg"] = 'white'
        status_bar.config(text='Ready!', padx=20)

    def replace_hovered_toolbar(e):
        replace_toolbar["bg"] = '#c8c8de'
        status_bar.config(text='Replace Window', padx=20)

    def replace_inhovered_toolbar(e):
        replace_toolbar["bg"] = 'white'
        status_bar.config(text='Ready!', padx=20)

    def ocean_hovered_toolbar(e):
        ocean_toolbar["bg"] = '#c8c8de'

    def ocean_inhovered_toolbar(e):
        ocean_toolbar['bg'] = 'white'

    def winter_hovered_toolbar(e):
        winter_toolbar['bg'] = '#c8c8de'

    def winter_inhovered_toolbar(e):
        winter_toolbar['bg'] = 'white'

    def back_hovered_toolbar(e):
        back_toolbar['bg'] = '#c8c8de'
    
    def back_inhovered_toolbar(e):
        back_toolbar['bg'] = 'white'
    
    # Textures


    def deafolt_texture():

        # Colors

        rot_color = "#242323"
        text_color = "#000000"
        frame_color = "#ffffff"
        toolbar_color = "SystemButtonFace"
        status_color = "SystemButtonFace"
        select_color = "#90989e"
        menu_color = "white"
        # Config

        root.config(bg=rot_color)
        status_bar.config(bg=status_color, fg=text_color, text='Ready', padx=20)
        # copyright_label.config(bg=status_color, fg=text_color)
        my_text.config(bg=frame_color, fg=text_color, selectforeground=text_color, selectbackground=select_color)
        toolbar_frame.config(bg=toolbar_color)
        second_toolbar.config(bg=toolbar_color)
        file_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        edit_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        color_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        font_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        texture_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        home_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        view_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        rc.config(background=menu_color, activebackground=select_color, foreground='black')
        font_label.config(bg=toolbar_color, fg=text_color)
        theme_label.config(bg=toolbar_color, fg=text_color)
        

    def dark_texture():

        # Colors

        rot_color = "#323336"
        text_color = "#ffffff"
        frame_color = "#47484a"
        toolbar_color = "#323336"
        select_color = "#5d5e63"
        menu_color = "#323336"

        # Config

        root.config(bg=rot_color)
        status_bar.config(bg=rot_color, fg=text_color, text='Dark Mode Enabled', padx=20)
        # copyright_label.config(bg=rot_color, fg=text_color)
        my_text.config(bg=frame_color, fg=text_color, selectforeground=text_color, selectbackground=select_color)
        toolbar_frame.config(bg=toolbar_color)
        second_toolbar.config(bg=toolbar_color)
        file_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        edit_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        color_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        font_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        texture_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        home_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        view_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        rc.config(background=menu_color, activebackground=select_color, foreground='white')
        font_label.config(bg=toolbar_color, fg=text_color)
        theme_label.config(bg=toolbar_color, fg=text_color)
    def ocean_texture():
        
        # Colors

        rot_color = "#0c6ec4"
        text_color = "#ffffff"
        frame_color = "#1c70ba"
        toolbar_color = "#0c6ec4"
        select_color = "#1a80d9"
        menu_color = "#0c6ec4"

        # Config

        root.config(bg=rot_color)
        status_bar.config(bg=rot_color, fg=text_color, text='Dark Mode Enabled', padx=20)
        # copyright_label.config(bg=rot_color, fg=text_color)
        my_text.config(bg=frame_color, fg=text_color, selectforeground=text_color, selectbackground=select_color)
        toolbar_frame.config(bg=toolbar_color)
        second_toolbar.config(bg=toolbar_color)
        file_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        edit_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        color_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        font_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        texture_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        home_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        view_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        rc.config(background=menu_color, activebackground=select_color, foreground='white')
        font_label.config(bg=toolbar_color, fg=text_color)
        theme_label.config(bg=toolbar_color, fg=text_color)
    def winter_texture():
        
        # Colors
        rot_color = "#86e1fc"
        text_color = "#ffffff"
        frame_color = "#abddeb"
        toolbar_color = "#86e1fc"
        select_color = "#c7e3eb"
        menu_color = "#86e1fc"


        # Config

        root.config(bg=rot_color)
        status_bar.config(bg=rot_color, fg=text_color, text='Dark Mode Enabled', padx=20)
        # copyright_label.config(bg=rot_color, fg=text_color)
        my_text.config(bg=frame_color, fg=text_color, selectforeground=text_color, selectbackground=select_color)
        toolbar_frame.config(bg=toolbar_color)
        second_toolbar.config(bg=toolbar_color)
        file_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        edit_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        color_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        font_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        texture_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        home_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        view_menu.config(bg=menu_color, foreground=text_color, activebackground=select_color)
        rc.config(background=menu_color, activebackground=select_color, foreground='white')
        font_label.config(bg=toolbar_color, fg=text_color)
        theme_label.config(bg=toolbar_color, fg=text_color)

    # Exite Function

    def ExitApplication():
        MsgBox = tkinter.messagebox.askquestion ('Exit Application','Are you sure you want to exit the application?', icon = 'warning')
        if MsgBox == 'yes':
            root.destroy()
        

    # Options

    # ------------------

    # Zoom Function

    def zoom_text_in():
        
        text_font.config(size=size1 + 8)
        sanSerif_prefont.configure(family='Microsoft Sans Serif', size=size1 + 8)
        deafolt_prefont.configure(family='Times New Roman', size=size1 + 8)
        bold_prefont.configure(weight="bold", size=size1 + 8)
        italic_prefont.configure(slant="italic", size=size1 + 8)
        over_prefont.configure(overstrike=1, size=size1 + 8)
        under_prefont.configure(underline=1, size=size1 + 8)
        helvetica_prefont.configure(family='Helvetica', size=size1 + 8)
        ink_prefont.configure(family='Ink Free', size=size1 + 8)



    def zoom_text_out():
        
        text_font.config(size=size1)
        sanSerif_prefont.config(size=size1)
        deafolt_prefont.config(size=size1)
        bold_prefont.config(size=size1)
        italic_prefont.config(size=size1)
        over_prefont.config(size=size1)
        under_prefont.config(size=size1)
        helvetica_prefont.config(size=size1)
        ink_prefont.config(size=size1)

    # ---------------------------------------
    # Cursors

    def deafolt_cursor():
        root.config(cursor="arrow")
        my_frame.config(cursor="arrow")
        my_text.config(cursor="arrow")
        my_menu.config(cursor="arrow")

    def star_cursor():
        root.config(cursor="star")
        my_frame.config(cursor="star")
        my_text.config(cursor="star")
        my_menu.config(cursor="star")

    def circle_cursor():
        root.config(cursor="circle")
        my_frame.config(cursor="circle")
        my_text.config(cursor="circle")
        my_menu.config(cursor="circle")

    def pirate_cursor():
        root.config(cursor="pirate")
        my_frame.config(cursor="pirate")
        my_text.config(cursor="pirate")
        my_menu.config(cursor="pirate")

    def plus_cursor():
        root.config(cursor="plus")
        my_frame.config(cursor="plus")
        my_text.config(cursor="plus")
        my_menu.config(cursor="plus")


    def wrap_world_on():
        my_text.config(wrap=WORD)
        status_bar.config(text="Word Wrap Enabled")

    def wrap_world_off():
        my_text.config(wrap="none")
        status_bar.config(text="Word Wrap Disabled")



    def font_window():
        
        font = askfont(root)
        
        if font:
            font['family'] = font['family'].replace(' ', '\ ')
            font_str = "%(family)s %(size)i %(weight)s %(slant)s" % font
            if font['underline']:
                font_str += ' underline'
            if font['overstrike']:
                font_str += ' overstrike'
            my_text.config(font=font_str)
            status_bar.config(text=["Font:", font['family']])
        
        


    # Right Click Menu
    rc = Menu(root, tearoff=False, font=line_font, background='white', foreground='black')
    rc.add_command(label='New                         ', command=lambda: new_file(False), accelerator="Ctrl+N", font=menu_font)
    rc.add_command(label='Open', command=lambda: open_file(False), accelerator="Ctrl+O", font=menu_font)
    rc.add_command(label='Save', command=lambda: save_file(False), accelerator="Ctrl+S", font=menu_font)


    def do_popup(event):
        try:
            rc.tk_popup(event.x_root, event.y_root)
        finally:
            rc.grab_release()


    def wrap_word_text_on():
        my_text.config(wrap=WORD)
        
    def wrap_word_text_off():
        my_text.config(wrap="none")
        
    def win_resizable_low():
        root.geometry("600x340")

    def win_resizable_mid():
        root.geometry("900x480")

    def win_resizable_high():
        root.geometry("1400x800")

    def win_resizable_default():
        root.geometry("1200x680")
    
    def home_toolbar():
        global version_toolbar
        global news_toolbar
        global about_toolbar
        global exit_toolbar

        version_toolbar = Button(toolbar_frame, image=version_bg, command=version_file, bg='white')
        version_toolbar.grid(row=0, column=0, sticky=W, padx=20, pady=5)
        version_toolbar.bind('<Enter>', version_hovered_toolbar)
        version_toolbar.bind('<Leave>', version_inhovered_toolbar)

        news_toolbar = Button(toolbar_frame, image=news_bg, command=news_window, bg='white')
        news_toolbar.grid(row=0, column=1, sticky=W, padx=5, pady=5)
        news_toolbar.bind('<Enter>', news_hovered_toolbar)
        news_toolbar.bind('<Leave>', news_inhovered_toolbar)

        about_toolbar = Button(toolbar_frame, image=about_bg, command=about_file, bg='white')
        about_toolbar.grid(row=0, column=2, sticky=W, padx=20, pady=5)
        about_toolbar.bind('<Enter>', about_hovered_toolbar)
        about_toolbar.bind('<Leave>', about_inhovered_toolbar)

        exit_toolbar = Button(toolbar_frame, image=exit_bg, command=ExitApplication, bg='white')
        exit_toolbar.grid(row=0, column=3, sticky=W, padx=5, pady=5)
        exit_toolbar.bind('<Enter>', exit_hovered_toolbar)
        exit_toolbar.bind('<Leave>', exit_inhovered_toolbar)

    def file_toolbar():

        global new_toolbar
        global save_toolbar
        global saveas_toolbar
        global open_toolbar
        global print_toolbar

        version_toolbar.destroy()
        news_toolbar.destroy()
        about_toolbar.destroy()
        exit_toolbar.destroy()
        undo_toolbar.destroy()
        redo_toolbar.destroy()
        cut_toolbar.destroy()
        copy_toolbar.destroy()
        paste_toolbar.destroy()
        delete_toolbar.destroy()
        clear_toolbar.destroy()
        select_toolbar.destroy()
        find_toolbar.destroy()
        replace_toolbar.destroy()
        fontMenu_toolbar.destroy()
        font_toolbar.destroy()
        bold_toolbar.destroy()
        italic_toolbar.destroy()
        under_toolbar.destroy()
        strike_toolbar.destroy()
        dark_toolbar.destroy()
        light_toolbar.destroy()
        zoom_toolbar.destroy()
        zoomout_toolbar.destroy()

        new_toolbar = Button(toolbar_frame, image=new_bg, command=newE_file, bg='white')
        new_toolbar.grid(row=0, column=0, sticky=W, padx=20, pady=5)
        new_toolbar.bind('<Enter>', exit_hovered_toolbar)
        new_toolbar.bind('<Leave>', exit_inhovered_toolbar)

        save_toolbar = Button(toolbar_frame, image=save2_bg, command=saveE_file, bg='white')
        save_toolbar.grid(row=0, column=1, sticky=W, padx=5, pady=5)
        save_toolbar.bind('<Enter>', exit_hovered_toolbar)
        save_toolbar.bind('<Leave>', exit_inhovered_toolbar)

        saveas_toolbar = Button(toolbar_frame, image=saveas_bg, command=save_as_file, bg='white')
        saveas_toolbar.grid(row=0, column=2, sticky=W, padx=20, pady=5)
        saveas_toolbar.bind('<Enter>', exit_hovered_toolbar)
        saveas_toolbar.bind('<Leave>', exit_inhovered_toolbar)

        open_toolbar = Button(toolbar_frame, image=open2_bg, command=openE_file, bg='white')
        open_toolbar.grid(row=0, column=3, sticky=W, padx=5, pady=5)
        open_toolbar.bind('<Enter>', exit_hovered_toolbar)
        open_toolbar.bind('<Leave>', exit_inhovered_toolbar)

        print_toolbar = Button(toolbar_frame, image=print_bg, command=print_file, bg='white')
        print_toolbar.grid(row=0, column=4, sticky=W, padx=25, pady=5)
        print_toolbar.bind('<Enter>', exit_hovered_toolbar)
        print_toolbar.bind('<Leave>', exit_inhovered_toolbar)

    def edit_toolbar():

        global undo_toolbar
        global redo_toolbar
        global cut_toolbar
        global copy_toolbar
        global paste_toolbar
        global delete_toolbar
        global clear_toolbar
        global select_toolbar
        global find_toolbar
        global replace_toolbar

        version_toolbar.destroy()
        news_toolbar.destroy()
        about_toolbar.destroy()
        exit_toolbar.destroy()
        fontMenu_toolbar.destroy()
        font_toolbar.destroy()
        bold_toolbar.destroy()
        italic_toolbar.destroy()
        under_toolbar.destroy()
        strike_toolbar.destroy()
        dark_toolbar.destroy()
        light_toolbar.destroy()
        zoom_toolbar.destroy()
        zoomout_toolbar.destroy()
        new_toolbar.destroy()
        save_toolbar.destroy()
        saveas_toolbar.destroy()
        open_toolbar.destroy()
        print_toolbar.destroy()

        undo_toolbar = Button(toolbar_frame, image=undo_bg, command=my_text.edit_undo, bg='white')
        undo_toolbar.grid(row=0, column=0, sticky=W, padx=20, pady=5)
        undo_toolbar.bind('<Enter>', undo_hovered_toolbar)
        undo_toolbar.bind('<Leave>', undo_inhovered_toolbar)

        redo_toolbar = Button(toolbar_frame, image=redo_bg, command=my_text.edit_redo, bg='white')
        redo_toolbar.grid(row=0, column=1, sticky=W, padx=5, pady=5)
        redo_toolbar.bind('<Enter>', redo_hovered_toolbar)
        redo_toolbar.bind('<Leave>', redo_inhovered_toolbar)

        cut_toolbar = Button(toolbar_frame, image=cut_bg, command=cutE_text, bg='white')
        cut_toolbar.grid(row=0, column=2, sticky=W, padx=20, pady=5)
        cut_toolbar.bind('<Enter>', redo_hovered_toolbar)
        cut_toolbar.bind('<Leave>', redo_inhovered_toolbar)

        copy_toolbar = Button(toolbar_frame, image=copy_bg, command=copyE_text, bg='white')
        copy_toolbar.grid(row=0, column=3, sticky=W, padx=5, pady=5)
        copy_toolbar.bind('<Enter>', redo_hovered_toolbar)
        copy_toolbar.bind('<Leave>', redo_inhovered_toolbar)

        paste_toolbar = Button(toolbar_frame, image=paste_bg, command=pasteE_text, bg='white')
        paste_toolbar.grid(row=0, column=4, sticky=W, padx=25, pady=5)
        paste_toolbar.bind('<Enter>', redo_hovered_toolbar)
        paste_toolbar.bind('<Leave>', redo_inhovered_toolbar)   

        delete_toolbar = Button(toolbar_frame, image=delete_bg, command=delete_text, bg='white')
        delete_toolbar.grid(row=0, column=5, sticky=W, padx=0, pady=5)
        delete_toolbar.bind('<Enter>', redo_hovered_toolbar)
        delete_toolbar.bind('<Leave>', redo_inhovered_toolbar)

        clear_toolbar = Button(toolbar_frame, image=clear_bg, command=clear_text, bg='white')
        clear_toolbar.grid(row=0, column=6, sticky=W, padx=25, pady=5)
        clear_toolbar.bind('<Enter>', redo_hovered_toolbar)
        clear_toolbar.bind('<Leave>', redo_inhovered_toolbar)

        select_toolbar = Button(toolbar_frame, image=select_bg, command=selectE_all_text, bg='white')
        select_toolbar.grid(row=0, column=7, sticky=W, padx=0, pady=5)
        select_toolbar.bind('<Enter>', redo_hovered_toolbar)
        select_toolbar.bind('<Leave>', redo_inhovered_toolbar)

        find_toolbar = Button(toolbar_frame, image=find_bg, command=find_text, bg='white')
        find_toolbar.grid(row=0, column=8, sticky=W, padx=25, pady=5)
        find_toolbar.bind('<Enter>', redo_hovered_toolbar)
        find_toolbar.bind('<Leave>', redo_inhovered_toolbar)

        replace_toolbar = Button(toolbar_frame, image=replace_bg, command=replace_text, bg='white')
        replace_toolbar.grid(row=0, column=9, sticky=W, padx=0, pady=5)
        replace_toolbar.bind('<Enter>', redo_hovered_toolbar)
        replace_toolbar.bind('<Leave>', redo_inhovered_toolbar)

    

    def fonts_toolbar():
        
        global font_toolbar
        global bold_toolbar
        global italic_toolbar
        global under_toolbar
        global strike_toolbar

        version_toolbar.destroy()
        news_toolbar.destroy()
        about_toolbar.destroy()
        exit_toolbar.destroy()
        undo_toolbar.destroy()
        redo_toolbar.destroy()
        cut_toolbar.destroy()
        copy_toolbar.destroy()
        paste_toolbar.destroy()
        delete_toolbar.destroy()
        clear_toolbar.destroy()
        select_toolbar.destroy()
        find_toolbar.destroy()
        replace_toolbar.destroy()
        fontMenu_toolbar.destroy()
        dark_toolbar.destroy()
        light_toolbar.destroy()
        zoom_toolbar.destroy()
        zoomout_toolbar.destroy()
        new_toolbar.destroy()
        save_toolbar.destroy()
        saveas_toolbar.destroy()
        open_toolbar.destroy()
        print_toolbar.destroy()

        font_toolbar = Button(toolbar_frame, image=fontText_bg, command=font_window, bg='white')
        font_toolbar.grid(row=0, column=0, sticky=W, padx=20, pady=5)
        font_toolbar.bind('<Enter>', fontText_hovered_toolbar)
        font_toolbar.bind('<Leave>', fontText_inhovered_toolbar)

        bold_toolbar = Button(toolbar_frame, image=bold_bg, command=bold_font, bg='white')
        bold_toolbar.grid(row=0, column=1, sticky=W, padx=5, pady=5)
        bold_toolbar.bind('<Enter>', bold_hovered_toolbar)
        bold_toolbar.bind('<Leave>', bold_inhovered_toolbar)

    
        italic_toolbar = Button(toolbar_frame, image=italic_bg, command=italic_font, bg='white')
        italic_toolbar.grid(row=0, column=2, sticky=W, padx=20, pady=5)
        italic_toolbar.bind('<Enter>', italic_hovered_toolbar)
        italic_toolbar.bind('<Leave>', italic_inhovered_toolbar)

        under_toolbar = Button(toolbar_frame, image=under_bg, command=underline_font, bg='white')
        under_toolbar.grid(row=0, column=3, sticky=W, padx=5, pady=5)
        under_toolbar.bind('<Enter>', under_hovered_toolbar)
        under_toolbar.bind('<Leave>', under_inhovered_toolbar)

        strike_toolbar = Button(toolbar_frame, image=stricke_bg, command=overstrike_font, bg='white')
        strike_toolbar.grid(row=0, column=4, sticky=W, padx=25, pady=5)
        strike_toolbar.bind('<Enter>', over_hovered_toolbar)
        strike_toolbar.bind('<Leave>', over_inhovered_toolbar)
    

    def options_toolbar():
        global dark_toolbar
        global light_toolbar
        global fontMenu_toolbar
        dark_toolbar = Button(toolbar_frame, image=dark_bg, command=dark_texture, bg='white')
        dark_toolbar.grid(row=0, column=0, sticky=W, padx=20, pady=5)
        dark_toolbar.bind('<Enter>', dark_hovered_toolbar)
        dark_toolbar.bind('<Leave>', dark_inhovered_toolbar)

        light_toolbar = Button(toolbar_frame, image=light_bg, command=deafolt_texture, bg='white')
        light_toolbar.grid(row=0, column=1, sticky=W, padx=5, pady=5)
        light_toolbar.bind('<Enter>', light_hovered_toolbar)
        light_toolbar.bind('<Leave>', light_inhovered_toolbar)

        fontMenu_toolbar = Button(toolbar_frame, image=font_bg, command=text_color, bg='white')
        fontMenu_toolbar.grid(row=0, column=0, sticky=W, padx=20, pady=5)
        fontMenu_toolbar.bind('<Enter>', font_hovered_toolbar)
        fontMenu_toolbar.bind('<Leave>', font_inhovered_toolbar)

    def view_toolbar():
        global zoom_toolbar
        global zoomout_toolbar

        version_toolbar.destroy()
        news_toolbar.destroy()
        about_toolbar.destroy()
        exit_toolbar.destroy()
        undo_toolbar.destroy()
        redo_toolbar.destroy()
        cut_toolbar.destroy()
        copy_toolbar.destroy()
        paste_toolbar.destroy()
        delete_toolbar.destroy()
        clear_toolbar.destroy()
        select_toolbar.destroy()
        find_toolbar.destroy()
        replace_toolbar.destroy()
        fontMenu_toolbar.destroy()
        font_toolbar.destroy()
        bold_toolbar.destroy()
        italic_toolbar.destroy()
        under_toolbar.destroy()
        strike_toolbar.destroy()
        dark_toolbar.destroy()
        light_toolbar.destroy()
        new_toolbar.destroy()
        save_toolbar.destroy()
        saveas_toolbar.destroy()
        open_toolbar.destroy()
        print_toolbar.destroy()

        zoom_toolbar = Button(toolbar_frame, image=zoom_bg, command=zoom_text_in, bg='white')
        zoom_toolbar.grid(row=0, column=8, sticky=W, padx=25, pady=5)
        zoom_toolbar.bind('<Enter>', zoom_hovered_toolbar)
        zoom_toolbar.bind('<Leave>', zoom_inhovered_toolbar)

        zoomout_toolbar = Button(toolbar_frame, image=open_bg, command=zoom_text_out, bg='white')
        zoomout_toolbar.grid(row=0, column=9, sticky=W, padx=0, pady=5)
        zoomout_toolbar.bind('<Enter>', zoomout_hovered_toolbar)
        zoomout_toolbar.bind('<Leave>', zoomout_inhovered_toolbar)

    
    # Toolbar frame
    
    
    toolbar_frame = Frame(root)
    toolbar_frame.pack(fill=X)

    
    # Toolbar items
    
    news_toolbar = Button(toolbar_frame, image=news_bg, command=news_window, bg='white', width=32, height=32)
    news_toolbar.grid(row=0, column=0, sticky=W, padx=5, pady=5)
    news_toolbar.bind('<Enter>', news_hovered_toolbar)
    news_toolbar.bind('<Leave>', news_inhovered_toolbar)

    open_toolbar = Button(toolbar_frame, image=open2_bg, command=openE_file, bg='white')
    open_toolbar.grid(row=0, column=1, sticky=W, padx=5, pady=5)
    open_toolbar.bind('<Enter>', open_hovered_toolbar)
    open_toolbar.bind('<Leave>', open_inhovered_toolbar)

    select_toolbar = Button(toolbar_frame, image=select_bg, command=selectE_all_text, bg='white')
    select_toolbar.grid(row=0, column=2, sticky=W, padx=5, pady=5)
    select_toolbar.bind('<Enter>', select_hovered_toolbar)
    select_toolbar.bind('<Leave>', select_inhovered_toolbar)

    find_toolbar = Button(toolbar_frame, image=find_bg, command=find_text, bg='white')
    find_toolbar.grid(row=0, column=3, sticky=W, padx=5, pady=5)
    find_toolbar.bind('<Enter>', find_hovered_toolbar)
    find_toolbar.bind('<Leave>', find_inhovered_toolbar)

    replace_toolbar = Button(toolbar_frame, image=replace_bg, command=replace_text, bg='white')
    replace_toolbar.grid(row=0, column=4, sticky=W, padx=5, pady=5)
    replace_toolbar.bind('<Enter>', replace_hovered_toolbar)
    replace_toolbar.bind('<Leave>', replace_inhovered_toolbar)

    font_toolbar = Button(toolbar_frame, image=fontText_bg, command=font_window, bg='white')
    font_toolbar.grid(row=0, column=5, sticky=W, padx=5, pady=5)
    font_toolbar.bind('<Enter>', fontText_hovered_toolbar)
    font_toolbar.bind('<Leave>', fontText_inhovered_toolbar)

    fontMenu_toolbar = Button(toolbar_frame, image=font_bg, command=text_color, bg='white')
    fontMenu_toolbar.grid(row=0, column=6, sticky=W, padx=5, pady=5)
    fontMenu_toolbar.bind('<Enter>', font_hovered_toolbar)
    fontMenu_toolbar.bind('<Leave>', font_inhovered_toolbar)

    zoom_toolbar = Button(toolbar_frame, image=zoom_bg, command=zoom_text_in, bg='white')
    zoom_toolbar.grid(row=0, column=7, sticky=W, padx=5, pady=5)
    zoom_toolbar.bind('<Enter>', zoom_hovered_toolbar)
    zoom_toolbar.bind('<Leave>', zoom_inhovered_toolbar)

    zoomout_toolbar = Button(toolbar_frame, image=open_bg, command=zoom_text_out, bg='white')
    zoomout_toolbar.grid(row=0, column=8, sticky=W, padx=5, pady=5)
    zoomout_toolbar.bind('<Enter>', zoomout_hovered_toolbar)
    zoomout_toolbar.bind('<Leave>', zoomout_inhovered_toolbar)

    # Second toolbar

    second_toolbar = Frame(root)
    second_toolbar.pack(fill=X)

    font_label = Label(second_toolbar, text="Fonts:")
    font_label.grid(row=0, column=0, sticky=W, padx=5, pady=5)

    back_toolbar = Button(second_toolbar, image=back_bg, command=deafolt_font, bg='white', width=16, height=16)
    back_toolbar.grid(row=0, column=1, sticky=W, padx=5, pady=5)
    back_toolbar.bind('<Enter>', back_hovered_toolbar)
    back_toolbar.bind('<Leave>', back_inhovered_toolbar)

    bold_toolbar = Button(second_toolbar, image=bold_bg, command=bold_font, bg='white', width=16, height=16)
    bold_toolbar.grid(row=0, column=2, sticky=W, padx=5, pady=5)
    bold_toolbar.bind('<Enter>', bold_hovered_toolbar)
    bold_toolbar.bind('<Leave>', bold_inhovered_toolbar)

    
    italic_toolbar = Button(second_toolbar, image=italic_bg, command=italic_font, bg='white', width=16, height=16)
    italic_toolbar.grid(row=0, column=3, sticky=W, padx=5, pady=5)
    italic_toolbar.bind('<Enter>', italic_hovered_toolbar)
    italic_toolbar.bind('<Leave>', italic_inhovered_toolbar)

    under_toolbar = Button(second_toolbar, image=under_bg, command=underline_font, bg='white', width=16, height=16)
    under_toolbar.grid(row=0, column=4, sticky=W, padx=5, pady=5)
    under_toolbar.bind('<Enter>', under_hovered_toolbar)
    under_toolbar.bind('<Leave>', under_inhovered_toolbar)

    strike_toolbar = Button(second_toolbar, image=stricke_bg, command=overstrike_font, bg='white', width=16, height=16)
    strike_toolbar.grid(row=0, column=5, sticky=W, padx=5, pady=5)
    strike_toolbar.bind('<Enter>', over_hovered_toolbar)
    strike_toolbar.bind('<Leave>', over_inhovered_toolbar)
    
    theme_label = Label(second_toolbar, text="Themes:")
    theme_label.grid(row=0, column=6, sticky=W, padx=10, pady=5)

    dark_toolbar = Button(second_toolbar, image=dark_bg, command=dark_texture, bg='white')
    dark_toolbar.grid(row=0, column=7, sticky=W, padx=5, pady=5)
    dark_toolbar.bind('<Enter>', dark_hovered_toolbar)
    dark_toolbar.bind('<Leave>', dark_inhovered_toolbar)

    light_toolbar = Button(second_toolbar, image=light_bg, command=deafolt_texture, bg='white')
    light_toolbar.grid(row=0, column=8, sticky=W, padx=5, pady=5)
    light_toolbar.bind('<Enter>', light_hovered_toolbar)
    light_toolbar.bind('<Leave>', light_inhovered_toolbar)  

    ocean_toolbar = Button(second_toolbar, image=ocean_bg, command=ocean_texture, bg='white')
    ocean_toolbar.grid(row=0, column=9, sticky=W, padx=5, pady=5)
    ocean_toolbar.bind('<Enter>', ocean_hovered_toolbar)
    ocean_toolbar.bind('<Leave>', ocean_inhovered_toolbar)  

    winter_toolbar = Button(second_toolbar, image=winter_bg, command=winter_texture, bg='white')
    winter_toolbar.grid(row=0, column=10, sticky=W, padx=5, pady=5)
    winter_toolbar.bind('<Enter>', winter_hovered_toolbar)
    winter_toolbar.bind('<Leave>', winter_inhovered_toolbar) 

    # My Frame

    my_frame = Frame(root)


    # Scrol dreapta


    text_scroll = Scrollbar(my_frame)
    text_scroll.pack(side=RIGHT, fill=Y)

    # Copyright Label

    # copyright_label = Label(my_frame, text='© World Writer 2022', anchor=E, padx=20, pady=7)
    # copyright_label.pack(fill=X, side=BOTTOM, ipadx=5)

    # Status Bar
    # -fill, -in, -ipadx, -ipady, -padx, -pady, or -side

    status_bar = Label(root, text='Ready', anchor=E, padx=20)
    status_bar.pack(fill=X, side=BOTTOM, ipady=5)


    # Scrol vertical

    hor_scroll = Scrollbar(my_frame, orient="horizontal")
    hor_scroll.pack(side=BOTTOM, fill=X)

    # Frame

    my_frame.pack(pady=0, padx=0)

    my_text = Text(my_frame, width=800, height=200, font=text_font, selectbackground='#90989e', selectforeground='black', undo=True, yscrollcommand=text_scroll.set, wrap="none", xscrollcommand=hor_scroll.set)

    my_text.pack(side=BOTTOM)

    #Menu Frame

    my_menu = Menu(root)
    root.config(menu=my_menu)

    # Home
    home_menu = Menu(my_menu, tearoff=False, foreground='black', bg="white", font=menu_font, activebackground='#90989e')
    my_menu.add_cascade(label='Home', menu=home_menu)
    home_menu.add_command(label='News                  ', accelerator='', command=news_window)
    home_menu.add_command(label='Version', accelerator='', command=version_file)
    home_menu.add_command(label='About', accelerator='', command=about_file)
    home_menu.add_separator()
    home_menu.add_command(label='Exit', accelerator='', command=ExitApplication)
    
    # File
    file_menu = Menu(my_menu, tearoff=False, foreground='black', bg="white", font=menu_font, activebackground='#90989e')
    my_menu.add_cascade(label='File', menu=file_menu)
    file_menu.add_command(label='New                  ', accelerator='Ctrl+N', command=newE_file)
    file_menu.add_command(label='Save', accelerator='Ctrl+S', command=saveE_file)
    file_menu.add_command(label='Save As', accelerator='', command=save_as_file)
    file_menu.add_command(label='Open File', accelerator='Ctrl+O', command=openE_file)
    file_menu.add_separator()
    file_menu.add_command(label='Print', accelerator='', command=print_file)

    # Edit 
    edit_menu = Menu(my_menu, tearoff=False, foreground='black', bg="white", font=menu_font, activebackground='#90989e')
    my_menu.add_cascade(label='Edit', menu=edit_menu)
    edit_menu.add_command(label='Undo                  ', accelerator='Ctrl+Z', command=my_text.edit_undo)
    edit_menu.add_command(label='Redo', accelerator='Ctrl+Y', command=my_text.edit_redo)
    edit_menu.add_separator()
    edit_menu.add_command(label='Cut', accelerator='Ctrl+X', command=cutE_text)
    edit_menu.add_command(label='Copy', accelerator='Ctrl+C', command=copyE_text)
    edit_menu.add_command(label='Paste', accelerator='Ctrl+V', command=pasteE_text)
    edit_menu.add_separator()
    edit_menu.add_command(label='Delete', accelerator='', command=delete_text)
    edit_menu.add_command(label='Clear', accelerator='', command=clear_text)
    edit_menu.add_command(label='Select All', accelerator='Ctrl+A', command=selectE_all_text)
    edit_menu.add_separator()
    edit_menu.add_command(label='Find', accelerator='', command=find_text)
    edit_menu.add_command(label='Replace', accelerator='', command=replace_text)

    # Fonts
    font_menu = Menu(my_menu, tearoff=False, foreground='black', bg="white", font=menu_font, activebackground='#90989e')
    my_menu.add_cascade(label='Fonts', menu=font_menu)
    font_menu.add_command(label='Font Window                  ', accelerator='', command=font_window)
    font_menu.add_separator()
    font_menu.add_command(label='Bold', accelerator='', command=bold_font)
    font_menu.add_command(label='Italic', accelerator='', command=italic_font)
    font_menu.add_command(label="Under", accelerator='', command=underline_font)
    font_menu.add_command(label="Strike", accelerator='', command=overstrike_font)

    #Color
    color_menu = Menu(my_menu, tearoff=False, foreground="black", bg="white", font=menu_font, activebackground='#90989e')
    my_menu.add_cascade(label='Color', menu=color_menu)
    color_menu.add_command(label="Colors                  ", accelerator='', command=text_color)

    #View
    view_menu = Menu(my_menu, tearoff=False, foreground="black", bg="white", font=menu_font, activebackground='#90989e')
    my_menu.add_cascade(label='View', menu=view_menu)
    view_menu.add_command(label="Zoom in                  ", accelerator='', command=zoom_text_in)
    view_menu.add_command(label="Zoom out", accelerator='', command=zoom_text_out)
    view_menu.add_separator()
    view_menu.add_command(label="Wrap Word On", accelerator='', command=wrap_word_text_on)
    view_menu.add_command(label="Wrap Word Off", accelerator='', command=wrap_word_text_off)
    view_menu.add_separator()
    view_menu.add_command(label="Low resizable win", accelerator='', command=win_resizable_low)
    view_menu.add_command(label="Mid resizable win", accelerator='', command=win_resizable_mid)
    view_menu.add_command(label="High resizable win", accelerator='', command=win_resizable_high)
    view_menu.add_command(label="Default resizable win", accelerator='', command=win_resizable_default)
    
    #Texture
    texture_menu = Menu(my_menu, tearoff=False, foreground="black", bg="white", font=menu_font, activebackground='#90989e')
    my_menu.add_cascade(label='Texture', menu=texture_menu)
    texture_menu.add_command(label="Light                  ", accelerator='', command=deafolt_texture)
    texture_menu.add_command(label="Dark", accelerator='', command=dark_texture)
    texture_menu.add_command(label="Oceanic", accelerator='', command=ocean_texture)
    texture_menu.add_command(label="Winter", accelerator='', command=winter_texture)


    # Configurare Scroluri

    text_scroll.config(command=my_text.yview)
    hor_scroll.config(command=my_text.xview)
    
    # Bind
    root.bind('<Control-Key-n>', new_file)
    root.bind('<Control-Key-o>', open_file)
    root.bind('<Control-Key-x>', cut_text)
    root.bind('<Control-Key-c>', copy_text)
    root.bind('<Control-Key-v>', paste_text)
    root.bind('<Control-Key-s>', save_file)
    root.bind('<Control-Key-z>', my_text.edit_undo)
    root.bind('<Control-Key-y>', my_text.edit_redo)
    # root.bind('<Alt-F5>', ExitApplication)
    root.bind('<Control-Key-A>', select_all_text)
    root.bind('<Control-Key-a>', select_all_text)
    root.bind('<Button-3>', do_popup)


    root.mainloop()

loading_root.after(1500, main_window)
mainloop()

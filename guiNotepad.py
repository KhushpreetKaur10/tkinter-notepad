from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.messagebox import showinfo
import os


def newFile():
    global file
    root.title("Untitled1 - Notepad")
    file = None
    textArea.delete(1.0, END)

def openFile():
    global file
    file = filedialog.askopenfilename(defaultextension='.txt', filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textArea.delete(1.0, END)
        f = open(file, "r")
        textArea.insert(1.0, f.read())
        f.close()

def saveFile():
    global file
    if file==None:
        file= filedialog.asksaveasfilename(initialfile="Untitled.txt", defaultextension='.txt', filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file=None
        else:
            f = open(file, "w")
            f.write(textArea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
            messagebox.showinfo("Info", "File saved successfully!")
    else:
        f = open(file, "w")
        f.write(textArea.get(1.0, END))
        f.close()

def quitApp():
    root.destroy()

def cut():
    textArea.event_generate(("<<Cut>>"))

def copy():
    textArea.event_generate(("<<Copy>>"))

def paste():
    textArea.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad by Khushi")



if __name__=='__main__':
    root = Tk()
    root.title("Untitled1 - Notepad")
    root.geometry('800x600')
    root.wm_iconbitmap(r"C:\Users\HP\Music\old\python\tkinterProjects\projects\GUI-Notepad\1.png")
    
    textArea = Text(root, wrap=WORD, font=("Helvetica", 12), fg="blue")
    file = None
    textArea.pack(expand=True, fill=BOTH)

    scroll = Scrollbar(textArea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=textArea.yview)
    textArea.config(yscrollcommand=scroll.set)


    menuBar = Menu(root)
    fileMenu = Menu(menuBar, tearoff=0)

    fileMenu.add_command(label="New", command=newFile)
    fileMenu.add_command(label="Open", command=openFile)
    fileMenu.add_command(label="Save", command=saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label="Exit", command=quitApp)

    menuBar.add_cascade(label="File", menu=fileMenu)
    root.config(menu=menuBar)

    editMenu = Menu(menuBar, tearoff=0)
    editMenu.add_command(label="Cut", command=cut)
    editMenu.add_command(label="Copy", command=copy)
    editMenu.add_command(label="Paste", command=paste)
    menuBar.add_cascade(label="Edit", menu=editMenu)

    helpMenu = Menu(menuBar, tearoff=0)
    helpMenu.add_command(label="About Notepad", command=about)
    menuBar.add_cascade(label="Help", menu=helpMenu)




    root.mainloop()
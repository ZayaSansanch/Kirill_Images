from cProfile import label
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
# from PIL import ImageFilter
import os

downIMG = ""
downIMGLable = ""
image = ""
filepath = ""
pixel = (0, 0, 0)
pixelRight = (0, 0, 0)
cmena = False
pR = 0
pG = 0
pb = 0

def openfile():
    filepath = filedialog.askopenfile(title="Select file")
    print(filepath.read())

def select_files():
    filetypes = (
        ('IMG files', '*.jpg ' + '*,jpeg ' + '*.png '),
        # ('IMG files', '*.jpg'),
        ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Open files',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Selected Files',
        message=filenames
    )

    curDir = os.getcwd()
    fn = curDir
    
    # file = Entry(text = "file")
    filetexttest = Label(text = "File name:")

    downIMG = ImageTk.PhotoImage(Image.open(fn + file).resize((320, 240)))
    downIMGLable = Label(image = downIMG)
    
    downIMGLable.grid(row = 8, column = 1)

root = Tk()
root.title("Coloring utility")
root.geometry("1280x720")
root.resizable(width = False, height = False)

fileOpen = Button(text = "File", command = select_files)

pR = Entry(text = "Red porogue")
pG = Entry(text = "Green porogue")
pB = Entry(text = "blue porogue")


pRtext = Label(text = "Red porogue:")
pGtext = Label(text = "Green porogue:")
pBtext = Label(text = "blue porogue:")


result = Button(text = "Result")



fileOpen.grid(row = 2, column = 1)

result.grid(row = 7, column = 1)

pR.grid(row = 3, column = 2)
pG.grid(row = 4, column = 2)
pB.grid(row = 5, column = 2)


pRtext.grid(row = 3, column = 1)
pGtext.grid(row = 4, column = 1)
pBtext.grid(row = 5 , column = 1)

# file.grid(row = 1, column = 2)
# filetexttest.grid(row = 1, column = 1)


root.mainloop()
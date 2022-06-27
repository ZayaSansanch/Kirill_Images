from cProfile import label
from fileinput import filename
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

# def select_files():
filetypes = (
    ('IMG files', '*.jpg ' + '*,jpeg ' + '*.png '),
    # ('IMG files', '*.jpg'),
    ('All files', '*.*')
)

filenames = fd.askopenfilenames(
    title='Coloring utility/open file',
    initialdir='/',
    filetypes=filetypes)

# showinfo(
#     title='Selected Files',
#     message=filenames
# )

curDir = os.getcwd()
fn = curDir

root = Tk()
print(filenames[0])
downIMG = ImageTk.PhotoImage(Image.open(filenames[0]).resize((320, 240)))
downIMGLable = Label(image = downIMG)
# downIMGLable.grid(row = 8, column = 1)
    

root.title("Coloring utility")
root.geometry("1280x720")
root.resizable(width = False, height = False)

pR = Entry(text = "Red porogue")
pG = Entry(text = "Green porogue")
pB = Entry(text = "blue porogue")


pRtext = Label(text = "Red porogue:")
pGtext = Label(text = "Green porogue:")
pBtext = Label(text = "blue porogue:")


result = Button(text = "Result")

result.grid(row = 5, column = 2)

pR.grid(row = 1, column = 2)
pG.grid(row = 2, column = 2)
pB.grid(row = 3, column = 2)

# downIMG = ImageTk.PhotoImage(Image.open("/Users/lev/Documents/GitHub/Kirill_Images/icon.jpg").resize((320, 240)))
# downIMGLable = Label(image = downIMG)
downIMGLable.grid(row = 6, column = 1)

pRtext.grid(row = 1, column = 1)
pGtext.grid(row = 2, column = 1)
pBtext.grid(row = 3, column = 1)

root.mainloop()
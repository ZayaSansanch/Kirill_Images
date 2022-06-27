from cProfile import label
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
# from PIL import ImageFilter

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
    filepath = filedialog()

root = Tk()
root.title("Coloring utility")
root.geometry("1280x720")
root.resizable(width = False, height = False)

fileOpen = Button(text = "File", command = openfile)

pR = Entry(text = "Red porogue")
pG = Entry(text = "Green porogue")
pB = Entry(text = "blue porogue")

sizeH = Entry(text = "Image height")
sizeW = Entry(text = "Image width")

pRtext = Label(text = "Red porogue:")
pGtext = Label(text = "Green porogue:")
pBtext = Label(text = "blue porogue:")

sizeHtext = Label(text = "Image height:")
sizeWtext = Label(text = "Image width:")

def showImages():
    downIMG = ImageTk.PhotoImage(Image.open("icon.jpg").resize((320, 240), Image.ANTIALIAS))
    downIMGLable = Label(image = downIMG)
    downIMGLable.grid(row = 8, column = 1)

result = Button(text = "Result", command = showImages)



fileOpen.grid(row = 1, column = 1)

result.grid(row = 7, column = 1)

pR.grid(row = 4, column = 2)
pG.grid(row = 5, column = 2)
pB.grid(row = 6, column = 2)
sizeH.grid(row = 2, column = 2)
sizeW.grid(row = 3, column = 2)

pRtext.grid(row = 4, column = 1)
pGtext.grid(row = 5, column = 1)
pBtext.grid(row = 6, column = 1)
sizeHtext.grid(row = 2, column = 1)
sizeWtext.grid(row = 3, column = 1)


root.mainloop()
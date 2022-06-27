from cProfile import label
from tkinter import *
from tkinter import filedialog
from unittest import result
from PIL import Image
# from PIL import ImageFilter

image = ""
filepath = ""
pixel = (0, 0, 0)
pixelRight = (0, 0, 0)
cmena = False
pR = 0
pG = 0
pb = 0

def openSave():
    image.save("result.png")
    image.show()

def openfile():
    filepath = filedialog.askopenfilename()
    image = Image.open("icon.jpg")

def result():
    openSave()

root = Tk()
root.title("Coloring utility")
root.geometry("1280x720")
root.resizable(width = False, height = False)

fileOpen = Button(text = "File", command=openfile)

pR = Entry(text = "Red porogue")
pG = Entry(text = "Green porogue")
pB = Entry(text = "blue porogue")

pRtext = label("Red porogue:")
pGtext = label("Green porogue:")
pBtext = label("blue porogue:")

result = Button(text = "result", command = result)

fileOpen.grid(row = 1, column = 1)
pR.grid(row = 2, column = 2)
pG.grid(row = 3, column = 2)
pB.grid(row = 4, column = 2)
pRtext.grid(row = 2, column = 1)
pGtext.grid(row = 3, column = 1)
pBtext.grid(row = 4, column = 1)
result.grid(row = 5, column = 1)

root.mainloop()
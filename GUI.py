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
filepath = ""
pixel = (0, 0, 0)
pixelRight = (0, 0, 0)
# cmena = False
pR = 0
pG = 0
pB = 0

def openfile():
    filepath = filedialog.askopenfile(title="Select file")
    print(filepath.read())

# def select_files():
filetypes = (
    ('IMG files', '*.jpg ' + '*,jpeg ' + '*.png '),
    # ('IMG files', '*.jpg'),
    ('All files', '*.*')
)

downfilenames = fd.askopenfilenames(
    title='Coloring utility/open file',
    initialdir='/',
    filetypes=filetypes)

upfilenames = fd.askopenfilenames(
    title='Coloring utility/save file',
    initialdir='/',
    filetypes=filetypes)

# showinfo(
#     title='Selected Files',
#     message=filenames
# )

curDir = os.getcwd()
fn = curDir

root = Tk()
print("Downfilenames: ", downfilenames[0], " Upfilenames", upfilenames[0])
downIMG = ImageTk.PhotoImage(Image.open(downfilenames[0]).resize((320, 240)))
downIMGLable = Label(image = downIMG)
# downIMGLable.grid(row = 8, column = 1)

# def upImage():
upIMG = ImageTk.PhotoImage(Image.open(downfilenames[0]).resize((320, 240)))
upIMGLable = Label(image = upIMG)
upIMGLable.grid(row = 6, column = 2)

root.title("Coloring utility")
root.geometry("1280x720")
root.resizable(width = False, height = False)

def get_value(entryWidget):
    value = entryWidget.get()
    try:
        return int(value)
    except ValueError:
        return None

def result():
    print("Working")
    upfilename = Image.open(upfilenames[0])
    for i in range(0, upfilename.size[0]):
        for j in range(0, upfilename.size[1]):
            cmena = False
            # Пиксели цвета (0, 0, 0) крашу в (1, 1, 1)
            if upfilename.getpixel((i, j)) == (0, 0, 0): upfilename.putpixel((i, j), (1, 1, 1))
            
            # Крашу линии
            pixel = upfilename.getpixel((i, j))
            if j < upfilename.size[1] - 1:
                pixelRight = upfilename.getpixel((i, j + 1))
            
            if abs(pixel[0] - pixelRight[0]) > get_value(pR): cmena = True
            if abs(pixel[1] - pixelRight[1]) > get_value(pG): cmena = True
            if abs(pixel[2] - pixelRight[2]) > get_value(pB): cmena = True

            if cmena == True:
                upfilename.putpixel((i, j), (0, 0, 0))
                cmena = False

            # Пиксели цвета > (0, 0, 0) крашу в (255, 255, 255)
            if upfilename.getpixel((i, j)) > (0, 0, 0): upfilename.putpixel((i, j), (255, 255, 255))
    # upfilename.save("result2")
    upfilename.show()

frame_parogue = Frame(root)
pR = Entry(text = "Red porogue")
pG = Entry(text = "Green porogue")
pB = Entry(text = "blue porogue")

pRtext = Label(text = "Red porogue:")
pGtext = Label(text = "Green porogue:")
pBtext = Label(text = "blue porogue:")

result = Button(text = "Result", command = result)

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
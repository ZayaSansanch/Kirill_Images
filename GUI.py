import tkinter

root = Tk()
root["bg"] = "#fafafa"
root.title = "Coloring utility"
root.wm_attributes("-alpha", 0.7)
root.geometry("640x480")
root.resizable(width = False, height = False)

canvas = Canvas(root, height = 480, width = 640)
canvas.pack()

root.mainloop()
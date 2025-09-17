from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("Image")
root.geometry("500x500")

upload = Image.open("img.jpg")

image = ImageTk.PhotoImage(upload)

label = Label(root, image=image)
label.place(x=50, y=0)
label2 = Label(root, text="This is an image")
label2.place(x=50, y=420)

root.mainloop()
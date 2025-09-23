from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root =  Tk()
root.title("Demonimation Counter")
root.configure(bg="lightblue")
root.geometry("650x400")

upload = Image.open("img.jpg")
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)
label = Label(root, image=image, bg='blue')
label.place(x=180, y=20)

label1 = Label(root, text="Hey User! Welcome to Demonimation Counter Application.",bg='lightblue')
label1.place(x=180,y=340)

def msg():
    MsgBox = messagebox.showinfo("Alert", "Do you want to calculate the denomination count?")
    if MsgBox == 'ok':
        topwin()

button1 = Button(root, text="Let's get started!", command=msg, bg='brown', fg='white')
button1.place(x=260, y=360)

def topwin():
    top = Toplevel()
    top.title("Denomination Counter")
    top.configure(bg="light grey")
    top.geometry("600x350")

    label = Label(top, text="Enter total amount", bg='light grey')
    entry = Entry(top)
    lbl = Label(top, text="Here are number of notes for each denomination", bg='light grey')

    l1=Label(top, text="2000", bg='light grey')
    l2=Label(top, text="500", bg='light grey')
    l3=Label(top, text="100", bg='light grey')
    l4=Label(top, text="10", bg='light grey')
    l5=Label(top, text="1", bg='light grey')

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)
    t4 = Entry(top)
    t5 = Entry(top)

    def calculator():
        try:
            global amount
            amount = int(entry.get())
            note2000=amount//2000
            amount %= 2000
            note500=amount//500
            amount %= 500
            note100=amount//100
            amount %= 100
            note10=amount//10
            amount %= 10
            note1=amount//1
            
            t1.delete(0, END)
            t2.delete(0, END)
            t3.delete(0, END)
            t4.delete(0, END)
            t5.delete(0, END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note100))
            t4.insert(END, str(note10))
            t5.insert(END, str(note1))
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid number.")

    btn = Button(top, text="Calculate", command=calculator, bg='brown', fg='white')

    label.place(x=200,y=50)
    entry.place(x=200,y=80)
    btn.place(x=240,y=120)
    lbl.place(x=140,y=170)

    l1.place(x=180,y=200)
    l2.place(x=180,y=230)
    l3.place(x=180,y=260)
    l4.place(x=180,y=290)
    l5.place(x=180,y=320)

    t1.place(x=270,y=200)
    t2.place(x=270,y=230)
    t3.place(x=270,y=260)
    t4.place(x=270,y=290)
    t5.place(x=270,y=320)

    top.mainloop()

root.mainloop()
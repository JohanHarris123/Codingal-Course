import tkinter as tk

window = tk.Tk()
window.title("Tkinter Button Example")
window.geometry('200x200')
window.configure(bg='lightblue')

for i in range(2):
    for j in range(2):
        button = tk.Button(text=f"Button {i+1}", fg='white', bg='black')
        button.place(x=0 + j*145, y=0 + i*175)

window.mainloop()
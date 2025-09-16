import tkinter as tk

window = tk.Tk()

def draw_grid(i,j):
    frame = tk.Frame(master=window, relief=tk.RAISED, borderwidth=5)
    frame.grid(row=i, column=j, padx=3, pady=3)
    label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}")
    label.pack()

gridsize = 15
for i in range(gridsize+1):
    for j in range(gridsize+1):
        if i == 0 or j == 0 or i == gridsize or j == gridsize:
            draw_grid(i,j)

window.mainloop()
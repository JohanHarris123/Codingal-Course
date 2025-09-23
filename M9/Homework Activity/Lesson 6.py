import tkinter as tk
import random

def play(user_choice):
    computer_choice = random.choice(['Rock', 'Paper', 'Scissors'])
    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (user_choice, computer_choice) in [('Rock', 'Scissors'), ('Paper', 'Rock'), ('Scissors', 'Paper')]:
        result = "You Win!"
    else:
        result = "You Lose!"
    result_label.config(text=f"Your: {user_choice}\nComputer: {computer_choice}\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x200")
root.configure(bg="lightgreen")

label = tk.Label(root, text="Choose Rock, Paper, or Scissors:", bg="lightgreen").pack(pady=10)

result_label = tk.Label(root, text="", bg="lightgreen")
b1 = tk.Button(root, text="Rock", command=lambda:play('Rock')).pack()
b2 = tk.Button(root, text="Paper", command=lambda:play('Paper')).pack()
b3 = tk.Button(root, text="Scissors", command=lambda:play('Scissors')).pack()
result_label.pack(pady=10)

root.mainloop()

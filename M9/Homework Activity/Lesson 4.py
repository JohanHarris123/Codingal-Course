import tkinter as tk
import random as r

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"

def generate_password():
    user_input = entry_length.get()
    if not user_input.isdigit():
        output["text"] = "Please enter a number."
        output["fg"] = "red"
        return
    
    length = int(user_input)
    if length < 8:
        output["text"] = "Password must be at least 8 characters."
        output["fg"] = "red"
    else:
        password = ''.join(r.choices(chars, k=length))
        output["text"] = f"Your password: {password}"
        output["fg"] = "green"

root = tk.Tk()
root.title("Password Generator")

label = tk.Label(root, text="Enter password length (min 8):")
label.pack(pady=5)

entry_length = tk.Entry(root)
entry_length.pack(pady=5)

generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=10)

output = tk.Label(root, text="")
output.pack(pady=10)

exit_btn = tk.Button(root, text="Exit", command=root.quit)
exit_btn.pack(pady=5)

root.mainloop()

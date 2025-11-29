import tkinter as tk
from datetime import datetime


LOG_FILE = "keylog_simulation.txt"
def log_key(event):
    key = event.char  


    if event.keysym == "BackSpace":
        key = "[BACKSPACE]"
    elif event.keysym == "Return":
        key = "[ENTER]"
    elif event.keysym == "Tab":
        key = "[TAB]"
    elif event.keysym == "Shift_L" or event.keysym == "Shift_R":
        key = "[SHIFT]"
    elif event.keysym == "Control_L" or event.keysym == "Control_R":
        key = "[CTRL]"
    elif event.char == "":
        key = f"[{event.keysym.upper()}]"

   
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.now()} - {key}\n")

  
    text_box.insert(tk.END, key)

root = tk.Tk()
root.title("Keylogger Simulation (Safe)")

label = tk.Label(root, text="Type here. Keys will be logged safely:")
label.pack()

text_box = tk.Text(root, height=10, width=50)
text_box.pack()


root.bind("<Key>", log_key)

root.mainloop()

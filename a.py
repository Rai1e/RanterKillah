import tkinter as tk
from tkinter import messagebox
import pyautogui
import time
import threading

def start_burst():
    msg = text_box.get("1.0", tk.END).strip()
    try:
        count = int(entry_count.get())
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number of bursts.")
        return

    if not msg:
        messagebox.showwarning("Warning", "Please type a message first!")
        return

    # Get speed from dropdown
    speed_choice = speed_var.get()
    if speed_choice == "Fast":
        delay = 0.05  # 50 ms
    elif speed_choice == "Normal":
        delay = 0.2  # 200 ms
    else:  # Slow
        delay = 0.5  # 500 ms

    def worker():
        time.sleep(3)  # give time to switch to target app
        for i in range(count):
            pyautogui.typewrite(msg)
            pyautogui.press("enter")
            time.sleep(delay)

    threading.Thread(target=worker, daemon=True).start()
    messagebox.showinfo("Ready", f"Switch to the app where you want to send.\nBurst will start in 3 seconds.")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Burst Typer")
root.geometry("400x350")

tk.Label(root, text="Type your message:").pack(pady=5)
text_box = tk.Text(root, height=5, width=40)
text_box.pack(padx=10, pady=5)

tk.Label(root, text="Number of bursts:").pack()
entry_count = tk.Entry(root)
entry_count.insert(0, "5")  # default value
entry_count.pack(pady=5)

tk.Label(root, text="Speed:").pack(pady=5)
speed_var = tk.StringVar(value="Normal")
speed_menu = tk.OptionMenu(root, speed_var, "Fast", "Normal", "Slow")
speed_menu.pack()

tk.Button(root, text="Start Burst", command=start_burst, bg="green", fg="white").pack(pady=15)

root.mainloop()

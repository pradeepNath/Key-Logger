import tkinter as tk
from pynput import keyboard

logging=False
listener=None

def on_press(key):
    if listener:
        try:
            text_box.insert(tk.END,(f"{key.char}"))
        except:
            text_box.insert(tk.END,(f"{key}"))

        text_box.see(tk.END)

def start_logger():
    global logging,listener
    logging=True
    status_label.config(text="Status: Logging")
    listener=keyboard.Listener(on_press=on_press)
    listener.start()

def stop_logger():
    global logging,listener
    logging=False
    status_label.config(text="Status: Stopped")
    if listener:
        listener.stop()


root=tk.Tk()
root.title("Key Logger")
root.geometry("500x500")

status_label=tk.Label(root,text="Status: Stopped")
status_label.pack()

text_box=tk.Text(root,height=20)
text_box.pack(padx=10,pady=10)

tk.Button(root,text="Start Logging",command=start_logger,width=20).pack(pady=10)
tk.Button(root,text="Stop Logging",command=stop_logger,width=20).pack(pady=10)
tk.Button(root,text="Exit",command=root.destroy,width=20).pack(pady=10)

root.mainloop()
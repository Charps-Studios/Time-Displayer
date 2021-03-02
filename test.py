import time, threading
import tkinter as tk

def time_loop_func():
    global b

    for i in range(1, 11):
        b['text'] = str(i)
        time.sleep(1)

print("test1")

root = tk.Tk()

b = tk.Button(root, text = "N/A", command = root.destroy, bd = 0, bg = "black", fg = "white")
b.pack()

#Starts the time checking thread/loop
time_loop = threading.Thread(target = time_loop_func)
time_loop.start()

root.mainloop()

print("test2")
from tkinter import *
import tkinter.font as font
import time, threading

def time_loop_func():
    global w
    while True:
        w['text'] = time.strftime("%I:%M", time.localtime())
        time.sleep(1)

w, h = 60, 35

root = Tk()

root.title("Time")
root.overrideredirect(True)
root.geometry("{w}x{h}+{x}+{y}".format(w = w, h = h, x = -1, y = root.winfo_screenheight() - h))
root.configure(bg='black')

#Text for time
w = Button(root, text="N/A", command=root.destroy, bd=0, bg="black", fg="white")
w['font'] = font.Font(family='Segoe UI Light')
w.pack()

root.attributes('-topmost', True)
root.attributes('-alpha', 0.75)

time_loop = threading.Thread(target=time_loop_func)
time_loop.start()

root.mainloop()

time_loop.join()
from tkinter import *
import tkinter.font as font
import time, threading

def time_loop_func():
    global w
    while True:
        w['text'] = time.strftime("%I:%M", time.localtime())
        time.sleep(1)

root = Tk()

root.title("Time")
root.overrideredirect(True)
root.geometry("60x60+{w}+{h}".format(w = 0, h =root.winfo_screenheight() - 60))
root.configure(bg='black')

w, h = 50, 50

canvas = Canvas(root, width=0, height=0, highlightthickness=0)
canvas.pack(fill='both')

#Text for time
w = Label(root, text="N/A", bg="black", fg="white")
w['font'] = font.Font(family='Segoe UI Light')
w.pack()

# Button for closing 
exit_button = Button(root, text="Exit", command=root.destroy, bd=0, bg="black", fg="white") 
exit_button.pack(pady=0) 

root.attributes('-topmost', True)
root.attributes('-alpha', 0.75)

time_loop = threading.Thread(target=time_loop_func)
time_loop.start()

root.mainloop()
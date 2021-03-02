from tkinter import *
import tkinter.font as font
import time, threading, json
import ctypes
 
ctypes.windll.shcore.SetProcessDpiAwareness(1)

#Updates the time displayer with the correct time.
def time_loop_func():
    global b
    while True:
        b['text'] = time.strftime("%I:%M", time.localtime())
        time.sleep(1)

#Opens the right click menu
def openMenu(event):
    try: 
        main_menu.tk_popup(event.x_root, event.y_root) 
    finally: 
        main_menu.grab_release() 

#Updates what side the displayer should be on
def setSide(horizontal, vertical):    
    data = json.loads(open("side.json").read())
    f = open("side.json", "a")
    f.truncate(0)

    if horizontal == 0: 
        x = -1
        data["x"] = horizontal
    elif horizontal == 1: 
        x = root.winfo_screenwidth() - w
        data["x"] = horizontal

    if vertical == 0: 
        y = -1
        data["y"] = vertical
    elif vertical == 1: 
        y = root.winfo_screenheight() - h
        data["y"] = vertical
        
    root.geometry("{w}x{h}+{x}+{y}".format(w = w, h = h, x = x, y = y))

    print(json.dumps(data))
    f.writelines(json.dumps(data))
    f.close()

root = Tk()

w, h = 120, 70
x, y = 0, 0

#Reads from the side file to see where the time displayer should be
try:
    f = open("side.json", "r+")
    data = json.loads(f.read())
    f.close()

    if data["x"] == 0: x = -1
    elif data["x"] == 1: x = root.winfo_screenwidth() - w
    if data["y"] == 0: y = -1
    elif data["y"] == 1: y = root.winfo_screenheight() - h
    print(data)
    print(w, y)
except FileNotFoundError:
    x = -1
    y = root.winfo_screenheight() - h

    f = open("side.json", "a")
    f.write("{\n     \"x\": 0,\n     \"y\": 0\n}")
    f.close()

#Creates the window
root.title("Time")
root.overrideredirect(True)
root.geometry("{w}x{h}+{x}+{y}".format(w = w, h = h, x = x, y = y))
root.configure(bg = 'black')

#Text for time
b = Button(root, text = "N/A", command = root.destroy, width = w, bd = 0, bg = "black", fg = "white")
b['font'] = font.Font(family = 'Segoe UI Light', size = 15)
b.pack()
b.bind("<Button-3>", openMenu)

#Right click menu
sides_menu = Menu(root, tearoff=0)
sides_menu.add_command(label = "Top Left", command = lambda: setSide(0, 0))
sides_menu.add_command(label = "Top Right", command = lambda: setSide(1, 0))
sides_menu.add_separator()
sides_menu.add_command(label = "Bottom Left", command = lambda: setSide(0, 1))
sides_menu.add_command(label = "Bottom Right", command = lambda: setSide(1, 1))

main_menu = Menu(root, tearoff=0)
main_menu.add_cascade(label = "Set Side...", menu = sides_menu)
main_menu.add_command(label = "Exit", command = root.quit)

#Sets attributes of the window.
root.attributes('-topmost', True)
root.attributes('-alpha', 0.75)

#Starts the time checking thread/loop
time_loop = threading.Thread(target = time_loop_func)
time_loop.start()

#Starts the main loop
root.mainloop()

#Waits for the time checking loop to stop.
time_loop.join()
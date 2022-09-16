import tkinter as tk
from tkinter import filedialog, Text, NW
from PIL import ImageTk,Image
import os

root = tk.Tk()
apps=[]

if os.path.isfile('save.txt'):
    with open('save.txt','r') as f:
        tempApps = f.read() 
        tempApps = tempApps.split(',')
        print(tempApps)
        apps=[x for x in  tempApps if x.strip()]

def addApp():

    for widget in frame.winfo_children():
        widget.destroy()

    filename=filedialog.askopenfilename(initialdir="/",title="select file",filetypes=(("python","&.py"),("executables","&.exe"),("all files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label=tk.Label(frame, text=app,bg="gray")
        label.pack()

def runJarvis():
    for app in apps:
        os.startfile(app)




root.title("Jarvis")
Canvas = tk.Canvas(root,height=300,width=400,bg="#263D42")
Canvas.pack()
root.iconbitmap(r'download.ico')


"""
my_img = ImageTk.PhotoImage(Image.open("download.ico"))
my_label= tk.Label(image=my_img)
my_label.pack()
"""

#img = tk.PhotoImage(file='C:\\Users\\monesh\\Downloads\\download.png')
#Canvas.create_image(0,0, anchor = NW, imag=img)
frame = tk.Frame(root,bg="gray")#C:\\Users\\monesh\\Downloads\\download.png")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

openfile=tk.Button(root,text="Open File",padx=10,pady=5,fg="white",bg="#263D42",command = addApp)
openfile.pack()

runapps=tk.Button(root,text="Run Jarvis",padx=10,pady=5,fg="white",bg="#263D42",command = runJarvis)
runapps.pack()

button_quit = tk.Button(root,text="Exit Program",padx=10,pady=5,fg="white",bg="#263D42",command = root.quit)
button_quit.pack()

for app in apps:
    label = tk.Label(frame, text=app)



root.mainloop()


with open('save.txt','w') as f:
    for app in apps:
        f.write(app +',')





"""
    for widget in frame.winfo_children():
        widget.destroy()

    filename=filedialog.askopenfilename(initialdir="/",title="select file",filetypes=(("python","&.py"),("executables","&.exe"),("all files","*.*")))
    apps.append(filename)
    print(filename)
    for app in apps:
        label=tk.Label(frame, text=app,bg="gray")
        label.pack()

def runApps():
    for app in apps:
        os.startfile(app)




root.title("Jarvis")
Canvas = tk.Canvas(root,height=300,width=400,bg="#263D42")
Canvas.pack()
root.iconbitmap(r'download.ico')
"""


my_img = ImageTk.PhotoImage(Image.open("download.ico"))
my_label= tk.Label(image=my_img)
my_label.pack()


"""
#img = tk.PhotoImage(file='C:\\Users\\monesh\\Downloads\\download.png')
#Canvas.create_image(0,0, anchor = NW, imag=img)
frame = tk.Frame(root,bg="gray")#C:\\Users\\monesh\\Downloads\\download.png")
frame.place(relwidth=0.8,relheight=0.8,relx=0.1,rely=0.1)

openfile=tk.Button(root,text="Open File",padx=10,pady=5,fg="white",bg="#263D42",command = addApp)
openfile.pack()

runapps=tk.Button(root,text="Run Jarvis",padx=10,pady=5,fg="white",bg="#263D42",command = runApps)
runapps.pack()

button_quit = tk.Button(root,text="Exit Program",padx=10,pady=5,fg="white",bg="#263D42",command = root.quit)
button_quit.pack()

for app in apps:
    label = tk.Label(frame, text=app)



root.mainloop()


with open('save.txt','w') as f:
    for app in apps:
        f.write(app +',')
"""

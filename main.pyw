import tkinter as tk
from tkinter import messagebox,ttk
from tkinter import filedialog as fd
import sys
from datetime import datetime

from PIL import Image
from pathlib import Path
import win32com.client
import os






xy=""
x=""

konumpng=""
konum=""

shell = win32com.client.Dispatch("WScript.Shell")
root=tk.Tk()

l = tk.Label(root, text = "IcoGeneral v1.0")
l.config(font =("Courier", 14))
l.pack()
home=os.environ['USERPROFILE']
if not os.path.exists(home+"\\AppData\\Local\\IcoGeneral"):
    os.makedirs(home+"\\AppData\\Local\\IcoGeneral\\")
konumsave=(home+"\\AppData\\Local\\IcoGeneral\\")
root.title("IcoGeneral v1.0 -Sarmsak Portable Utilities by Arsarimsak-")
root.geometry('500x180')


#pyinstallericin: auto-py-to-exe ile calistir ikonu direk roota . ile ekle ve ikon secenekden de ekle
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

iconPath = resource_path('icon.ico')
root.iconbitmap(iconPath)
#pyinstaller bitis




def resimsec():
    now = datetime.now()
    konumpng = fd.askopenfilename(title='Open a photo',initialdir='/',filetypes=[("Supported files", "*.png *.jpg *.jpeg *.tiff *.bmp *.gif *.ppm"), ('All files', '*.*')])
    logo = Image.open(konumpng)
    global x
    global y
    x = now.strftime("%d%m%Y%H%M%S")
    xy=x
    x=(x+".ico")
    logo.save(konumsave+x, format ='ICO',sizes=[(256, 256)])

def programsec():
    konumdosya = fd.askopenfilename(title='Open a file',initialdir='/',filetypes=[('All files', '*.*')])

    shortcut = shell.CreateShortcut(home+"\\desktop\\"+os.path.basename(konumdosya).split('\\')[-1]+".lnk")
    shortcut.TargetPath = (konumdosya)
    print(home+"\\AppData\\Local\\IcoGeneral\\"+x+",1")
    #shortcut.IconLocation = (home+"\\AppData\\Local\\IcoGeneral\\"+x+",1")
    shortcut.IconLocation = (home + "\\AppData\\Local\\IcoGeneral\\" + x )
    shortcut.Save()
def kisayolsec():
    konum = fd.askopenfilename(title='Open a shortcut',initialdir='/',filetypes=[('Shortcut files', '*.lnk')])

def klasorsec():
    konumdosya = fd.askdirectory(title='Open a folder',initialdir='/')

    with open(konumdosya+"/desktop.ini", 'w') as fp:
        fp.write("[.ShellClassInfo]" + "\n")
        fp.write("IconResource=" + home + "\\AppData\\Local\\IcoGeneral\\" + x + ",0")


    aa=("attrib +h +s "+'"'  +konumdosya+'"' +"/desktop.ini")

    os.system(aa)


open_button1 = ttk.Button(root,text='Open a Photo for Icon',command=resimsec)
open_button1.pack(expand=True)

open_button0 = ttk.Button(root,text='Create an Application/File Shortcut to the Desktop',command=programsec)
open_button0.pack(expand=True)



#open_button2 = ttk.Button(root,text='Open a Shortcut',command=kisayolsec)
#open_button2.pack(expand=True)

open_button3 = ttk.Button(root,text='Change a Folder Icon',command=klasorsec)
open_button3.pack(expand=True)

root.mainloop()


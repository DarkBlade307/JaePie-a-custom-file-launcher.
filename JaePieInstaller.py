#JaePie Installer V1.0
#Importing
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
import os
#Definitions:
#This is the installation function
def install():
    os.mkdir('JaePie V1.0')
    os.mkdir('JaePie V1.0\\importantfiles')
    os.mkdir('JaePie V1.0\\programs')
    f= open('JaePie V1.0\\importantfiles\\numberone.txt', 'w')
    f.write('unassigned')
    f.close()
    f= open('JaePie V1.0\\importantfiles\\numbertwo.txt', 'w')
    f.write('unassigned')
    f.close()
    f= open('JaePie V1.0\\importantfiles\\numberthree.txt', 'w')
    f.write('unassigned')
    f.close()
    f= open('JaePie V1.0\\JaePie V1.0.txt', 'w')
    f.write('f= open("importantfiles\\\\numberone.txt", "r")\n')
    f.write('b1t = f.read()\n')
    f.write('f.close()\n')
    f.write('f= open("importantfiles\\\\numbertwo.txt", "r")\n')
    f.write('b2t = f.read()\n')
    f.write('f.close()\n')
    f.write('f= open("importantfiles\\\\numberthree.txt", "r")\n')
    f.write('b3t = f.read()\n')
    f.write('f.close()\n')
    f.write('#Imports\nfrom tkinter import ttk\nfrom tkinter import filedialog\nimport os\nfrom tkinter import *\nfrom tkinter import messagebox\nfrom tkinter.ttk import Progressbar\n')
    f.write('#Definitions\ndef runone():\n    f= open("importantfiles\\\\numberone.txt", "r")\n    runner = f.read()\n    f.close()\n    os.startfile("programs\\\\" + runner)\n')
    f.write('def runtwo():\n    f= open("importantfiles\\\\numbertwo.txt", "r")\n    runner = f.read()\n    f.close()\n    os.startfile("programs\\\\" + runner)\n')
    f.write('def runthree():\n    f= open("importantfiles\\\\numberthree.txt", "r")\n    runner = f.read()\n    f.close()\n    os.startfile("programs\\\\" + runner)\n')
    f.write('def setone():\n    one = assigner.get()\n    f= open("importantfiles\\\\numberone.txt", "w")\n    f.write(one)\n    f.close()\n')
    f.write('def settwo():\n    two = assigner.get()\n    f= open("importantfiles\\\\numbertwo.txt", "w")\n    f.write(two)\n    f.close()\n')
    f.write('def setthree():\n    three = assigner.get()\n    f= open("importantfiles\\\\numberthree.txt", "w")\n    f.write(three)\n    f.close()\n')
    f.write('window = Tk()\n')
    f.write('window.title("JaePie V1.0")\n')
    f.write('tab_control = ttk.Notebook(window)\n')
    f.write('tab1 = ttk.Frame(tab_control)\n')
    f.write('tab_control.add(tab1, text="Launcher")\n')
    f.write('tab2 = ttk.Frame(tab_control)\n')
    f.write('tab_control.add(tab2, text="Button Assignment")\n')
    f.write('tab_control.pack(expand=1, fill="both")\n')
    f.write('buttonone = Button(tab1, text=b1t, bg="blue", fg="white", command=runone)\n')
    f.write('buttontwo = Button(tab1, text=b2t, bg="red", fg="white", command=runtwo)\n')
    f.write('buttonthree = Button(tab1, text=b3t, bg="green", fg="white", command=runthree)\n')
    f.write('buttonfour = Button(tab2, text="Assign button one", bg="blue", fg="white", command=setone)\n')
    f.write('buttonfive = Button(tab2, text="Assign button two", bg="red", fg="white", command=settwo)\n')
    f.write('buttonsix = Button(tab2, text="Assign button three", bg="green", fg="white", command=setthree)\n')
    f.write('buttonone.grid(column=0, row=0)\n')
    f.write('buttontwo.grid(column=0, row=1)\n')
    f.write('buttonthree.grid(column=0, row=2)\n')
    f.write('buttonfour.grid(column=0, row=0)\n')
    f.write('buttonfive.grid(column=0, row=1)\n')
    f.write('buttonsix.grid(column=0, row=2)\n')
    f.write('assigner = Entry(tab2, width=20)\n')
    f.write('assigner.grid(column=1, row=0)\n')
    f.close()
    os.rename('JaePie V1.0\\JaePie V1.0.txt', 'JaePie V1.0\\JaePie V1.0.py')
    messagebox.showinfo("Complete", "The installation is complete, you may close the installer.")
#Object assignments:
#The main window
window = Tk()
#The first piece of text
lbl = Label(window, text='This is the JaePie installer for JaePie version 1, if this is not the version you were looking for, please look for the updated version from where you downloaded this version.\n')
#The second piece of text
#The install button
installbutton = Button(window, text="Install now", bg="white", fg="blue", command=install)
#The input box where you set your filepath
filepathset = Entry(window, width=60)

#Assemblement:
window.title("JaePie Installer")
lbl.grid(column=0, row=0)
window.geometry('1000x200')
installbutton.grid(column=0, row=2)
window.mainloop()


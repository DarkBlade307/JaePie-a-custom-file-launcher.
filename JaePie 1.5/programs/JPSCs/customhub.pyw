from tkinter import ttk
from tkinter import filedialog
import os
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Progressbar
from tkinter import Menu
#Window setup
window = Tk()
window.title("Customisation Hub")
window.geometry("500x500")
#Tabs:
#Tab setup
tab_control = ttk.Notebook(window)
tab_control.pack(expand=2, fill="both")
#Tab one scripts/ Tab one setup/ Tab one content
#scripts
def saveone():
    txt1 = onetext.get()
    col1 = onecolour.get()
    nik1 = onenickname.get()
    f= open("styles\\buttononetext.txt", "w")
    f.write(nik1)
    f.close()
    f= open("styles\\buttononecolour.txt", "w")
    f.write(col1)
    f.close()
    f= open("styles\\tc1.txt", "w")
    f.write(txt1)
    f.close()
#setup
tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Button One:")
#content
butonecol = Label(tab1, text="Button one background colour:")
butonecol.grid(column=0, row=0)
onecolour = Entry(tab1, width=20)
onecolour.grid(column=1, row=0)
butonenick = Label(tab1, text="Button one nickname:")
butonenick.grid(column=0, row=1)
onenickname = Entry(tab1, width=20)
onenickname.grid(column=1, row=1)
butonetext = Label(tab1, text="Button one text colour:")
butonetext.grid(column=0, row=2)
onetext = Entry(tab1, width=20)
onetext.grid(column=1, row=2)
onesave = Button(tab1, text="Save changes", command=saveone)
onesave.grid(column=0, row=3)
#Tab two scripts/ Tab two setup/ Tab two content
#scripts
def savetwo():
    txt2 = onetext.get()
    col2 = onecolour.get()
    nik2 = onenickname.get()
    f= open("styles\\buttontwotext.txt", "w")
    f.write(nik2)
    f.close()
    f= open("styles\\buttontwocolour.txt", "w")
    f.write(col2)
    f.close()
    f= open("styles\\tc2.txt", "w")
    f.write(txt2)
    f.close()
#setup
tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Button Two:")
#content
buttwocol = Label(tab2, text="Button two background colour:")
buttwocol.grid(column=0, row=0)
twocolour = Entry(tab2, width=20)
twocolour.grid(column=1, row=0)
buttwonick = Label(tab2, text="Button two nickname:")
buttwonick.grid(column=0, row=1)
twonickname = Entry(tab2, width=20)
twonickname.grid(column=1, row=1)
buttwotext = Label(tab2, text="Button two text colour:")
buttwotext.grid(column=0, row=2)
twotext = Entry(tab2, width=20)
twotext.grid(column=1, row=2)
twosave = Button(tab2, text="Save changes", command=savetwo)
twosave.grid(column=0, row=3)
#Tab three scripts/ Tab three setup/ Tab three content
#scripts
def savethree():
    txt3 = threetext.get()
    col3 = threecolour.get()
    nik3 = threenickname.get()
    f= open("styles\\buttonthreetext.txt", "w")
    f.write(nik3)
    f.close()
    f= open("styles\\buttonthreecolour.txt", "w")
    f.write(col3)
    f.close()
    f= open("styles\\tc3.txt", "w")
    f.write(txt3)
    f.close()
#setup
tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text="Button Three:")
#content
butthreecol = Label(tab3, text="Button three background colour:")
butthreecol.grid(column=0, row=0)
threecolour = Entry(tab3, width=20)
threecolour.grid(column=1, row=0)
butthreenick = Label(tab3, text="Button three nickname:")
butthreenick.grid(column=0, row=1)
threenickname = Entry(tab3, width=20)
threenickname.grid(column=1, row=1)
butthreetext = Label(tab3, text="Button three text colour:")
butthreetext.grid(column=0, row=2)
threetext = Entry(tab3, width=20)
threetext.grid(column=1, row=2)
threesave = Button(tab3, text="Save changes", command=savethree)
threesave.grid(column=0, row=3)


window.mainloop()

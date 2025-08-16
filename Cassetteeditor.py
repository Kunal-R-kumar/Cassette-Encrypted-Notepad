from tkinter import *
from tkinter import messagebox
import Cassettemain,os,csv

def encode(name,add):
    ab=''
    for i in name.strip():
       ab+=chr(ord(i)+add)     
    return ab
def decode(name,sub):
    ab=''
    for i in name:
       ab+=chr(ord(i)-sub)
    return ab
def main(a,be):
    main=open('E:\\Cassette\\do_not_open.csv')
    mainr=csv.reader(main)
    for i in mainr:
        if be==i[0][3:]:
            mainpass=len(i[1])    
    fmain = Tk()
    fmain.title("Untitled - cassette")
    fmain.attributes("-fullscreen",True)
    def openf():
        file = a
        TextArea.delete(1.0, END)
        f = open(file, "r")
        TextArea.insert(1.0, decode(f.read(),mainpass))
        f.close()
    def savef():
            f = open(a, "w")
            f.write(encode(TextArea.get(1.0, END),mainpass))
            f.close()

    def about():
        messagebox.showinfo("cassette", "cassette designed by Kunal\nFeel Secured")
    def quitt():
        m=messagebox.askokcancel("alert","Are you sure you want to Quit",icon="warning")
        if m==True:
            quit()
    TextArea = Text(fmain, font="Times 17")
    openf()
    TextArea.pack(expand=True, fill=BOTH)
    MenuBar = Menu(fmain)
    FileMenu = Menu(MenuBar, tearoff=0)
    def menu():
        fmain.destroy()
        Cassettemain.main(be)
    FileMenu.add_command(label="Menu", command = menu)
    FileMenu.add_command(label = "Save",command=savef)
    FileMenu.add_separator()
    FileMenu.add_command(label = "Exit", command = quitt)
    MenuBar.add_cascade(label = "File", menu=FileMenu)
    EditMenu = Menu(MenuBar, tearoff=0)
    # EditMenu.add_command(label = "Rename file",)
    def delete():
        m=messagebox.askokcancel("alert","Are you sure you want to delete the file",icon="warning")
        if m==True:
            deletee()
    def deletee():
        fmain.destroy()
        os.remove(a)
        Cassettemain.main(be)
    EditMenu.add_command(label = "Delete file ", command=delete)
    MenuBar.add_cascade(label="Edit", menu = EditMenu)
    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label = "About cassette", command=about)
    MenuBar.add_cascade(label="About", menu=HelpMenu)
    fmain.config(menu=MenuBar)

    Scroll = Scrollbar(TextArea)
    Scroll.pack(side=RIGHT,  fill=Y)
    Scroll.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=Scroll.set)

    def exit(event):
        quitt()
    def save(event):
        savef()
    def menuu(event):
        menu()
    def aboutt(event):
        about()
    def dell(event):
        delete
    fmain.bind("<Alt-x>",exit)
    fmain.bind("<Alt-s>",save)
    fmain.bind("<Alt-m>",menuu)
    fmain.bind("<Alt-a>",aboutt)
    fmain.bind("<Alt-d>",dell)
    fmain.mainloop()
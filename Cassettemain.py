from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import os
import Cassetteeditor
def quitt():
    m=messagebox.askokcancel("alert","Are you sure you want to Quit",icon="warning")
    if m==True:
        quit()
def main(a):
    def switchopen(be):
        cwin.destroy()
        Cassetteeditor.main(f"E:\\Cassette\\file\\{a}\\{be}",a)
    cwin=Tk()
    filelist=[]
    cwin.title("Cassetee Main Window")
    cwin.attributes("-fullscreen",True)
    f=Frame(cwin).pack(expand=True)
    Label(f,text="").pack(anchor=E)
    cmenu=Menu(cwin)
    cwin.config(menu=cmenu)
    cmenu.add_command(label="Quit",font=("Times",20),compound=RIGHT,command=quitt)
    sw = cwin.winfo_screenwidth()
    sh = cwin.winfo_screenheight()
    q=Image.open("E:\\vscode\\clgproj\\fileimg.png").resize((50,50))
    q=ImageTk.PhotoImage(q)
    scroll=Scrollbar(cwin)
    scroll.pack(side=RIGHT,fill=Y)
    Label(cwin,text="").pack(side=LEFT,fill=Y)
    text=Text(cwin,width=sw,height=sh,background="#141414",font=("Times Bold",18),yscrollcommand=scroll.set)
    text.pack()
    text.configure(cursor="arrow",state=DISABLED)
    filelist=os.listdir("E:\\Cassette\\file\\"+a)  

    class Que(Tk):
        def __init__(self,abc):
            def click():
                v=self.b.cget('text')
                switchopen(v)
                
            self.b=Button(cwin,image=q,compound=TOP,text=f"{abc}", command=click,padx=4, pady=4,bg="#5a72d1",fg="white")
            text.window_create("end", window=self.b, padx=10, pady=10)
    for i in filelist:
        widget=Que(i)
    pl=Image.open("E:\\vscode\\clgproj\\plus.png").resize((50,50))
    pl=ImageTk.PhotoImage(pl)
    
    def add_new():
        def remove():
            if e.get().strip()=='':
                text.nametowidget(eb).destroy()
                text.nametowidget(e).destroy()
            elif (e.get()) in filelist:
                e.delete(0,"end")
                e.focus_set()
            else:
                opnn=open(f"E:\\Cassette\\file\\{a}\\{e.get()}",'a')
                opnn.close()
                filelist.append(e.get())
                ab=Que(e.get())
                text.nametowidget(eb).destroy()
                text.nametowidget(e).destroy()
        e=Entry(width=10)
        text.window_create("end", window=e, padx=10, pady=10)
        eb=Button(cwin,text="Add",bg="#5a72d1",fg="white",command=remove)
        text.window_create("end", window=eb, padx=10, pady=10)

    add = Button(cwin, image=pl,compound=TOP,bg="#141414",fg="white",text="New",font=("Times",12),padx=4, pady=4,command=add_new)
    text.window_create(1.0, window=add, padx=10, pady=10) 
    scroll.config(command=text.yview)
    def quittt(event):
        quitt()
    cwin.bind("<Alt-x>",quittt)
    cwin.mainloop()

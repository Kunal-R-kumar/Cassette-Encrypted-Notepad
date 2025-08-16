from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
from tkcalendar import Calendar
from random import randint
import os,csv,subprocess,Cassettemain
nmlst=[]
#Encode&decoder
def pssen(a):
    e=0
    f=''
    for i in a :
        if i!='_':
            f+=i
        else:
            e+=int(f)
            f=''
    return e

def encode(a):
    e=''
    for i in a:
        e+=(str(ord(i))+'_')
    return e
def decoder(a):
    e=''
    f=''
    for i in a :
        if i!='_':
            f+=i
        else:
            e+=chr(int(f))
            f=''
    return e
#main file creation
direc=os.path.isdir('E:\\Cassette')
if direc == False:
    os.mkdir('E:\\Cassette')
subdirec=os.path.isdir("E:\\Cassette\\file")
if subdirec == False:
    os.mkdir('E:\\Cassette\\file')
files=os.path.isfile('E:\\Cassette\\do_not_open.csv')
if files==False:
    a=open('E:\\Cassette\\do_not_open.csv','a',newline='')
    a.close()
else:
    f=open('E:\\Cassette\\do_not_open.csv')
    fr=csv.reader(f)
    for i in fr:
        nmlst.append(decoder(i[0][3:]))
    f.close()
lwin=Tk()
dt=IntVar()
dt.set(0)
lwin.title("Cassette New User Page")
lwin.attributes("-fullscreen",True)
sw = lwin.winfo_screenwidth()
sh = lwin.winfo_screenheight()
imgc = Image.open("E:\\vscode\\clgproj\\cni.png").resize((sw,sh))
img=imgc.copy().save("E:\\vscode\\clgproj\\cni.png")
img = PhotoImage(file="E:\\vscode\\clgproj\\cni.png")
bg=Label(lwin,image = img)
bg.pack(fill="both",expand=True)
#username
def nxt(event):
        e2.focus_set()
def fin(event):
    if e1.get().strip()=="Enter Username...":
        e1.delete(0,'end')
        e1.configure(bg="light gray",fg="#370466")
def fout(entry):
    if e1.get().strip()=="":
        e1.delete(0,'end')
        e1.insert(0,"Enter Username...")
        e1.configure(bg="white",fg="#443F3F")
    if e1.get().strip()=="Enter Username...":
        l1.configure(text="Empty Username",fg="black")
        e1.focus_set()
    elif e1.get().strip() not in nmlst:
        l1.configure(text="Available✅",fg="green")  
    else:
        l1.configure(text="Unavailable❌",fg="red")
        e1.focus_set()
e1=Entry(lwin,bg="white",width=24,font=("Algerian",20,),fg="#443F3F",bd=1,relief=SOLID)
e1.place(relx=0.365,rely=0.355)
e1.insert(0,"Enter Username...")
e1.bind("<FocusIn>",fin)
e1.bind("<FocusOut>",fout)
e1.bind("<Return>",nxt)

l1=Label(bg="white")
l1.place(relx=0.655,rely=0.360)
#entry of password
def nxt2(event):
    e3.focus_set()
def fin2(event):
    if e2.get()=="Enter Password...":
        e2.delete(0,'end')
        e2.configure(bg="light gray",fg="#370466",show="*")
def fout2(entry):
    if e2.get()=="":
        e2.insert(0,"Enter Password...")
        e2.configure(bg="white",fg="#443F3F",show="")
e2=Entry(lwin,bg="white",width=24,font=("Algerian",20,),fg="gray")
e2=Entry(lwin,bg="white",width=24,font=("Algerian",20,),fg="#443F3F",bd=1,relief=SOLID)
e2.place(relx=0.365,rely=0.43)
e2.bind("<FocusIn>",fin2)
e2.insert(0,"Enter Password...")
e2.bind("<FocusOut>",fout2)
e2.bind("<Return>",nxt2)
def showw():
    if e2.get().strip()!="Enter Password..." and e2.get()!="":
        e2.configure(show="")
        hideb["state"]=NORMAL
        showb['state']=DISABLED
def hidee():
    e2.configure(show="*")
    hideb["state"]=DISABLED
    showb['state']=NORMAL
showb=Button(text="(◔◡◔)".strip(),font=("Times",12),bg="white",command=showw)
showb.place(relx=0.655,rely=0.43)
hideb=Button(text="(-__-)".strip(),state=DISABLED,font=("Times",12),bg="white",command=hidee)
hideb.place(relx=0.7,rely=0.43)
#confirm password
def nxt3(event): 
    if e2.get()==e3.get():
        clndr()
        lp.configure(text="Matched✅",fg="green")
    else:
        lp.configure(text="Unmatched❌",fg="red")
        e3.delete(0,END)
def fin3(event):
    if e3.get()=="Confirm Password...":
        e3.delete(0,'end')
        e3.configure(bg="light gray",fg="#370466",show="*")
def fout3(entry):
    if e2.get()==e3.get():
        lp.configure(text="Matched✅",fg="green")
    else:
        lp.configure(text="Unmatched❌",fg="red")
        e3.delete(0,END)
    if e3.get()=="":
        e3.insert(0,"Confirm Password...")
        e3.configure(bg="white",fg="#443F3F",show="")
e3=Entry(lwin,bg="white",width=24,font=("Algerian",20,),fg="gray")
e3=Entry(lwin,bg="white",width=24,font=("Algerian",20,),fg="#443F3F",bd=1,relief=SOLID)
e3.place(relx=0.365,rely=0.505)
e3.bind("<FocusIn>",fin3)
e3.insert(0,"Confirm Password...")
e3.bind("<FocusOut>",fout3)
e3.bind("<Return>",nxt3)
lp=Label(bg="white")
lp.place(relx=0.655,rely=0.510)
#dob
def gd():
    b2["state"]=NORMAL
    l2.configure(text='Your D.O.B  '+cal.get_date()+"   ")
    fr2.place_forget()
    dt.set(1)
    sbtn.focus_set()

def clndr():
    cal.pack()
    gb.pack()
    fr2.place(relx=0.670,rely=0.570)
    b2["state"]=DISABLED
def nxt4(event):
    gd()
fr1=Frame(bd=1,relief=SOLID,bg="white")
fr1.place(relx=0.365,rely=0.575)
l2=Label(fr1,text="Your D.O.B:   ",font=("Algerian",16),fg="#443F3F",bg="white")
l2.pack(side=LEFT)
b2=Button(fr1,text="Choose Date",command=clndr,font=("Algerian",14),fg="#443F3F",bg="white",bd=1,relief=SOLID)
b2.pack(side=RIGHT)
fr2=Frame(lwin,bg="white")
cal=Calendar(fr2,selectmode = 'day',year = 1980, month = 11,day = 2)
cal.pack()
fr2.bind("<Return>",nxt4)
gb=Button(fr2,text="Select Date",command=gd,font=("Algerian",14),fg="#443F3F",bg="white",bd=1,relief=SOLID)
gb.pack()
#Quit Button
def quitt():
    m=messagebox.askokcancel("alert","Are you sure you want to Quit",icon="warning")
    if m==True:
        quit()
q=Image.open("E:\\vscode\\clgproj\\nquit.png")
lwin.q=ImageTk.PhotoImage(q)
qbtn=Button(lwin,image=lwin.q,bd=0,bg="white",command=quitt)
qbtn.place(relx=0.82)
#Login Button
def loginn():
    lwin.destroy()
    subprocess.call(["python","Cassettelogin.py"])
l=Image.open("E:\\vscode\\clgproj\\lredir.png")
lwin.l=ImageTk.PhotoImage(l)
lbtn=Button(lwin,image=lwin.l,bd=0,bg="white",command=loginn)
lbtn.place(relx=0,rely=0)
#Submit Button

def last(event):
    submit()
def submit():
    
    lst=[e1.get().strip(),e2.get(),e3.get(),dt.get()]
    if lst[0]=='Enter Username...'or lst[1]=='Enter Password...'or lst[0]==''or lst[1]=='' or lst[2]=='Confirm Password...'or lst[2]=='' or lst[3]==0:
        status.configure(text="*Some Field(s) left Empty*",fg="red")
    elif lst[0] in nmlst:
        status.configure(text="*Unavailable Username chosen*",fg="red")
        e1.delete(0,END)
        e1.focus_set()
    elif lst[1]!=lst[2]:
        status.configure(text="*Password Does not match*",fg="red")
        lp.configure(text="")
        e3.delete(0,END)
        e3.focus_set()
    else:
        lbtn["state"]=DISABLED
        qbtn["state"]=DISABLED
        sbtn["state"]=DISABLED
        status.configure(text="Successful",fg="green")
        a=open('E:\\Cassette\\do_not_open.csv','a',newline="")
        b=csv.writer(a)
        b.writerow([str(randint(100,999))+encode(e1.get().strip()),str(randint(100,999))+encode(e2.get()),encode(cal.get_date())])
        a.close()
        os.mkdir('E:\\Cassette\\file\\'+encode(e1.get().strip()))
        foldername=encode(e1.get().strip())
        lwin.destroy()
        Cassettemain.main(foldername)

status=Label(text="*Waiting for submit button to be clicked*",font=("Times",13),bg="white")
status.place(relx=0.365,rely=0.640)
s=Image.open("E:\\vscode\\clgproj\\submit.png")
lwin.s=ImageTk.PhotoImage(s)
sbtn=Button(lwin,image=lwin.s,bd=0,bg="white",command=submit)
sbtn.place(relx=0.360,rely=0.675)
sbtn.bind("<Return>",last)
#window bindings
def lswitch(event):
    loginn()
def qswitch(event):
    quitt()
lwin.bind("<Alt-l>",lswitch)
lwin.bind("<Alt-s>",last)
lwin.bind("<Alt-x>",qswitch)
# lwin.bind("<Alt-F4>",qswitch) 
lwin.mainloop()
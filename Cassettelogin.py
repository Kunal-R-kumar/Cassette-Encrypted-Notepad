from tkinter import *
from tkinter import messagebox
import csv,os,subprocess,Cassettemain
from PIL import ImageTk,Image
direc=os.path.isdir('E:\\Cassette')
files=os.path.isfile('E:\\Cassette\\do_not_open.csv')
subdirec=os.path.isdir("E:\\Cassette\\file")
def quitt():
    m=messagebox.askokcancel("alert","Are you sure you want to Quit",icon="warning")
    if m==True:
        quit()
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
if direc == False or files==False or subdirec == False:
    cwin=Tk()
    cwin.title("Redirecting...")
    cwin.attributes("-fullscreen",True)
    m=messagebox.askyesno("alert","Seems like you are new user or user file being deleted\nShould we go to new user page",icon="question")
    cwin.destroy()
    if m==True:
        subprocess.call(["python","Cassettenwusr.py"])
    
else:
    lwin=Tk()
    lwin.title("Cassette Login Page")
    sw = lwin.winfo_screenwidth()
    sh = lwin.winfo_screenheight()
    lwin.attributes('-fullscreen',True)
    #filling bg img
    imgc = Image.open("E:\\vscode\\clgproj\\login.png").resize((sw,sh)).save("E:\\vscode\\clgproj\\login.png")
    img=PhotoImage(file="E:\\vscode\\clgproj\\login.png")
    bg=Label(lwin,image = img)
    bg.pack(fill="both",expand=True)
    #till here
    def nxt(event):
        e2.focus_set()
    def fin(event):
        if e1.get().strip()=="Enter Username...":
            e1.delete(0,'end')
            e1.configure(bg="light gray",fg="#370466")
    def fout(entry):
        if e1.get().strip()=="":
            e1.insert(0,"Enter Username...")
            e1.configure(bg="white",fg="gray")
    e1=Entry(lwin,bg="white",width=24,font=("Algerian",20,),fg="gray",relief="solid")
    e1.place(relx=0.388,rely=0.35)
    e1.insert(0,"Enter Username...")
    e1.bind("<FocusIn>",fin)
    e1.bind("<FocusOut>",fout)
    e1.bind("<Return>",nxt)

    pswd=StringVar()
    def fin2(event):
        if e2.get()=="Enter Password...":
            e2.delete(0,'end')
            e2.configure(bg="light gray",fg="#370466",show="*")
    def fout2(entry):
        if e2.get()=="":
            e2.insert(0,"Enter Password...")
            e2.configure(bg="white",fg="gray",show="")
    e2=Entry(lwin,bg="white",width=24,font=("Algerian",20,),fg="gray",textvariable=pswd,relief="solid")
    e2.place(relx=0.388,rely=0.45)
    e2.insert(0,"Enter Password...")
    e2.bind("<FocusIn>",fin2)
    e2.bind("<FocusOut>",fout2)

    #####
    def button_clicked():
        f=open('E:\\Cassette\\do_not_open.csv')
        fr=csv.reader(f)
        b=[e1.get().strip(),e2.get()]
        if b[0]=='Enter Username...'or b[1]=='Enter Password...'or b[0]==''or b[1]=='':
            label.configure(text="Username/password can't be empty",fg="red")
        else:
            for i in fr:
                if b[0]==decoder(i[0][3:]) and b[1]==decoder(i[1][3:]):
                    label.config(text="  Successful..redirecting in few seconds",fg="Green",font=10)
                    lbtn['state']=DISABLED
                    nbtn['state']=DISABLED
                    qbtn['state']=DISABLED
                    a=encode(e1.get().strip())
                    lwin.destroy()
                    Cassettemain.main(a)
                    break
            else:
                e2.delete(0,'end')
                e2.insert(0,"Enter Password...")
                e2.configure(bg="white",fg="gray",show='')
                e1.delete(0,"end")
                e1.focus_set()
                e1.icursor(0)
                label.config(text="Invalid username/password",fg="red")
    def buttonclicked(event):
        button_clicked()
    label=Label(lwin,text="*waiting for login button to be clicked*",bg="white",font=("Algerian",14))
    label.place(relx=0.382,rely=0.5595)
    lbtnp=Image.open("E:\\vscode\\clgproj\\lbtn.png")
    lwin.lbtnp=ImageTk.PhotoImage(lbtnp)
    #login button
    lbtn=Button(lwin,image=lwin.lbtnp,bd=0,bg="white",command=button_clicked)
    lbtn.place(relx=0.388,rely=0.637)
    e2.bind("<Return>",buttonclicked)
    #New User
    def new_clicked():
        lwin.destroy()
        subprocess.call(["python","Cassettenwusr.py"])
    lnu=Image.open("E:\\vscode\\clgproj\\lnew.png")
    lwin.lnu=ImageTk.PhotoImage(lnu)
    nbtn=Button(lwin,image=lwin.lnu,bd=0,bg="white",command=new_clicked)
    nbtn.place(relx=0.459,rely=0.23)
    # Quit
    def quitt():
        m=messagebox.askokcancel("alert","Are you sure you want to Quit",icon="warning")
        if m==True:
            quit()
    q=Image.open("E:\\vscode\\clgproj\\quit.png")
    lwin.q=ImageTk.PhotoImage(q)
    qbtn=Button(lwin,image=lwin.q,bd=0,bg="white",command=quitt)
    qbtn.place(relx=0.92,rely=0.007)  
    #window bindings
    def nswitch(event):
        new_clicked()
    def qswitch(event):
        quitt()
    lwin.bind("<Alt-x>",qswitch) 
    lwin.bind("<Alt-n>",nswitch)
    lwin.bind("<Alt-s>",buttonclicked)
    # lwin.bind("<Alt-F4>",qswitch)    
    lwin.mainloop()
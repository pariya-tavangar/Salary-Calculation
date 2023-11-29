#---------- Imports ----------
from tkinter import *
import tkinter
from tkinter import messagebox
import os
from PIL import Image, ImageTk

root = Tk()
root.resizable(False,False)
root.geometry("700x500+100+100")
root.title("Financial Project | Pariya Tavangar")
root.iconbitmap("img/iconroot.ico")


#---------- Admins -------------
admin = {'pariya':'1234'}


bg = PhotoImage(file = "img/loginbg.png")
label1 = Label( root,image = bg)
label1.place(x = 0, y = 0)



# ---------- Commands ----------
def mainmenu():

    root.destroy()
    os.system('python main_menu.py')

def exit_app():

    result = messagebox.askyesno("خروج","آیا مایل به خروج از برنامه هستید؟")
    if result:
        root.destroy()
    else:
        return

def submit(event = None):

    user = username_entry.get()
    pasw = password_entry.get()

    if (user == 'admin' and pasw == 'admin') or (user == 'pariya' and pasw == '1234'):
        messagebox.showinfo(title="ورود موفق",message="خوش آمدید",)
        mainmenu()
        

    elif username_entry.get()=='' and password_entry.get()=='':
        messagebox.showerror('خطا','لطفا نام کاربری و رمز عبور خود را وارد کنید')
        all_binds()

    else:
        username_entry.delete(0,END)
        password_entry.delete(0,END)
        messagebox.showerror(title="خطا در ورود",message='نام یا رمزعبور اشتباه است')
        all_binds()

def pass_protect(event = None):
    if password_entry["show"] == '*':
        password_entry["show"] = ''
        
        #------------
        img2 = ImageTk.PhotoImage(Image.open("img/eyeon.png"))
        label2.configure(image=img2)
        img_eye.image=img2
        
    else:
        password_entry["show"] ='*'
        #------------
        img2 = ImageTk.PhotoImage(Image.open("img/eyeoff.png"))
        label2.configure(image=img2)
        img_eye.image=img2



#---------- Initializing ----------
login_lbl = tkinter.Label(root, text="به سامانه حقوقی فایننشال خوش آمدید", bg='#4493A7',fg="#FFFFFF", font=("Titr",17),pady=10)
login_lbl.place(x=170,y=20)

username_lbl = tkinter.Label(root, text="نام کاربری", bg='#4493A7',fg="#FFFFFF",font=("Titr",13),width=6)
username_lbl.place(x=380,y=150)
username_entry = tkinter.Entry(root, font=("Titr",10),width=30,justify='center')
username_entry.place(x=180,y=155)

password_lbl = tkinter.Label(root, text="رمز ورود", bg='#4493A7',fg="#FFFFFF",font=("Titr",13),width=6)
password_lbl.place(x=380,y=230)
password_entry = tkinter.Entry(root, show='*',font=("Titr",10),width=30,justify='center')
password_entry.place(x=180,y=235)
img_eye = PhotoImage(file='img/eyeoff.png')
label2 = Label(root,image=img_eye)
label2.place(x=130,y=238)

login_btn = tkinter.Button(root, text="ورود به سامانه" , bg="#E7CBAC", fg="black", font=("Titr",12),width=10,command=submit)
login_btn.place(x=243,y=330)

exit_btn = tkinter.Button(root, text='خروج',bg='#870e0e',fg='white',font=("Titr",11),command=exit_app,width=6)
exit_btn.place(x=60,y=420)


# ---------- Binds ----------
def all_binds():
    username_entry.focus()
    username_entry.bind('<Return>', lambda event : password_entry.focus())
    password_entry.bind('<Return>',lambda event : login_btn.focus())
    login_btn.bind('<Return>',submit)
    label2.bind('<Button>',pass_protect)
    label2.bind('<Button>',pass_protect)


# #---------- Execute ----------
all_binds()

root.mainloop()
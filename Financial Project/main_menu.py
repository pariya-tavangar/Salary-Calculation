#---------- Imports ----------
from tkinter import *
import tkinter
from tkinter import messagebox
import os
from PIL import Image, ImageTk


menu = Tk()
menu.geometry("800x490")
menu.title("Financial Project | Pariya Tavangar")
menu.iconbitmap("img/iconroot.ico")


admins = ['pariya']
#---------- Initializing ----------

menu.resizable(False,False)
bg = PhotoImage(file = "img/bg2.png")
label1 = Label( image = bg)
label1.place(x = 0, y = 0)


frame = tkinter.Frame()
frame.configure(background='#A5B7C3')
frame.place(x=50,y=25)



# ---------- Commands ----------
def back():
    menu.destroy()
    os.system('python login.py')


def add_employee_menu():
    menu.destroy()
    os.system('python add_employee.py')

def about_us_page():
    menu.destroy()
    os.system('python about_us.py')

def calculating_salary():
    menu.destroy()
    os.system('python calculating_salary.py')


#------------------components-----------------------
login_lbl = tkinter.Label(frame, text="به سامانه حقوقی فایننشال خوش آمدید", bg='#A5B7C3',fg="#FFFFFF",font=('Titr',15))
login_lbl.grid(row=0,column=1,padx=4,pady=30)



img_1 = PhotoImage(file='img/add.png')
label_img1 = Label(frame,image=img_1,bg='#A5B7C3')
label_img1.grid(row=1,column=0)

btn_cal = tkinter.Button(frame,text='افزودن پرسنل جدید',command=add_employee_menu,font=("Titr",12),pady=15,bg='#0074FF',fg='white',relief='raised')
btn_cal.grid(row=1,column=1)

img_2 = PhotoImage(file='img/cal.png')
label_img2 = Label(frame,image=img_2,bg='#A5B7C3')
label_img2.grid(row=2,column=0,pady=20)

btn_cal = tkinter.Button(frame,text='محاسبه حقوق پرسنل',
                         command=calculating_salary,
                         font=("Titr",12),pady=15,bg='#0074FF',fg='white',relief='raised')
btn_cal.grid(row=2,column=1)

img_3 = PhotoImage(file='img/support.png')
label_img3 = Label(frame,image=img_3,bg='#A5B7C3')
label_img3.grid(row=3,column=0)

btn_cal = tkinter.Button(frame,text='پشتیبانی/پیشنهادات',font=("Titr",12),pady=15,
                         command=about_us_page,
                         bg='#0074FF',fg='white',relief='raised')
btn_cal.grid(row=3,column=1)


img_4 = PhotoImage(file='img/back.png')
btn_back = Button(menu,image=img_4,command=back)
btn_back.place(x=650,y=390)


img_5 = PhotoImage(file='img/admin.png')
label_img4 = Label(menu,image=img_5,bg='#EBECF1')
label_img4.place(x=690,y=40)


label_img5 = Label(menu,bg='#EBECF1',text='خوش آمدید',font=('Titr'))
label_img5.place(x=620,y=100)

label_img6 = Label(menu,bg='#EBECF1',text= admins[0] + " " + ': ادمین ',font=('Titr'))
label_img6.place(x=600,y=130)

menu.mainloop()
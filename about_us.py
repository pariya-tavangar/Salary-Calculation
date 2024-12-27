#----------imports----------
from tkinter import *
import tkinter as tk
import tkinter
from tkinter import ttk
from tkinter import filedialog
from tkinter.filedialog import askopenfile
from PIL import Image, ImageTk
from tkinter import scrolledtext
import csv
import os
from tkinter.messagebox import askyesno,askokcancel
from tkinter import messagebox
import pandas as pd
from csv import DictWriter


#------------configurations------------
win = tkinter.Tk()
win.geometry('690x390')
win.resizable(False,False)
win.title("ثبت کارمند جدید")
iconn = ImageTk.PhotoImage(Image.open("img/new_employeee.png"))
win.option_add( "*font", "Homa 10" )
win.iconbitmap("img/iconroot.ico")


# ------------ Footer -------------
bg = PhotoImage(file = "img/support_bg.png")
label1 = Label( win, image = bg)
label1.pack()



#---------------Command----------------
def exit_btn():
    win.destroy()
    os.system('python main_menu.py')      


def report_message():

    reportt = report_area.get("1.0",END)
    with open('reports/report.md', 'w',encoding='utf-8',newline='') as f_object:
        f_object.write(reportt)
        f_object.close()

        messagebox.showinfo('ارسال پیشنهادات','♥ پیام شما به ادمین اضافه شد')
        report_area.delete('1.0',END)

# ------------Attributes---------------
bg2 = PhotoImage(file = "img/software-developer.png")
label2 = Label( win, image = bg2)
label2.place(x=300,y=20)

label3 = Label( win, text='تماس با ما ',font=("Titr",13),width=8,
               relief='ridge',borderwidth=5,bg='#1E1F23',fg='white'
               )
label3.place(x=400,y=150)

label4 = Label( win, text='Ptavangar1382@gmail',font=("Arial",14),
               relief='flat',borderwidth=5,bg='#1E1F23',fg='white'
               )
label4.place(x=120,y=155)
 

label3 = Label( win, text='پیشنهادات',font=("Titr",13),width=8,
               relief='ridge',borderwidth=5,bg='#1E1F23',fg='white'
               )
label3.place(x=400,y=210)

report_area = Text(win,font = ("Koodak", 10),width=30,height=2,)
report_area.place(x=120,y=200)

label4 = Button( win, text='ارسال',font=("Titr",10),width=12,height=1,
               relief='raised',borderwidth=3,bg='#64C8F0',fg='black',
               command=report_message
               )
label4.place(x=158,y=280)

label5 = Button( win, text='بازگشت',font=("Titr",10),width=8,height=1,
               relief='raised',borderwidth=3,bg='#850707',fg='white',
               command=exit_btn
               )
label5.place(x=540,y=320)

win.mainloop()

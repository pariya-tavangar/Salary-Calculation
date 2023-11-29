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

global workerCodes
workerCodes = ['110','120','130','140']


#------------configurations------------
win = tkinter.Tk()
win.geometry('790x510')
win.resizable(False,False)
win.iconbitmap("img/iconroot.ico")
win.title("ثبت کارمند جدید")
iconn = ImageTk.PhotoImage(Image.open("img/new_employeee.png"))
win.configure(background="#A57B56")
win.option_add( "*font", "Homa 10" )

# win.option_add( "*font", "Koodak 10" )



#--------------Frames-----------------
frame = Frame(win,width=780,height=300,padx=10,pady=20,bg='#A57B56')
frame.pack()

frame2 = Frame(frame,width=500,height=200)
frame2.grid(row=0,column=0)
frame3 = Frame(frame,width=200,height=200)
frame3.grid(row=0,column=1)





#--------------- commands --------------
def upload_file():
    f_types = [('Jpg Files', '*.jpg'),
    ('PNG Files','*.png')]   # type of files to select 
    filename = tk.filedialog.askopenfilename(multiple=True,filetypes=f_types)

    for f in filename:
        img=Image.open(f)
        img=img.resize((115,110))
        img=ImageTk.PhotoImage(img)

        img_label.image = img
        img_label['image']=img

def submit_data():

    if len(first_name_entry.get()) == 0 or len(last_name_entry.get()) == 0 or len(age_spinbox.get())==0 or len(gender_combobox.get())==0 or len(info_entry.get())==0 or len(code_entry.get())==0 or len(phone_entry.get())==0 or len(marriage_combobox.get())==0 or len(degree_entry.get())==0 or len(children_entry.get())==0:
        messagebox.showerror(title='خطا',message='همه فیلدها باید پر شوند')
    else:
        if code_entry.get() in workerCodes:
                messagebox.showerror(title="خطا", message="کد پرسنلی استفاده شده است")
                [widget.delete(0, tk.END) for widget in user_info_frame.winfo_children() if isinstance(widget, tk.Entry)]
                [widget.delete(0, tk.END) for widget in user_info_frame.winfo_children() if isinstance(widget, tk.Spinbox)]
                [widget.delete(0, tk.END) for widget in user_info_frame2.winfo_children() if isinstance(widget, tk.Entry)]
                text_area.delete('1.0', END)
                first_name_entry.focus()
        else:
            workerCodes.append(code_entry.get())
            answer = askyesno(title='ثبت اطلاعات',message='آیا مایل به ثبت اطلاعات هستید؟')
            if answer:

                field_names = ["employeeCode","firstname","lastname","age","gender",
                            "codeMeli","phone","marriage","degree","children"]
                new_employee_data={
                                'employeeCode':code_entry.get(),
                            'firstname':first_name_entry.get(),
                            'lastname':last_name_entry.get(),
                            'age':age_spinbox.get(),
                            'gender':gender_combobox.get(),
                            'codeMeli':info_entry.get(),
                            'phone':phone_entry.get(),
                            'marriage':marriage_combobox.get(),
                            'degree':degree_entry.get(),
                            'children':children_entry.get()
                            }


                with open('employee_data.csv', 'a',encoding='utf-8',newline='') as f_object:

                    dictwriter_object = DictWriter(f_object, fieldnames=field_names)
                    dictwriter_object.writerow(new_employee_data)
                    f_object.close()

def del_data():
    answer = messagebox.askokcancel("حذف", "رکورد ها حذف شود؟")
    if answer:
        [widget.delete(0, tk.END) for widget in user_info_frame.winfo_children() if isinstance(widget, tk.Entry)]
        [widget.delete(0, tk.END) for widget in user_info_frame.winfo_children() if isinstance(widget, tk.Spinbox)]
        [widget.delete(0, tk.END) for widget in user_info_frame2.winfo_children() if isinstance(widget, tk.Entry)]
        text_area.delete('1.0', END)
        first_name_entry.focus()

    else:
        return

def exit_btn():
    answer = messagebox.askokcancel("خروج", "منو بسته شود؟")
    if answer:
        win.destroy()
        os.system('python main_menu.py') 




win.option_add( "*font", "Homa 8" )
# ------------ Footer -------------
bg = PhotoImage(file = "img/Bg.png")
label1 = Label( win, image = bg)
label1.pack()



# ---------------- other frames -------------------
frame4 = Frame(frame,width=200,height=200,bg='#A57B56')
frame4.grid(row=1,column=1)
frame5 = Frame(frame,bg="red",width=500,height=200)
frame5.grid(row=1,column=0)


background_image=tk.PhotoImage('bg1.png')
background_label = tk.Label(frame3, image=background_image)
background_label.place(x=0, y=0)



#---------------components--------------
img_label = tkinter.Label(frame3,bg="#703F2A")
img_label.grid(row=0,column=0)

img_label.configure(image=iconn)
img_label.image=iconn

btn1 = tk.Button(frame3, text='بارگزاری عکس',bg='#703F2A',fg='white',
   width=15,padx=2,pady=2,command=lambda:upload_file(),relief='groove')
btn1.grid(row=1,column=0)

user_info_frame = tkinter.LabelFrame(frame2,width=100,bg='#A57B56')
user_info_frame.pack()




#--------------- Section 1 ------------------
first_name_label = tkinter.Label(user_info_frame,text='نام',relief='ridge',width=12)
first_name_label.grid(row=0,column=3)
first_name_entry = tkinter.Entry(user_info_frame,justify='center')
first_name_entry.grid(row=0,column=2)

last_name_label = tkinter.Label(user_info_frame,text='نام خانوادگی',relief='ridge',width=12)
last_name_label.grid(row=1,column=3)
last_name_entry = tkinter.Entry(user_info_frame,justify='center')
last_name_entry.grid(row=1,column=2)

gender_label = tkinter.Label(user_info_frame,text='جنسیت',relief='ridge',width=12)
gender_combobox = ttk.Combobox(user_info_frame,values=['زن','مرد'],width=17,justify='center') 
gender_label.grid(row=2,column=3)
gender_combobox.grid(row=2,column=2)

code_label = tkinter.Label(user_info_frame,text='شماره پرسنلی',relief='ridge',width=12)
code_label.grid(row=2,column=1)
code_entry = tkinter.Entry(user_info_frame,justify='center')
code_entry.grid(row=2,column=0)

age_label = tkinter.Label(user_info_frame,text='سن',relief='ridge',width=12)
age_spinbox = tkinter.Spinbox(user_info_frame,from_=18, to=70,justify='center')
age_label.grid(row=0,column=1)
age_spinbox.grid(row=0,column=0)

marriage_label = tkinter.Label(user_info_frame,text='وضعیت تاهل',relief='ridge',width=12)
marriage_combobox = ttk.Combobox(user_info_frame,values=['متاهل','مجرد'],width=18,justify='center') 
marriage_label.grid(row=1,column=1)
marriage_combobox.grid(row=1,column=0)





#--------------- Section 2 ------------------

user_info_frame2 = tkinter.LabelFrame(frame5,width=200,padx=10,pady=15,bg='#A57B56')
user_info_frame2.pack()

info_label = tkinter.Label(user_info_frame2,text='شماره شناسنامه',relief='ridge',width=12)
info_label.grid(row=0,column=1)
info_entry = tkinter.Entry(user_info_frame2,justify='center')
info_entry.grid(row=0,column=0)

lob_label = tkinter.Label(user_info_frame2,text='محل تولد',relief='ridge',width=12)
lob_label.grid(row=0,column=3)
lob_entry = tkinter.Entry(user_info_frame2,justify='center')
lob_entry.grid(row=0,column=2)

dob_label = tkinter.Label(user_info_frame2,text='تاریخ تولد',relief='ridge',width=12)
dob_label.grid(row=1,column=1)
dob_entry = tkinter.Entry(user_info_frame2,justify='center')
dob_entry.grid(row=1,column=0)

children_label = tkinter.Label(user_info_frame2,text='تعداد فرزند',relief='ridge',width=12)
children_label.grid(row=1,column=3)
children_entry = tkinter.Entry(user_info_frame2,justify='center')
children_entry.grid(row=1,column=2)

degree_label = tkinter.Label(user_info_frame2,text='مدرک تحصیلی',relief='ridge',width=12)
degree_label.grid(row=2,column=1)
degree_entry = tkinter.Entry(user_info_frame2,justify='center')
degree_entry.grid(row=2,column=0)

phone_label = tkinter.Label(user_info_frame2,text='شماره همراه',relief='ridge',width=12)
phone_label.grid(row=2,column=3)
phone_entry = tkinter.Entry(user_info_frame2,justify='center')
phone_entry.grid(row=2,column=2)

post_label = tkinter.Label(user_info_frame2,text=':کد پستی',relief='ridge',width=12)
post_label.grid(row=3,column=3)
post_entry = tkinter.Entry(user_info_frame2,justify='center')
post_entry.grid(row=3,column=2)

address_label = tkinter.Label(user_info_frame2,text='آدرس',relief='ridge',width=12)
address_label.grid(row=3,column=1)
text_area = scrolledtext.ScrolledText(user_info_frame2,
                                      wrap = tk.WORD,  
                                      width = 15,
                                      height = 1.5,  
                                      font = ("Koodak", 10))
text_area.grid(row=3,column=0)


user_info_final = tkinter.LabelFrame(frame4,width=200,padx=10,pady=15,bg='#A57B56',relief='raised',borderwidth=10)
user_info_final.pack()

# bg='#703F2A'
btn_submit = tk.Button(user_info_final, text='ثبت اطلاعات',bg='#703F2A',fg='white',
   width=15,padx=2,pady=2,command=submit_data,relief='raised')
btn1.grid(row=0,column=0)

btn_clean = tk.Button(user_info_final, text='پاک کردن',bg='#703F2A',fg='white',
   width=15,padx=2,pady=2,command=del_data,relief='raised')
btn1.grid(row=1,column=0)

btn_back = tk.Button(user_info_final, text='بازگشت',bg='#703F2A',fg='white',
   width=15,padx=2,pady=2,command=exit_btn,relief='raised')
btn1.grid(row=2,column=0)



#------------- all paddings ----------------
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=11,pady=12)

for widget in user_info_frame2.winfo_children():
    widget.grid_configure(padx=10,pady=8)

for widget in user_info_final.winfo_children():
    widget.grid_configure(padx=10,pady=8)



#----------------Binds------------------
def all_binds():
    first_name_entry.focus()
    first_name_entry.bind('<Return>',lambda event : last_name_entry.focus())
    last_name_entry.bind('<Return>',lambda event : gender_combobox.focus())
    gender_combobox.bind('<Return>',lambda event : age_spinbox.focus())
    age_spinbox.bind('<Return>',lambda event : marriage_combobox.focus())
    marriage_combobox.bind('<Return>',lambda event : code_entry.focus())
    code_entry.bind('<Return>',lambda event : lob_entry.focus())
    lob_entry.bind('<Return>',lambda event : info_entry.focus())
    info_entry.bind('<Return>',lambda event : children_entry.focus())
    children_entry.bind('<Return>',lambda event : dob_entry.focus())
    dob_entry.bind('<Return>',lambda event : phone_entry.focus())
    phone_entry.bind('<Return>',lambda event : degree_entry.focus())
    degree_entry.bind('<Return>',lambda event : post_entry.focus())
    post_entry.bind('<Return>',lambda event : text_area.focus())
    text_area.bind('<Return>',lambda event : btn_submit.focus())



    btn_submit.bind('<Return>',submit_data)
    btn_back.bind('<Button>',del_data)
    btn_clean.bind('<Button>',exit_btn)

#---------execute-----------
all_binds()

win.mainloop()
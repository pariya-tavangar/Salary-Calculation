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
from tkinter import filedialog




global showData

#------------configurations------------
win = tkinter.Tk()
win.geometry('810x510')
win.resizable(False,False)
win.title("محاسبه حقوق پرسنل")
win.configure(background="#3C342E")
win.option_add( "*font", "Homa 10" )
win.iconbitmap("img/iconroot.ico")
 

#--------------Frames-----------------
frame = Frame(win,width=780,height=300,padx=10,pady=20,bg='#3C342E')
frame.pack()

frame2 = Frame(frame,width=700,height=200)
frame2.grid(row=0,column=0)


frame3 = Frame(frame,width=150,height=130,bg='#3C342E')
frame3.grid(row=0,column=1)


#--------------- commands --------------

def find_by_code():

    with open('employee_data.csv',encoding='utf-8') as file_obj: 
        reader_obj = csv.reader(file_obj)

        for row in reader_obj:
            if codee_entry.get() in row:
                label_persenel['text'] = ('کارمند',row[0],':',row[1],row[2])
                persenel_entry.delete(0,END)
                persenel_entry.insert(0,row[0])
                first_name_entry.delete(0,END)
                first_name_entry.insert(0,row[1])

                last_name_entry.delete(0,END)
                last_name_entry.insert(0,row[2])

                info_entry.delete(0,END)
                info_entry.insert(0,row[4])

                married_combobox.delete(0,END)
                married_combobox.insert(0,row[7])

                children_entry.delete(0,END)
                children_entry.insert(0,row[9])
                break
            else:
                label_persenel['text'] = 'کاربر وارد شده وجود ندارد'

def del_data():
    answer = messagebox.askokcancel("حذف", "رکورد ها حذف شود؟")
    if answer:
        [widget.delete(0, tk.END) for widget in user_info_frame.winfo_children() if isinstance(widget, tk.Entry)]
        [widget.delete(0, tk.END) for widget in user_info_frame2.winfo_children() if isinstance(widget, tk.Entry)]
        [widget.delete(0, tk.END) for widget in user_info_frame3.winfo_children() if isinstance(widget, tk.Entry)]

        first_name_entry.focus()
    else:
        return

def exit_btn():
    answer = messagebox.askokcancel("خروج", "منو بسته شود؟")
    if answer:
        win.destroy()
        os.system('python main_menu.py')      

def submit():

    global saveData

    if len(first_name_entry.get()) == 0 or len(last_name_entry.get()) == 0 or len(info_entry.get())==0 or len(married_combobox.get())==0 or len(children_entry.get())==0 or len(persenel_entry.get())==0 or len(low_salary_entry.get())==0 or len(base_salary_entry.get())==0 or len(overtime_entry.get())==0 or len(friday_entry.get())==0 or len(night_work_entry.get())==0 or len(total_work_entry.get())==0:
        messagebox.showerror(title='خطا',message='همه فیلدها باید پر شوند')
    else:
        saveData = {

            'name': first_name_entry.get(),
            'lastname' : last_name_entry.get(),
            'info': info_entry.get(),
            'married': married_combobox.get(),
            'children': children_entry.get(),
            'persenel' : persenel_entry.get(),
            'low_salary' : low_salary_entry.get(),
            'base_salary' : base_salary_entry.get(),
            'overtime' : overtime_entry.get(),
            'friday' : friday_entry.get(),
            'night_work' : night_work_entry.get(),
            'total_work' : total_work_entry.get()
            }

        
        btn1['state'] = 'disabled'
        btn_submit['state'] = 'disabled'
        codee_entry['state'] = 'disabled'
        

        btn_save = tk.Button(user_info_final, text='ذخیره فیش',bg='#6FBC01', fg='white',
        width=15,padx=0,pady=0,command=save_data,relief='raised',borderwidth=3)
        btn_save.grid(row=1,column=0)

        first_name_entry.grid_forget()
        first_name_lbl = tkinter.Label(user_info_frame,
                                    text= saveData['name'],
                                    justify='center',bg='#3C342E',fg='white')
        first_name_lbl.grid(row=0,column=2)

        last_name_entry.grid_forget()
        last_name_lbl = tkinter.Label(user_info_frame,text=saveData['lastname'],width=12,bg='#3C342E',fg='white')
        last_name_lbl.grid(row=1,column=2)

        info_entry.grid_forget()
        info_lbl = tkinter.Label(user_info_frame,text=saveData['info'],width=12,bg='#3C342E',fg='white')
        info_lbl.grid(row=2,column=2)

        married_combobox.grid_forget()
        marry_lbl = tkinter.Label(user_info_frame,text=saveData['married'],width=12,bg='#3C342E',fg='white')
        marry_lbl.grid(row=0,column=0)

        children_entry.grid_forget()
        children_lbl = tkinter.Label(user_info_frame,text=saveData['children'],width=12,bg='#3C342E',fg='white')
        children_lbl.grid(row=1,column=0)

        persenel_entry.grid_forget()
        persenel_lbl = tkinter.Label(user_info_frame,text=saveData['persenel'],width=12,bg='#3C342E',fg='white')
        persenel_lbl.grid(row=2,column=0)

        low_salary_entry.grid_forget()
        low_salary_lbl = tkinter.Label(user_info_frame2,text=saveData['low_salary'],width=12,bg='#3C342E',fg='white')
        low_salary_lbl.grid(row=0,column=2)

        base_salary_entry.grid_forget()
        base_salary_lbl = tkinter.Label(user_info_frame2,text=saveData['base_salary'],width=12,bg='#3C342E',fg='white')
        base_salary_lbl.grid(row=1,column=2)

        overtime_entry.grid_forget()
        overtime_lbl = tkinter.Label(user_info_frame2,text=saveData['overtime'],width=12,bg='#3C342E',fg='white')
        overtime_lbl.grid(row=0,column=4)

        friday_entry.grid_forget()
        friday_lbl = tkinter.Label(user_info_frame2,text=saveData['friday'],width=12,bg='#3C342E',fg='white')
        friday_lbl.grid(row=1,column=4)

        night_work_entry.grid_forget()
        night_work_lbl = tkinter.Label(user_info_frame2,text=saveData['friday'],width=12,bg='#3C342E',fg='white')
        night_work_lbl.grid(row=2,column=4)

        total_work_entry.grid_forget()
        total_work_lbl = tkinter.Label(user_info_frame2,text=saveData['total_work'],width=12,bg='#3C342E',fg='white')
        total_work_lbl.grid(row=2,column=2)

def save_data():

    file = filedialog.asksaveasfilename(filetypes=[('Text File','*.txt'),
                                                   ('CSV File','*.csv')
                                                   ],
                                        defaultextension='.csv'
                                        )
    fob = open(file,'w',encoding='utf-8')
    fob.write(str(saveData))
    fob.close()

# ------------ Footer -------------

bg = PhotoImage(file = "img/bg4.png")
label1 = Label( win, image = bg)
label1.pack()

# ---------------- other frames -------------------
frame4 = Frame(frame,width=200,height=200,bg='#4B332A')
frame4.grid(row=1,column=1)

frame5 = Frame(frame,width=700,height=200)
frame5.grid(row=1,column=0)

#---------------components--------------

user_info_frame3 = tkinter.LabelFrame(frame3,width=100,bg='#3C342E',borderwidth=3,relief='groove')
user_info_frame3.pack()

label_persenel = tk.Labelfirst_name_label = tkinter.Label(user_info_frame3,text='کد پرسنلی جست و جو کنید',
                                                          relief='ridge',bg='black',width=17,fg='white',pady=5)
label_persenel.grid(row=0,column=0)

codee_entry = tkinter.Entry(user_info_frame3,width=20,justify='center')
codee_entry.grid(row=1,column=0)

btn1 = tk.Button(user_info_frame3, text='جست و جو',bg='#6A423B',fg='white',font=('Homa',10),
   width=13,command=lambda:find_by_code(),relief='raised',borderwidth=3)
btn1.grid(row=3,column=0)


#--------------- Section 1 ------------------

user_info_frame = tkinter.LabelFrame(frame2,width=100,bg='#3C342E')
user_info_frame.pack()


first_name_label = tkinter.Label(user_info_frame,text='نام',relief='ridge',width=12,bg='#c2c5d1')
first_name_label.grid(row=0,column=3)
first_name_entry = tkinter.Entry(user_info_frame,justify='center')
first_name_entry.grid(row=0,column=2)

last_name_label = tkinter.Label(user_info_frame,text='نام خانوادگی',relief='ridge',width=12,bg='#c2c5d1')
last_name_label.grid(row=1,column=3)
last_name_entry = tkinter.Entry(user_info_frame,justify='center')
last_name_entry.grid(row=1,column=2)

info_label = tkinter.Label(user_info_frame,text='شماره شناسنامه',relief='ridge',width=12,bg='#c2c5d1')
info_label.grid(row=2,column=3)
info_entry = tkinter.Entry(user_info_frame,justify='center')
info_entry.grid(row=2,column=2)

married_label = tkinter.Label(user_info_frame,text='وضعیت تاهل',relief='ridge',width=12,bg='#c2c5d1')
married_combobox = ttk.Combobox(user_info_frame,values=['متاهل','مجرد'],width=17,justify='center') 
married_label.grid(row=0,column=1)
married_combobox.grid(row=0,column=0)

children_label = tkinter.Label(user_info_frame,text='تعداد فرزند',relief='ridge',width=12,bg='#c2c5d1')
children_label.grid(row=1,column=1)
children_entry = tkinter.Entry(user_info_frame,justify='center')
children_entry.grid(row=1,column=0)

persenel_code = tkinter.Label(user_info_frame,text='کد پرسنلی',relief='ridge',width=12,bg='#c2c5d1')
persenel_code.grid(row=2,column=1)
persenel_entry = tkinter.Entry(user_info_frame,justify='center')
persenel_entry.grid(row=2,column=0)




# #--------------- Section 2 ------------------

user_info_frame2 = tkinter.LabelFrame(frame5,width=200,padx=10,pady=15,bg='#3C342E')
user_info_frame2.pack()

low_salary_label = tkinter.Label(user_info_frame2,text='حداقل حقوق',relief='ridge',width=12,bg='#c2c5d1')
low_salary_label.grid(row=0,column=3)
low_salary_entry = tkinter.Entry(user_info_frame2,justify='center')
low_salary_entry.grid(row=0,column=2)

base_salary_label = tkinter.Label(user_info_frame2,text='حقوق پایه',relief='ridge',width=12,bg='#c2c5d1')
base_salary_label.grid(row=1,column=3)
base_salary_entry = tkinter.Entry(user_info_frame2,justify='center')
base_salary_entry.grid(row=1,column=2)


overtime_label = tkinter.Label(user_info_frame2,text='ساعات اضافی کاری',relief='ridge',width=14,bg='#c2c5d1')
overtime_label.grid(row=0,column=5)
overtime_entry = tkinter.Entry(user_info_frame2,justify='center')
overtime_entry.grid(row=0,column=4)

friday_label = tkinter.Label(user_info_frame2,text='ساعات تعطیل کاری',relief='ridge',width=14,bg='#c2c5d1')
friday_label.grid(row=1,column=5)
friday_entry = tkinter.Entry(user_info_frame2,justify='center')
friday_entry.grid(row=1,column=4)


night_work_label = tkinter.Label(user_info_frame2,text='ساعات شب کاری',relief='ridge',width=14,bg='#c2c5d1')
night_work_label.grid(row=2,column=5)
night_work_entry = tkinter.Entry(user_info_frame2,justify='center')
night_work_entry.grid(row=2,column=4)

total_work_label = tkinter.Label(user_info_frame2,text='کارکرد ( روز )',relief='ridge',width=12,bg='#c2c5d1')
total_work_label.grid(row=2,column=3)
total_work_entry = tkinter.Entry(user_info_frame2,justify='center')
total_work_entry.grid(row=2,column=2)


user_info_final = tkinter.LabelFrame(frame4,width=200,padx=10,pady=15,bg='#3C342E',relief='raised',borderwidth=10)
user_info_final.pack()


btn_submit = tk.Button(user_info_final, text='صدور فیش',bg='#6A423B', fg='white',
   width=15,padx=0,pady=0,command=submit,relief='raised',borderwidth=3)
btn_submit.grid(row=0,column=0)

btn_clean = tk.Button(user_info_final, text='پاک کردن',bg='#6A423B', fg='white',
   width=15,padx=0,pady=0,command=del_data,relief='raised',borderwidth=3)
btn_clean.grid(row=1,column=0)

btn_back = tk.Button(user_info_final, text='بازگشت',bg='#6A423B', fg='white',
   width=15,padx=0,pady=0,command=exit_btn,relief='raised',borderwidth=3)
btn_back.grid(row=2,column=0)



#------------- all paddings ----------------
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=11,pady=12)

for widget in user_info_frame2.winfo_children():
    widget.grid_configure(padx=10,pady=8)

for widget in user_info_frame3.winfo_children():
    widget.grid_configure(padx=10,pady=8)

for widget in user_info_final.winfo_children():
    widget.grid_configure(padx=3,pady=3)


#----------------Binds------------------
def all_binds():
    first_name_entry.focus()
    first_name_entry.bind('<Return>',lambda event : last_name_entry.focus())
    last_name_entry.bind('<Return>',lambda event : info_entry.focus())
    info_entry.bind('<Return>',lambda event : married_combobox.focus())
    married_combobox.bind('<Return>',lambda event : children_entry.focus())
    children_entry.bind('<Return>',lambda event : persenel_entry.focus())
    persenel_entry.bind('<Return>',lambda event : overtime_entry.focus())
    overtime_entry.bind('<Return>',lambda event : friday_entry.focus())
    friday_entry.bind('<Return>',lambda event : night_work_entry.focus())
    night_work_entry.bind('<Return>',lambda event : low_salary_entry.focus())
    low_salary_entry.bind('<Return>',lambda event : base_salary_entry.focus())
    base_salary_entry.bind('<Return>',lambda event : total_work_entry.focus())
    total_work_entry.bind('<Return>',lambda event : btn_submit.focus())

    btn_submit.bind('<Return>',submit)
    btn_back.bind('<Button>',del_data)
    btn_clean.bind('<Button>',exit_btn)

#---------execute-----------
all_binds()

win.mainloop()
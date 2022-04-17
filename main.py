from tkinter import *
import pyperclip
import random
import string
def generator():
    clean()
    small_alpha=string.ascii_lowercase
    cap_alpha=string.ascii_uppercase
    nums=string.digits
    special_char=string.punctuation

    all=small_alpha+cap_alpha+nums+special_char
    password_len=int(len_box.get())
    print(password_len)
    if Choice.get()==1:
        output_box.insert(0,random.sample(small_alpha,password_len))
    if Choice.get() == 2:
        output_box.insert(0,random.sample(small_alpha+cap_alpha+nums,password_len))
    if Choice.get() == 3:
        output_box.insert(0,random.sample(small_alpha+cap_alpha+nums+special_char,password_len))
def copy():
    random_password=output_box.get()
    pyperclip.copy(random_password)
def clean():
    output_box.delete(0,END)
root=Tk()
root.geometry("610x450")
root.title("GUI Password Generator")
root.iconbitmap("icon.ico")
root.config(bg='#afeeee')

Title = Label(root, text="PASSWORD GENERATOR", fg="black", bg='#afeeee', font=("segoe UI Black", 32, "bold","underline"))
Title.place(x=40, y=8)
Choice=IntVar()
Font=("segoe UI Black", 20, "bold",)
#WEAK BUTTON
wk_button=Radiobutton(root,text='  WEAK   ',fg="black", bg='#32CD32',value=1,variable=Choice,font=Font,borderwidth=3,relief="solid")
wk_button.place(x=30,y=100)

#MEDIUM BUTTON
mid_button=Radiobutton(root,text='MEDIUM ',fg="black", bg='#FFA500',value=2,variable=Choice,font=Font,borderwidth=3, relief="solid")
mid_button.place(x=30,y=180)

#STRONG BUTTON
s_button=Radiobutton(root,text='STRONG ',fg="black", bg='#FF5733',value=3,variable=Choice,font=Font,borderwidth=3, relief="solid")
s_button.place(x=30,y=260)

#LENGTH BOX
len_box=Spinbox(root,from_=5,to_=20,width=7,font=("Arial Black",14),borderwidth=3, relief="raised")
len_box.place(x=44,y=340)

#LENGTH BOX TEXT
len = Label(root, text="Password \n Length", fg="black", bg='#afeeee', font=("segoe UI Black", 12))
len.place(x=50,y=380)

#OUTPUT BOX
output_box=Entry(root,width=20,fg="red",bg='white',bd=5,font=("segoe UI Black",24, "bold"))
output_box.place(x=207,y=130)

#GENERATE BUTTON
gen_button=Button(root,text="GENERATE",fg="black",bg='#ffd343',font=("segoe UI Black", 25, "bold",),borderwidth=3, relief="solid",command=generator)
gen_button.place(x=280,y=200)

#COPY BUTTON
copy_button=Button(root,text="COPY",fg="white",bg='purple',font=("segoe UI Black", 18, "bold",),borderwidth=3, relief="solid",command=copy)
copy_button.place(x=285,y=300)

#CLEAN BUTTON
copy_button=Button(root,text="CLEAN",fg="black",bg='pink',font=("segoe UI Black", 18, "bold",),borderwidth=3, relief="solid",command=clean)
copy_button.place(x=380,y=300)

#FOOTER SECTION
footer = Label(root, text="Developed & Designed By @Rupam_Chakraborty \n All Rights reserved",bg="#afeeee", fg="black", font=("ubuntu", 12, "bold"))
footer.place(x=205, y=400)
root.mainloop()

from tkinter import *
from PIL import ImageTk , Image
import os
import pandas as pd

interface_1=Tk()
interface_1.geometry('750x500')
interface_1.title('Fitter Health')

def interface_2():
    h = height.get()
    w = weight.get()
    if h==0 or w==0:
        bmi=0
    else:
        bmi = w//(h*h)
    if bmi<1:
        os.startfile('2.pyw')
    else:
        os.startfile('3.pyw')

# NAME
name2 = StringVar()
name_button=Label(interface_1  ,  text='Enter your name: ',width=15, height=1, activeforeground='red' , font=('Times', 16))
name_button.grid(pady=20 , column=2 , row=1)
name_input=Entry(interface_1 , textvariable = name2, font=("arial", 15) , border=5)
name_input.grid(pady=20 ,column=3 , row=1)

# AGE
age = IntVar()
age_button=Label(interface_1,  text='Enter your age: ',width=15, height=1, activeforeground='red' , font=('Times', 16))
age_button.grid(pady=20 ,column=2 , row=3)
age_input=Entry(interface_1 ,textvariable = age,  font=("arial", 15), border=5)
age_input.grid(pady=20 ,column=3 , row=3)

# GENDER
gender_button=Label(interface_1 ,  text='Gender: ',width=15, height=1, activeforeground='red' , font=('Times', 16))
gender_button.grid(pady=20 ,column=2 , row=5)
v = IntVar()
male = Radiobutton(interface_1 , text='Male' , variable=v, font=('Times', 16) , value=1).grid(pady=20 ,column=3 , row=5)
female = Radiobutton(interface_1 , text='Female' , variable=v, font=('Times', 16) , value=2).grid(pady=20 ,column=4 , row=5)

# HEIGHT
height = IntVar()
height_button = Label(interface_1 ,  text='Height(in meters): ',width=15, height=1, activeforeground='red' , font=('Times', 16))
height_button.grid(pady=20 ,column=2 , row=7)
height_input=Entry(interface_1 , textvariable=height ,  font=("arial", 15), border=5)
height_input.grid(pady=20 ,column=3 , row=7)

# WEIGHT
weight = IntVar()
weight_button = Label(interface_1 ,  text='Weight(in kgs): ',width=15, height=1, activeforeground='red' , font=('Times', 16))
weight_button.grid(pady=20 ,column=2 , row=9)
weight_input=Entry(interface_1 , textvariable=weight , font=("arial", 15), border=5)
weight_input.grid(pady=20 ,column=3 , row=9)

# img1 = PhotoImage(file = 'button.png')
img1 = Image.open('finalbutton.png')
img2 = img1.resize((260,130), Image.ANTIALIAS)
img3= ImageTk.PhotoImage(img2)

# ENTER BUTTON
blank_space = Label(interface_1, text='          ',width=10, height=2, activeforeground='red' , font=('Times', 16))
blank_space.grid(column=0 , row=1)
enter_button = Button(interface_1, image=img3 , borderwidth = 0 , text='Enter ->', command=interface_2)
enter_button.grid(column=3 , row=11)

# df = pd.read_excel('"C:\Users\Ishika Gulati\OneDrive\Desktop\Book1.xlsx"')

# for item in df.iterrows():
#     ans = item['bmi']
#     print(ans)


interface_1.mainloop()
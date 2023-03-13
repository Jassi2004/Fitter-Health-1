from tkinter import *
from PIL import ImageTk , Image
import pandas as pd

interface_3 = Tk()
interface_3.geometry('750x500')
interface_3.title('Fitter Health interface 3')
# ans = bmi_func()

img1 = Image.open('bmi.png')
img2 = img1.resize((650 , 350) , Image.ANTIALIAS)
img3 = ImageTk.PhotoImage(img2)

frame1 = Frame(interface_3 , width=700 , height=100 , border=5 , relief='raised' , bg='light grey')
frame1.pack(side = TOP)
  

frame2 = Frame(interface_3 , width=710 , height=400 , border=5 , relief='raised' , bg='light blue')
frame2.pack(side = TOP)
#  , padx=50 ,pady=50)

# df = pd.read_excel("C:\Users\Ishika Gulati\OneDrive\Desktop\Book1.xlsx")

# for item in df.iterrows():
#     ans = item['bmi']

calculate_bmi = Label(frame1 , text='BMI : ' ,width=15, height=1, activeforeground='red' , font=('Times', 16) )
calculate_bmi.grid(column=2 , row=2 , padx=20 , pady=20)
x1 = Label(frame1 , text='23' ,width=15, height=1, activeforeground='red' , font=('Times', 16))
x1.grid(column=3 , row=2 , padx=20 , pady=20)

pho = Label(frame2 , image=img3)
pho.pack()

# can = Canvas(frame2 , width=700 , height=390 , image=img3)
# can.pack()
interface_3.mainloop()
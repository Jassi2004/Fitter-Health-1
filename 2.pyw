from tkinter import *
from PIL import ImageTk , Image
import os

interface_2 = Tk()
interface_2.geometry('750x500')
interface_2.title('Fitter Health')

def interface_3():
    os.startfile('3.pyw')
def interface_4():
    os.startfile('4.pyw')
def interface_5_button():
    pass

hello = Label(interface_2 , text = "Hello ", font=('Times', 16))
# + name_input.get() 
hello.pack(side = TOP  , pady=10)
hello2 = Label(interface_2 , text = "Welcome to the journey" , font=('Times', 16))
hello2.pack(side = TOP  , pady=10)

calculator = Button(interface_2 , text='Calculator' , width=20 , height=1 ,  activeforeground='red' , command=interface_3, font=('Times', 16), border=5 , relief='raised')
calculator.pack(side = TOP  , pady=10)

diet = Button(interface_2 , text='Diet' , width=20 , height=1 ,  activeforeground='red' , command=interface_4, font=('Times', 16), border=5 , relief='raised')
diet.pack(side = TOP , pady=10 )

workout = Button(interface_2 , text='Workout' , width=20 , height=1 ,  activeforeground='red' , command=interface_5_button, font=('Times', 16), border=5 , relief='raised')
workout.pack(side = TOP, pady=10 )

trackers = Button(interface_2 , text='Trackers' , width=20 , height=1 ,  activeforeground='red' , command='', font=('Times', 16), border=5 , relief='raised')
trackers.pack(side = TOP , pady=10 )

chat_bot = Button(interface_2 , text='Chat Bot' , width=20 , height=1 ,  activeforeground='red' , command='', font=('Times', 16), border=5 , relief='raised')
chat_bot.pack(side = TOP , pady=10)

interface_2.mainloop()
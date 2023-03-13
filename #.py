
from tkinter import *
from PIL import Image,ImageTk

window=Tk()

bg=PhotoImage(file='bmi.png')
Label(window,image=bg).pack()
 
window.mainloop()

from tkinter import *
from PIL import ImageTk , Image
# from PIL 
import os

interface_1=Tk()
interface_1.geometry('750x500')
interface_1.title('Fitter Health')


def input_1_interface_5():
    interface_5_Workout_info(1)
def input_2_interface_5():
    interface_5_Workout_info(2)
def input_3_interface_5():
    interface_5_Workout_info(3)
def input_4_interface_5():
    interface_5_Workout_info(4)

def interface_5_Workout_info(inp):

    interface_5_Workout_info=Tk()
    interface_5_Workout_info.geometry('750x500')
    interface_5_Workout_info.title('Fitter Health abs')
    if inp==1:
        w1= Label(interface_5_Workout_info,text='Side crunches kicks: 3 sets of 30 secs (per side)\n\nHigh Plank Walk: 3 sets of 60 secs\n\nDumbbell Oblique Crunches: 3 sets of 30 secs (per side)\n\nFrog Jumps: 3 sets of 60 secs\n\nOne side Leg Crossovers: 3 sets of 30 secs (per side)\n\nSide Dumbbell raises: 3 sets of 30 secs (per side)\n\nHigh Donkey Kicks: 3 sets of 30 secs (per side)\n\nLeg Extensions: 3 sets of 60 secs\n\nDumbbell biceps curls: 3 sets of 30 secs (per side)\n\nPile Squat Calf Raises: 3 sets of 60 secs\n\nPlanks: 3 sets of 60 secs', font=('Times', 16), border=2 , relief='raised')
        w1.pack()
    elif inp==2:
        w1= Label(interface_5_Workout_info,text='Frog Jumps: 3 sets of 15 reps\n\nSide Plank Leg Raise: 3 sets of 15 reps (per side)\n\nBulgarian Split Squats: 3 sets of 15 reps (per side)\n\nBent Over Lateral Leg Raise: 3 sets of 15 reps (per side)\n\nBody Weight Sumo Squats: 3 sets of 15 reps\n\nOne Legged Row: 3 sets of 15 reps (per side)\n\nPile Squat Calf Raises: 3 sets of 15 reps\n\nBench Glute Raises: 3 sets of 15 reps\nWall Squats: 3 sets of 15 reps\n\nLateral Lunge: 3 sets of 15 reps (per side)', font=('Times', 16), border=2 , relief='raised')
        w1.pack()
    elif inp==3:
        w1= Label(interface_5_Workout_info,text='Body Weight Squats: 3 sets of 15 reps\n\nOne Side Leg Crossovers: 3 sets of 15 reps (per side)\n\nJump Lunges: 3 sets of 15 reps (per side)\nReverse Lunge with elevated Front Leg: 3 sets of 15 reps (per side)\n\nHip Thrusters: 3 sets of 15 reps\nOne Leg Row: 3 sets of 15 reps (per side)\n\nGlute Bridge to Leg Raise: 3 sets of 15 reps (per side)\n\nDonkey Kicks: 3 sets of 15 reps (per side)\n\nBulgarian Split Squats: 3 sets of 15 reps (per side)', font=('Times', 16), border=2 , relief='raised')
        w1.pack()
    else:
        w1= Label(interface_5_Workout_info,text='Dumbbell Squat and Press: 3 sets of 60 secs\n\nDumbbell Skull Crusher: 3 sets of 45 secs\n\nSquat Dumbbell Oblique Raises: 3 sets of 30 secs (per side)\n\nDumbbell Peck Fly: 3 sets of 45 secs\n\nDumbbell bent over row: 3 sets of 30 secs (per side)\n\nSide Dumbbell Raise: 3 sets of 45 secs\n\nTricep Dumbbell Flipbacks: 3 sets of 30 secs (per side)\n\nHigh Plank Dumbbell Row and Push Up: 3 sets of 45 secs\n\nDumbbell Step Up: 3 sets of 30 secs (per side)\n\nGoblet Squat: 3 sets of 60 secs', font=('Times', 16), border=2 , relief='raised')
        w1.pack()
    
    interface_5_Workout_info.mainloop()

def interface_5_button():

    interface_5_button = Tk()
    interface_5_button.geometry('750x500')
    interface_5_button.title('Fitter Health 5')

    blank_space = Label(interface_5_button, text='          ',width=10, height=2, activeforeground='red' , font=('Times', 16))
    blank_space.pack(side=TOP, pady=10)

    AbsWorkout_button=Button(interface_5_button,text='Abs Workout' , width=20 , height=1 ,  activeforeground='red' , font=('Times', 16), border=5 , relief='raised',command=input_1_interface_5)
    AbsWorkout_button.pack(side = TOP  , pady=10)

    LegWorkout_button=Button(interface_5_button,text='Leg Workout' , width=20 , height=1 ,  activeforeground='red' , font=('Times', 16), border=5 , relief='raised',command=input_2_interface_5)
    LegWorkout_button.pack(side = TOP  , pady=10)

    ButtWorkout_button=Button(interface_5_button,text='Butt Workout'  , width=20 , height=1 ,  activeforeground='red' , font=('Times', 16), border=5 , relief='raised',command=input_3_interface_5)
    ButtWorkout_button.pack(side = TOP  , pady=10)

    FullBodyWorkout_button=Button(interface_5_button,text='Full Body Workout'  , width=20 , height=1 ,  activeforeground='red' , font=('Times', 16), border=5 , relief='raised',command=input_4_interface_5)
    FullBodyWorkout_button.pack(side = TOP  , pady=10)


def interface_2():

    interface_2 = Tk()
    interface_2.geometry('750x500')
    interface_2.title('Fitter Health')

    hello = Label(interface_2 , text = "Hello "+ name_input.get() , font=('Times', 16))
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

def bmi_func():
    
    height = float(height_input.get())
    weight = float(weight_input.get())
    if height==0 or weight==0:
        return 0
    bmi = round((weight)/(height)**2)
    return bmi


def interface_3():
    # pass
    os.startfile('1.pyw')

#     from PIL import ImageTk , Image

#     interface_3 = Toplevel()
#     interface_3.geometry('750x500')
#     interface_3.title('Fitter Health interface 3')
#     ans = bmi_func()

#     frame1 = Frame(interface_3 , width=700 , height=100 , border=5 , relief='raised' , bg='light grey')
#     frame1.pack(side = TOP)
  
#     mage = PhotoImage(file='b.png')

#     # label=Label(image=mage)
#     # label.place(x=0,y=0)


#     frame2 = Frame(interface_3 , width=710 , height=400 , border=5 , relief='raised' , Image=mage)
#     frame2.pack(side = TOP)

#     # calculate_bmi = Label(frame1 , text='BMI : ' ,width=15, height=1, activeforeground='red' , font=('Times', 16) )
#     # calculate_bmi.grid(column=2 , row=2 , padx=20 , pady=20)
#     # x1 = Label(frame1 , text=ans ,width=15, height=1, activeforeground='red' , font=('Times', 16))
#     # x1.grid(column=3 , row=2 , padx=20 , pady=20)


#     # canvas = Canvas(interface_3  , image=mage)
#     # canvas.pack()


#     # image = (Image.open('a.png'))
#     # resized_image= image.resize((700,100), Image.ANTIALIAS)
#     # new_image= ImageTk.PhotoImage(resized_image)

#     # x = 'a.png'
#     # img = Image.open(x)
#     # img = img.resize((700 , 400) , Image.ANTIALIAS)
#     # img = ImageTk.PhotoImage(img)

#     # img = ImageTk.PhotoImage(Image.open("a.png"))

#     # label = Label(frame2,image=img)
#     # label.pack()
    
#     # interface_3 = Tk()
#     # interface_3.geometry('750x500')
#     # interface_3.title('Fitter Health')
#     # frame1 = Frame(interface_3 , bg='red')        
#     # frame1.pack(side=TOP)         
#     # frame2 = Frame(interface_3 , width=500 , height=300 , bg='light blue')           
#     # frame2.pack(side=TOP)        
#     # # image = (Image.open("Screenshot (17).png"))          
#     # image = ImageTk.PhotoImage(Image.open("ab.png"))            
#     # label = Label(frame2 , image=image)
#     # label.pack()
#     # # blank_space = Label(frame1, text='          ',width=10, height=2, activeforeground='red' , font=('Times', 16))
#     # # blank_space.grid(column=0 , row=2 , padx=10)
#     # calculate_bmi = Label(frame1 , text='BMI : ' ,width=15, height=1, activeforeground='red' , font=('Times', 16) )
#     # calculate_bmi.grid(column=2 , row=2 , padx=50 , pady=20)

#     # x1 = Label(frame1 , text=ans ,width=15, height=1, activeforeground='red' , font=('Times', 16))
#     # x1.grid(column=3 , row=2 , padx=50 , pady=20)



#     # # blank_space = Label(interface_3, text='          ',width=10, height=2, activeforeground='red' , font=('Times', 16))
#     # # blank_space.grid(column=0 , row=5)
#     # # calculate_bfi = Label(interface_3 , text='Body Fat Percentage' ,width=15, height=1, activeforeground='red' , font=('Times', 16) , command=bmi_func)
#     # # calculate_bfi.grid(column=2 , row=5)

#     interface_3.mainloop()

def paleo_diet_info():
    paleo_button = Tk()
    paleo_button.geometry('750x500')
    paleo_button.title('Paleo Button')

    info1= Label(interface_4, text='How it works: The paleo diet emphasizes whole foods, lean protein, vegetables, fruits, nuts, and seeds, while discouraging processed foods, sugar, dairy, and grains.Some more flexible versions of the paleo diet also allow for dairy like cheese and butter, as well as tubers like potatoes and sweet potatoes.',width=10, height=2 , font=('Times', 16))
    info2= Label(interface_4, text='Weight loss: Several studies have shown that the paleo diet can lead to significant weight loss and reduced waist size. In studies, paleo dieters automatically eat much fewer carbs, more protein, and 300–900 fewer calories per day ', width=10, height=2 , font=('Times', 16))
    info3= Label(interface_4, text='Other benefits: The diet seems effective at reducing risk factors for heart disease, such as cholesterol, blood sugar, blood triglycerides, and blood pressure ',width=10, height=2 , font=('Times', 16))
    info4= Label(interface_4, text='The downside: The paleo diet eliminates whole grains, legumes, and dairy, which are healthy and nutritious.',width=10, height=2, font=('Times', 16))
    paleo_button= Button(interface_4, text='Check few suggestions',width=10, height=2, activeforeground='red' , font=('Times', 16))
    info1.pack()
    info2.pack()
    info3.pack()
    info4.pack()
    paleo_button.pack()

    paleo_button.mainloop()

def interface_4():

    interface_4= Tk()
    interface_4.geometry('750x500')
    interface_4.title('Fitter Health')

    blank_space = Label(interface_4, text='          ',width=10, height=2, activeforeground='red' , font=('Times', 16))
    blank_space.pack(side=TOP, pady=10)
    paleo_diet = Button(interface_4 , text='Paleo Diet' , width=20 , height=1 ,  activeforeground='red' , font=('Times', 16), border=5 , relief='raised', command=paleo_diet_info )
    paleo_diet.pack(side = TOP  , pady=10)
    vegan_diet = Button(interface_4 , text='Vegan Diet' , width=20 , height=1 ,  activeforeground='red' , command='', font=('Times', 16), border=5 , relief='raised')
    vegan_diet.pack(side = TOP  , pady=10)
    low_carb_diet = Button(interface_4 , text='Low Carb Diet' , width=20 , height=1 ,  activeforeground='red' , command='', font=('Times', 16), border=5 , relief='raised')
    low_carb_diet.pack(side = TOP  , pady=10)
    atkins_diet = Button(interface_4 , text='Atkins Diet' , width=20 , height=1 ,  activeforeground='red' , command='', font=('Times', 16), border=5 , relief='raised')
    atkins_diet.pack(side = TOP  , pady=10)
    intermittent_fasting = Button(interface_4 , text='Intermittent Fasting' , width=20 , height=1 ,  activeforeground='red' , command='', font=('Times', 16), border=5 , relief='raised')
    intermittent_fasting.pack(side = TOP  , pady=10)

    interface_4.mainloop()


# photo = ImageTk.PhotoImage(Image.open("ab.png"))
# photo = (Image.open("ab.png"))
# resize = photo.resize((50,50) , Image.ANTIALIAS)
# new_image= ImageTk.PhotoImage(resize)

# PhotoFrame = Frame(interface_1, width=100 , height=100)
# PhotoFrame.grid(column=0 , row=1)
# label1 = Label(interface_1 ,text='asdfghjkl;lkjhgf0' , image = new_image)
# label1.grid(row=3 , column=0)

# bg = PhotoImage(file = "bg2.png")

# canvas1 = Canvas(interface_1, width = 750 , height = 500)
# canvas1.pack()
# # canvas1.create_image( 0, 0, image = bg , anchor = "nw")

# frame = Frame(interface_1 , height=500 , width=300 , bg='blue')
# frame.pack(anchor='center')


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
img1 = Image.open('enterbutton1.png')
img2 = img1.resize((260,130), Image.ANTIALIAS)
img3= ImageTk.PhotoImage(img2)

# ENTER BUTTON
blank_space = Label(interface_1, text='          ',width=10, height=2, activeforeground='red' , font=('Times', 16))
blank_space.grid(column=0 , row=1)
enter_button = Button(interface_1, image=img3 , borderwidth = 0 , text='Enter ->', command=interface_2)
#  , border=5 , relief='raised' ,  text='Enter ->',width=15, height=1, activeforeground='red' , font=('Times', 16) , command=interface_2)
enter_button.grid(column=3 , row=11)


interface_1.mainloop()



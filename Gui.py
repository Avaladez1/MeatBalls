import tkinter as tk
import os
import simulation as Sim


root = tk.Tk()
root.geometry("1000x600")

# Get the directory path and file path of the image
DIRECTORY_PATH = os.path.dirname(__file__)
FILE_PATH = os.path.join(DIRECTORY_PATH, "new.gif")

# Create a PhotoImage object from the JPG file
back = tk.PhotoImage(file=FILE_PATH)

# Create a label and set the image as background
background_label = tk.Label(root, image=back)
background_label.pack(fill="both", expand="yes")

# Create buttons and entry widgets and place them on the background label
text1 = tk.Entry(background_label, fg='black', width=8)
text1.place(x=40,y=0)


def set_students():
    Sim.number_of_students=text1.get()





button1 = tk.Button(background_label, text="Number_Students", fg='black', height=2, width=10)
button1.place(x=20,y=50)

text2 = tk.Entry(background_label, fg='black', width=8)
text2.place(x=295,y=0)

def slide_amount_change():
    Sim.number_of_students=text2.get()




button2 = tk.Button(background_label, text="Slide_Amount", fg='black', height=2, width=10)
button2.place(x=280,y=50)

text3 = tk.Entry(background_label, fg='black', width=8)
text3.place(x=560, y=0)

def Slide_length_change():

    Sim.slide_length=text3.get()

button3 = tk.Button(background_label, text="Slide_Length", fg='black', height=2, width=10)
button3.place(x=540,y=50)

# text boxes for driving times 
text4 = tk.Entry(background_label, fg='black', width=6)
text4.place(x=795,y=0)

text5= tk.Entry(background_label, fg='black', width=6)
text5.place(x=860,y=0)

def set_drive_time():
    Sim.max_drive_time =text4.get()
    Sim.min_drive_time =text5.get()


button4 = tk.Button(background_label, text="Drive_Time", fg='black', height=2, width=10)
button4.place(x=803,y=50)

# button5 = tk.Button(background_label, text="Submit", fg='black', height=2, width=15)
# button5.place(x=390,y=140)

def Submit():
    button5 = tk.Button(background_label, text="Submit", fg='black', height=2, width=15)
    button5.place(x=390,y=140)
    button5=Sim.simulate_week()

root.mainloop()

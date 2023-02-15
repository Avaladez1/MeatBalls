import tkinter as tk
import os
import simulation as Sim

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Full Week Simulation")
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
    text1 = tk.Entry(background_label, fg='lightgreen', bg='black', width=8)
    text1.place(x=40,y=0)


    def set_students():
        Sim.number_of_students=int(text1.get())
        print(int(Sim.number_of_students))


    button1 = tk.Button(background_label, text="Number_Students", fg='black', height=2, width=10,command=set_students)
    button1.place(x=20,y=50)

    text2 = tk.Entry(background_label, fg='lightgreen', bg='black', width=8)
    text2.place(x=295,y=0)

    def slide_amount_change():
        Sim.number_of_slides=int(text2.get())
        print(int(Sim.number_of_slides))


    button2 = tk.Button(background_label, text="Slide_Amount", fg='black', height=2, width=10,command=slide_amount_change)
    button2.place(x=275,y=50)

    text3 = tk.Entry(background_label, fg='lightgreen', bg='black', width=8)
    text3.place(x=560, y=0)

    def Slide_length_change():
        Sim.slide_length=int(text3.get())
        print(int(Sim.slide_length))


    button3 = tk.Button(background_label, text="Slide_Length", fg='black', height=2, width=10, command=Slide_length_change)
    button3.place(x=540,y=50)

    # text boxes for driving times 
    text4 = tk.Entry(background_label, fg='lightgreen', bg='black', width=6)
    text4.place(x=795,y=0)

    text5= tk.Entry(background_label, fg='lightgreen', bg='black', width=6)
    text5.place(x=860,y=0)

    def set_drive_time():
        Sim.sq.min_driving_time = int(text4.get())
        Sim.sq.max_driving_time = int(text5.get())
        print(f"max-{Sim.sq.max_driving_time} + min-{Sim.sq.min_driving_time}")


    button4 = tk.Button(background_label, text="Drive_Time", fg='black', height=2, width=10,command=set_drive_time)
    button4.place(x=803,y=50)

    def Submit():

        set_students()
        slide_amount_change()
        Slide_length_change()
        set_drive_time()
        Sim.simulate_week()
        result_string = Sim.average_students_that_saw_slide(Sim.STUDENT_LIST,Sim.sign)
        # print(len(Sim.STUDENT_LIST))
        # print(Sim.STUDENT_LIST[0].slides_seen)
        # print(Sim.sign.head)
        results.configure(text=result_string)
    
    button5 = tk.Button(background_label, text="Submit", fg='black', height=2, width=15,command=Submit)
    button5.place(x=390,y=140)
    
    results=tk.Label(background_label, text="Results", fg='black', height=25, width=40)
    results.place(x=0,y=190)
    root.mainloop()



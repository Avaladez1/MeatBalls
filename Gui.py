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
text1 = tk.Entry(background_label, fg='black', width=20)
text1.place(x=10,y=0)

button1 = tk.Button(background_label, text="Button 1", fg='black', height=2, width=15)
button1.place(x=20,y=50)

text2 = tk.Entry(background_label, fg='black', width=20)
text2.place(x=270,y=0)

button2 = tk.Button(background_label, text="Button 2", fg='black', height=2, width=15)
button2.place(x=280,y=50)

text3 = tk.Entry(background_label, fg='black', width=20)
text3.place(x=530, y=0)

button3 = tk.Button(background_label, text="Button 3", fg='black', height=2, width=15)
button3.place(x=540,y=50)

text4 = tk.Entry(background_label, fg='black', width=20)
text4.place(x=793,y=0)

button4 = tk.Button(background_label, text="Button 4", fg='black', height=2, width=15)
button4.place(x=803,y=50)

root.mainloop()

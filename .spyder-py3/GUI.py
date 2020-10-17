from tkinter import *
import os

root = Tk ()

root.title("Drowsiness Detection")
root.geometry("400x400")
thresh = 0.25
frame_check = 20

Threshold = Label(root, text = "Thresh eye ratio ")
Frame_check = Label(root, text = "Frames to be checked ")
entry1 = Entry(root,textvariable = thresh)
entry2 = Entry(root,textvariable = frame_check)



def Button_1():
     msg = Message(root, text = "Enjoy your movie! ")
     msg.config(justify = CENTER, bg='lightgreen', font=('times', 10, 'italic'))
     msg.grid(row = 18,columnspan = 13)
     thresh = entry1.get()
     frame_check = entry2.get()
     os.system('python sleep.py')
     
     
def Button_2():
     msg = Message(root, text = "Don't sleep! Don't get fired! ")
     msg.config(justify = CENTER, bg='lightgreen', font=('times', 10, 'italic'))
     msg.grid(row = 18,columnspan = 13)
     thresh = entry1.get()
     frame_check = entry2.get()
     os.system('python alarm.py')
    

Threshold.grid(row = 1,column = 4)
Frame_check.grid(row = 3,column = 4)
entry1.grid(row = 1, column = 7)
entry2.grid(row = 3, column = 7)


button1 = Button(root,text = "Sleep", fg="red", command = Button_1)
button1.grid(row = 5 ,column = 3, columnspan = 3)

button2 = Button(root,text = "Alarm", fg="blue",command = Button_2)
button2.grid(row = 5, column = 5, columnspan = 3)

root.mainloop()
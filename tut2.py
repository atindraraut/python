from tkinter import *
#for other image formats  PIL is been imported
from PIL import Image, ImageTk

root = Tk()

#add title to the GUI
root.title("my first GUI")
#width x height
root.geometry("733x434")
#set the minimum size of the window syntax= width, height
root.minsize(733, 434)

#set the maxsize of the window syntax = width, height
root.maxsize(733, 434)

#label to display on the GUI
dis = Label(text="this is the first sentence to be displayed on the window")
dis.pack()

#to display an image in the window
"""photo = PhotoImage(file="s50.png")
dis_photo = Label(image=photo)
dis_photo.pack()"""

"""for jpg image format"""
image = Image.open("unnamed.jpg")
photo = ImageTk.PhotoImage(image)
dis_photo = Label(image=photo)
dis_photo.pack()

#here we will write the main logic of the programme

root.mainloop()
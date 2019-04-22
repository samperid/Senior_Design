from Tkinter import *

# Main window / sizing main window
root = Tk()
root.geometry("500x500")


# Function
def labelAppear():
    imaging = Label(text="Imaging...")
    imaging.config(font=("Arial",24,"bold"))
    imaging.place(relx=0.37, rely=0.9)


# Title label
title = Label(root, text="LESION CHECK",anchor=CENTER)
title.config(font=("Arial", 36, "italic"))
title.place(relx=0.23, rely=0.2)

# Button to start acquisition
start = Button(root, text="Start Imaging", command=labelAppear)
start.config(font=("Arial", 20, "bold"))
start.place(relx=0.3, rely=0.65)

# Enter text for patient's name
enter = Entry()
enter.place(relx=0.3, rely=0.5)

# Label for text box
label_enter = Label(root, text="Enter Patient's Name")
label_enter.config(font=("Arial", 16,"bold"))
label_enter.place(relx=0.33, rely = 0.45)

root.mainloop()
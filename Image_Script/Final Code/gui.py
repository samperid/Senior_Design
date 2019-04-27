import flask
app = flask.Flask(__name__)
app.secret_key = "super secret key"

@app.route("/",methods=['GET','POST'])
def index():
	#run main with name from user
	return flask.render_template('index.html',**locals())

@app.route("/result",methods=['GET','POST'])
def image():
	name = flask.request.form.get('name')
	flask.session['name'] = name
	test = "string"
	return flask.render_template('result.html',**locals())

if __name__ == "__main__":
    app.run(debug=True)


# from Tkinter import *
# import time
# from test2 import test

# #Main window / sizing main window
# root = Tk()
# root.geometry("800x480")


# # Function
# def labelAppear():
# 	text_var = "imaging...."
# 	imaging = Label(text=text_var)
# 	imaging.config(font=("Arial",24,"bold"))
# 	imaging.place(relx=0.37, rely=0.9)
# 	#imaging.pack()
# 	test()


# # Title label
# title = Label(root, text="LESION CHECK",anchor=CENTER)
# title.config(font=("Arial", 36, "italic","underline"))
# title.place(relx=0.3, rely=0.2)

# # Label for text box
# label_enter = Label(root, text="Enter Patient's Name")
# label_enter.config(font=("Arial", 16,"bold"))
# label_enter.place(relx=0.39, rely = 0.45)

# # Enter text for patient's name
# enter = Entry()
# enter.place(relx=0.36, rely=0.5)

# # Button to start acquisition
# start = Button(text="Start Imaging", command=labelAppear)
# start.config(font=("Arial", 20, "bold"))
# start.place(height=100, width=200, relx=0.35, rely=0.65)

# root.mainloop()

# class buddy:

# 	def labelAppear(input):
# 		imaging = Label(text=input)
# 		imaging.config(font=("Arial",24,"bold"))
# 		imaging.place(relx=0.37, rely=0.9)

# 	def __init__(self, master):
# 		self.master = master
# 		master.title("Bigio Buddy")

# 		self.total = 0
# 		self.entered_number = 0

# 		self.label = Label(master, text="LESION CHECK", anchor=CENTER)
# 		self.label.config(font=("Arial", 36, "italic"))
# 		self.label.place(relx=0.23, rely=0.2)

# 		self.entry = Entry()
# 		self.entry.place(relx=0.3, rely=0.5)

# 		self.add_button = Button(master, text="Start Imaging", command= self.labelAppear("Imaging..."))
# 		self.add_button.config(font=("Arial", 20, "bold"))
# 		self.add_button.place(height=50, width=200, relx=0.3, rely=0.65)

#         # LAYOUT

# root = Tk()
# root.geometry('500x300')
# my_gui = buddy(root)
# root.mainloop()

'''
class Calculator:

    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.total = 0
        self.entered_number = 0

        self.total_label_text = IntVar()
        self.total_label_text.set(self.total)
        self.total_label = Label(master, textvariable=self.total_label_text)

        self.label = Label(master, text="Total:")

        vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master, validate="key", validatecommand=(vcmd, '%P'))

        self.add_button = Button(master, text="+", command=lambda: self.update("add"))
        self.subtract_button = Button(master, text="-", command=lambda: self.update("subtract"))
        self.reset_button = Button(master, text="Reset", command=lambda: self.update("reset"))

        # LAYOUT

        self.label.grid(row=0, column=0, sticky=W)
        self.total_label.grid(row=0, column=1, columnspan=2, sticky=E)

        self.entry.grid(row=1, column=0, columnspan=3, sticky=W+E)

        self.add_button.grid(row=2, column=0)
        self.subtract_button.grid(row=2, column=1)
        self.reset_button.grid(row=2, column=2, sticky=W+E)

    def validate(self, new_text):
        if not new_text: # the field is being cleared
            self.entered_number = 0
            return True

        try:
            self.entered_number = int(new_text)
            return True
        except ValueError:
            return False

    def update(self, method):
        if method == "add":
            self.total += self.entered_number
        elif method == "subtract":
            self.total -= self.entered_number
        else: # reset
            self.total = 0

        self.total_label_text.set(self.total)
        self.entry.delete(0, END)

root = Tk()
root.geometry('500x300')
my_gui = Calculator(root)
root.mainloop()
'''
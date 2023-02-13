import tkinter as tk
from tkinter import ttk
from tkinter import * 

# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = tInput.get()
	return userInput


# this is a function to get the user input from the text input box
def getInputBoxValue():
	userInput = standard.get()
	return userInput


# this is a function which returns the selected combo box item
def getSelectedComboItem():
	choice = Mark_List.get()


# this is the function called when the button is clicked
def Mark_List_Fetch():
	print(Mark_List.get())
def test():
	pass



root = Tk()

# This is the section of code which creates the main window
root.geometry('760x467')
root.configure(background='#838B8B')
root.title('Student Login')


# This is the section of code which creates a text input box
tInput=Entry(root)
tInput.place(x=234, y=114)


# This is the section of code which creates a text input box
standard=Entry(root)
standard.place(x=233, y=206)


# This is the section of code which creates the a label
Label(root, text='Student Name', bg='#838B8B', font=('arial', 20, 'bold')).place(x=107, y=63)


# This is the section of code which creates the a label
Label(root, text='Student Standard ', bg='#838B8B', font=('arial', 20, 'bold')).place(x=97, y=152)


# This is the section of code which creates the a label
Label(root, text='Select Required MarkList', bg='#838B8B', font=('arial', 20, 'bold')).place(x=94, y=250)


# This is the section of code which creates a combo box
Mark_List= ttk.Combobox(root, values=['Quartely', 'Half_Yearly', 'Finals'], font=('arial', 20, 'bold'), width=10)
Mark_List.place(x=230, y=305)
Mark_List.current(1)


# This is the section of code which creates a button
Button(root, text='Fetch MarkList', bg='#CCCCCC', font=('arial', 20, 'bold'), command=Mark_List_Fetch).place(x=400, y=378)
Button(root,text='Insert MarkList', bg='#CCCCCC', font=('arial', 20, 'bold'), command=test).place(x=150,y=378)


root.mainloop()

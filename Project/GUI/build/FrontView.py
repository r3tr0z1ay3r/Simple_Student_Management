


import tkinter as tk
from tkinter import ttk
from tkinter import * 
from pathlib import Path
from tkinter import *
from tkinter import messagebox

# from tkinter import *
# Explicit imports to satisfy Flake8

# this is a function to get the user input from the text input box



def Student_window():
    def getInputBoxValue1():
        name_inp = tInput.get()
        return name_inp


    # this is a function to get the user input from the text input box
    def getInputBoxValue2():
        standard_inp = standard.get()
        return standard_inp


    # this is a function which returns the selected combo box item
    def getSelectedComboItem():
        choice = Mark_List.get()


    # this is the function called when the button is clicked
    def Mark_List_Fetch():
        print(Mark_List.get())
        name = getInputBoxValue1()
        standard = getInputBoxValue2()
        if name == "" or standard == "":
            messagebox.showwarning("Invalid Input","Please enter a valid input")
        #Should finish with showing the table input
        print(name,standard)
    root = Tk()
    window.destroy()
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
    Button(root, text='Fetch MarkList', bg='#CCCCCC', font=('arial', 20, 'bold'), command=Mark_List_Fetch).place(x=260, y=378)


    root.mainloop()


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
authenticated = False
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

db_student = {"admin":"admin"}

def autheticate():
    usr = entry_1.get()
    pas = entry_2.get()
    print(usr,pas)
    if usr in db_student:
        if db_student[usr] == pas:
            Student_window()

    #Check if usr and pass match in Student Teacher or Admin table and login in accordingly
    #If usr and pass in student run Student_window function

window = Tk()
window.title("SCHOOL MANAGEMENT")

window.geometry("800x600")
window.configure(bg = "#666666")


canvas = Canvas(
    window,
    bg = "#666666",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    172.0,
    35.0,
    anchor="nw",
    text="School Management\n",
    fill="#FFFFFF",
    font=("Inter Bold", 36 * -1)
)

canvas.create_text(
    90.0,
    140.0,
    anchor="w",
    text="User ID",
    fill="#FFFFFF",
    font=("Inter Bold", 36 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    377.5,
    231.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    font = ('Arial 20'),
    bg="#D9D9D9",
    highlightthickness=0
)
entry_1.place(
    x=136.0,
    y=209.0,
    width=483.0,
    height=42.0
)

canvas.create_text(
    136.0,
    276.0,
    anchor="nw",
    text="Password\n",
    fill="#FFFFFF",
    font=("Inter Bold", 36 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    380.0,
    379.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    font = ('Arial 20'),
    show = '*',
    highlightthickness=0
)
entry_2.place(
    x=141.0,
    y=359.0,
    width=478.0,
    height=39.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command= lambda: autheticate(),
    relief="flat"
)
button_1.place(
    x=292.0,
    y=446.0,
    width=206.0,
    height=51.0
)
window.resizable(False, False)


window.mainloop()

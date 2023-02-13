from tkinter import ttk
from tkinter import * 
from tkinter import messagebox
from pathlib import Path
import sqlite3

con = sqlite3.Connection('Student1.db')
cur = con.cursor()
marks = []

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
        return choice


    # this is the function called when the button is clicked
    def Mark_List_Fetch():
        print(Mark_List.get())
        name = getInputBoxValue1()
        standard = getInputBoxValue2()
        if name == "" or standard == "":
            messagebox.showwarning("Invalid Input","Please enter a valid input")
        else:
            Student_Window_Result(name,standard,getSelectedComboItem())
        #Should finish with showing the table input
        print(name,standard)
    def Insert_MarkList():
        Student_Window_Insert()
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
    Mark_List= ttk.Combobox(root, values=['Quaterly', 'Half_Yearly', 'Finals'], font=('arial', 20, 'bold'), width=10)
    Mark_List.place(x=230, y=305)
    Mark_List.current(1)


    # This is the section of code which creates a button
    Button(root, text='Fetch MarkList', bg='#CCCCCC', font=('arial', 20, 'bold'), command=Mark_List_Fetch).place(x=400, y=378)
    Button(root,text='Insert MarkList', bg='#CCCCCC', font=('arial', 20, 'bold'), command=Insert_MarkList).place(x=150,y=378)


    root.mainloop()

def Student_Window_Result(name,standard,exam):
    window3 = Tk()
    window3.geometry("800x600")
    window3.configure(bg = "#666666")
    window3.title("Student's Detail")
    try:
        result = '''select * from {} where student_name='{}' and standard = '{}' '''.format(exam,name,standard)
        marks = cur.execute(result).fetchall()[0]
        print(marks)
    except IndexError:
        messagebox.showerror("Error","There is no record under the given name and standard!")
        window3.destroy()
    canvas = Canvas(
        window3,
        bg = "#666666",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        193.0,
        32.0,
        anchor="nw",
        text="Student’s Detail\n",
        fill="#FFFFFF",
        font=("Inter Bold", 36 * -1)
    )

    canvas.create_text(
        165.0,
        197.0,
        anchor="nw",
        text="English\n",
        fill="#FFFFFF",
        font=("Inter Bold", 20 * -1)
    )

    canvas.create_text(
        419.0,
        112.0,
        anchor="nw",
        text="Student’s Grade:\n",
        fill="#FFFFFF",
        font=("Inter Bold", 20 * -1)
    )

    canvas.create_text(
        31.0,
        112.0,
        anchor="nw",
        text="Student’s Name:\n",
        fill="#FFFFFF",
        font=("Inter Bold", 20 * -1)
    )

    canvas.create_text(
        165.0,
        249.0,
        anchor="nw",
        text="Language\n",
        fill="#FFFFFF",
        font=("Inter Bold", 20 * -1)
    )   

    entry_image_1 = PhotoImage(
        file=relative_to_assets("box1.png"))
    entry_bg_1 = canvas.create_image(
        512.5,
        215.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        highlightthickness=0,
        font=("Inter Bold", 20 * -1)
    )
    entry_1.place(
        x=390.0,
        y=201.0,
        width=245.0,
        height=27.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("box2.png"))
    entry_bg_2 = canvas.create_image(
        700.5,
        124.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#D9D9D9",
        highlightthickness=0,
        font=("Inter Bold", 20 * -1)
    )
    entry_2.place(
        x=607.0,
        y=110.0,
        width=187.0,
        height=27.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("box3.png"))
    entry_bg_3 = canvas.create_image(
        321.5,
        123.5,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#D9D9D9",
        highlightthickness=0,
        font=("Inter Bold", 20 * -1)
    )
    entry_3.place(
        x=229.0,
        y=110.0,
        width=185.0,
        height=25.0
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("box4.png"))
    entry_bg_4 = canvas.create_image(
        512.5,
        265.5,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#D9D9D9",
        highlightthickness=0,
        font=("Inter Bold", 20 * -1)
    )
    entry_4.place(
        x=390.0,
        y=251.0,
        width=245.0,
        height=27.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("box5.png"))
    entry_bg_5 = canvas.create_image(
        512.5,
        363.5,
        image=entry_image_5
    )
    entry_5 = Entry(
        bd=0,
        bg="#D9D9D9",
        highlightthickness=0,
        font=("Inter Bold", 20 * -1)
    )
    entry_5.place(
        x=390.0,
        y=349.0,
        width=245.0,
        height=27.0
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("box6.png"))
    entry_bg_6 = canvas.create_image(
        512.5,
        419.5,
        image=entry_image_6
    )
    entry_6 = Entry(
        bd=0,
        bg="#D9D9D9",
        highlightthickness=0,
        font=("Inter Bold", 20 * -1)
    )
    entry_6.place(
        x=390.0,
        y=405.0,
        width=245.0,
        height=27.0
    )

    entry_image_7 = PhotoImage(
        file=relative_to_assets("box7.png"))
    entry_bg_7 = canvas.create_image(
        512.5,
        313.5,
        image=entry_image_7
    )
    entry_7 = Entry(
        bd=0,
        bg="#D9D9D9",
        highlightthickness=0,
        font=("Inter Bold", 20 * -1)
    )
    entry_7.place(
        x=390.0,
        y=299.0,
        width=245.0,
        height=27.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("back.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda:window3.destroy(),
        relief="flat"
    )
    button_1.place(
        x=341.0,
        y=494.0,
        width=119.0,
        height=35.0
    )

    canvas.create_text(
        169.0,
        302.0,
        anchor="nw",
        text="Chemistry\n",
        fill="#FFFFFF",
        font=("Inter Bold", 20 * -1)
    )

    canvas.create_text(
        165.0,
        355.0,
        anchor="nw",
        text="Physics",
        fill="#FFFFFF",
        font=("Inter Bold", 20 * -1)
    )

    canvas.create_text(
        165.0,
        409.0,
        anchor="nw",
        text="Maths",
        fill="#FFFFFF",
        font=("Inter Bold", 20 * -1)
    )
    entry_1.insert(0," "*18+str(marks[3]))
    entry_4.insert(0," "*18+str(marks[4]))
    entry_7.insert(0," "*18+str(marks[5]))
    entry_5.insert(0," "*18+str(marks[6]))
    entry_6.insert(0," "*18+str(marks[7]))
    entry_2.insert(0,marks[2])
    entry_3.insert(0,marks[1])
    window3.resizable(False, False)
    window3.mainloop()

def insert_value(name,grade,term,english,language,chemistry,physics,maths):
    #SQL COMMAND TO INSERT
    roll_1 = 'Select count(rollno) from '+term
    exc = cur.execute(roll_1)
    roll = exc.fetchall()[0][0]
    cmd = '''insert into '''+term+''' values('{}','{}','{}','{}','{}','{}','{}','{}')'''.format(roll+1,name,grade,english,language,chemistry,physics,maths)
    cur.execute(cmd)
    con.commit()
    print(name,grade,term,english,language,chemistry,physics,maths)
    messagebox.showinfo("Alert","Your value has been successfully added!")

def Student_Window_Insert():
    window4 = Tk()
    window4.title("Student Data Insertion")
    window4.geometry("800x600")
    window4.configure(bg = "#666666")


    canvas = Canvas(
        window4,
        bg = "#666666",
        height = 600,
        width = 800,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge"
    )

    canvas.place(x = 0, y = 0)
    canvas.create_text(
        193.0,
        32.0,
        anchor="nw",
        text="Student’s Detail\n",
        fill="#FFFFFF",
        font=("Inter Bold", 36 * -1)
    )

    canvas.create_text(
        165.0,
        266.0,
        anchor="nw",
        text="English\n",
        fill="#FFFFFF",
        font=("Inter Bold", 20 * -1)
    )

    canvas.create_text(
        397.0,
        128.0,
        anchor="nw",
        text="Student’s Grade:\n",
        fill="#FFFFFF",
        font=("Inter Bold", 20 * -1)
    )

    canvas.create_text(
        9.0,
        128.0,
        anchor="nw",
        text="Student’s Name:\n",
        fill="#FFFFFF",
        font=("Inter Bold", 20 * -1)
    )

    canvas.create_text(
        165.0,
        318.0,
        anchor="nw",
        text="Language\n",
        fill="#FFFFFF",
        font=("Inter Bold", 20 * -1)
    )

    entry_image_1 = PhotoImage(
        file=relative_to_assets("box_insert1.png"))
    entry_bg_1 = canvas.create_image(
        512.5,
        284.5,
        image=entry_image_1
    )
    entry_1 = Entry(
        bd=0,
        bg="#D9D9D9",
        highlightthickness=0,
        font=("Inter Bold", 36 * -1)
    )
    entry_1.place(
        x=390.0,
        y=270.0,
        width=245.0,
        height=27.0
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("box_insert2.png"))
    entry_bg_2 = canvas.create_image(
        678.5,
        140.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        bd=0,
        bg="#D9D9D9",
        highlightthickness=0,
        font=("Inter Bold", 36 * -1)
    )
    entry_2.place(
        x=585.0,
        y=126.0,
        width=187.0,
        height=27.0
    )

    entry_image_3 = PhotoImage(
        file=relative_to_assets("box_insert3.png"))
    entry_bg_3 = canvas.create_image(
        299.5,
        139.5,
        image=entry_image_3
    )
    entry_3 = Entry(
        bd=0,
        bg="#D9D9D9",
        highlightthickness=0,
        font=("Inter Bold", 36 * -1)
    )
    entry_3.place(
        x=207.0,
        y=126.0,
        width=185.0,
        height=25.0
    )

    canvas.create_text(
        173.0,
        189.0,
        anchor="nw",
        text="Exam Term",
        fill="#FFFFFF",
        font=("Inter Bold", 20 * -1)
    )

    entry_image_4 = PhotoImage(
        file=relative_to_assets("box_insert4.png"))
    entry_bg_4 = canvas.create_image(
        512.5,
        334.5,
        image=entry_image_4
    )
    entry_4 = Entry(
        bd=0,
        bg="#D9D9D9",
        highlightthickness=0,
        font=("Inter Bold", 36 * -1)
    )
    entry_4.place(
        x=390.0,
        y=320.0,
        width=245.0,
        height=27.0
    )

    entry_image_5 = PhotoImage(
        file=relative_to_assets("box_insert5.png"))
    entry_bg_5 = canvas.create_image(
        512.5,
        432.5,
        image=entry_image_5
    )
    entry_5 = Entry(
        bd=0,
        bg="#D9D9D9",
        highlightthickness=0,
        font=("Inter Bold", 36 * -1)
    )
    entry_5.place(
        x=390.0,
        y=418.0,
        width=245.0,
        height=27.0
    )

    entry_image_6 = PhotoImage(
        file=relative_to_assets("box_insert6.png"))
    entry_bg_6 = canvas.create_image(
        512.5,
        488.5,
        image=entry_image_6
    )
    entry_6 = Entry(
        bd=0,
        bg="#D9D9D9",
        highlightthickness=0,
        font=("Inter Bold", 36 * -1)
    )
    entry_6.place(
        x=390.0,
        y=474.0,
        width=245.0,
        height=27.0
    )

    entry_image_7 = PhotoImage(
        file=relative_to_assets("box_insert7.png"))
    entry_bg_7 = canvas.create_image(
        512.5,
        382.5,
        image=entry_image_7
    )
    entry_7 = Entry(
        bd=0,
        bg="#D9D9D9",
        highlightthickness=0,
        font=("Inter Bold", 36 * -1)
    )
    entry_7.place(
        x=390.0,
        y=368.0,
        width=245.0,
        height=27.0
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("insert.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: insert_value(entry_3.get(),entry_2.get(),term.get(),entry_1.get(),entry_4.get(),entry_7.get(),entry_5.get(),entry_6.get()),
        relief="flat"
    )
    button_1.place(
        x=367.0,
        y=527.0,
        width=119.0,
        height=35.0
    )

    canvas.create_text(
        169.0,
        371.0,
        anchor="nw",
        text="Chemistry\n",
        fill="#FFFFFF",
        font=("Inter Bold", 20 * -1)
    )

    canvas.create_text(
        165.0,
        424.0,
        anchor="nw",
        text="Physics",
        fill="#FFFFFF",
        font=("Inter Bold", 20 * -1)
    )

    canvas.create_text(
        165.0,
        478.0,
        anchor="nw",
        text="Maths",
        fill="#FFFFFF",
        font=("Inter Bold", 20 * -1)
    )

    canvas.create_text(
        406.0,
        189.0,
        anchor="nw",
        text="Dummy",
        fill="#FFFFFF",
        font=("Inter Bold", 20 * -1)
    )
    term = ttk.Combobox(window4,values=['Quaterly', 'Half_Yearly', 'Finals'], font=('arial', 20, 'bold'), width=10)
    term.place(x=406.0,y=189.0)
    term.current(1)

    print([marks[3]])



    window4.resizable(False, False)
    window4.mainloop()

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")
authenticated = False
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

db_student = {"admin":"admin"}
db_teacher = {"teacher":"teacher"}

def autheticate():
    usr = entry_1.get()
    pas = entry_2.get()
    print(usr,pas)
    if usr in db_student:
        if db_student[usr] == pas:
            Student_window()
        else:
            messagebox.showerror("Incorrect Password","Please enter the correct password")
    else:
        messagebox.showerror("User not found","There is no such user!")
    #Check if usr and pass match in Student Teacher or Admin table and login in accordingly
    #If usr and pass in student run Student_window function
window = Tk()
window.title("STUDENT MANAGEMENT")

window.geometry("800x600")
window.configure(bg = "#666666")
window.bind('<Return>',lambda event:autheticate())


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
text="Student Management\n",
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
entry_2.bind()

button_image_1 = PhotoImage(
file=relative_to_assets("submit.png"))
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

con.commit()
con.close()

'''
entry1 = english
entry2 = standard
entry3 = Name
entry4 = language
entry5 = physics
entry6 = maths
entry7 = chemistry
'''

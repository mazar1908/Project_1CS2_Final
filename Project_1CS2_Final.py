from tkinter import *
from tkinter import ttk


def enter_data() -> None:
    '''
    Function: Save the information of students who enroll in intro to computer science 2 class.
    :return: prints the infromation of students enrolled
    '''
    valid = valid_var.get()
    if valid == 'Box ticked':
        firstname = fname_entry.get()
        lastname = lname_entry.get()
        NUID = NUID_entry.get()
        if firstname and lastname and NUID:
            major = major_combobox.get()
            age = age_box.get()
            year = year_combobox.get()
            #NUID = NUID_entry.get()
            General_ed_prerequisite = Prerequisite1_var.get()
            #Intro_to_CS1_prerequisite = Prerequisite2_var.get()

            print('First name: ',firstname, 'Last name: ',lastname, 'Major: ',major)
            print('Age: ',age, 'Year: ',year, 'NUID Number: ',NUID)
            print('Prerequisite 1 (General Eds): ', General_ed_prerequisite)
            #print('Prerequisite 2 (Intro to CS 1): ', Intro_to_CS1_prerequisite)
            print('----------------------------------------------------------------')
        else:
            print('Error! must include your first name and last name and NUID number.')
    else:
        print('You cant register in this class because you have not yet completted Intro to CS 1:( \nContact an advior for more information.')

#setting up the Tk
window = Tk()
window.title('Intro to Computer Science II registration form')
window.geometry('450x450')
window.resizable(False, False)

#title frame and label
frame_title = Frame(window)
frame_title.pack()

student_information = Label(frame_title, text='Student Information for Intro to CS 2 Class Registration')
student_information.pack()

#student information(1) frame and labels (Firstname, Lastname, Major)
frame_FLM = Frame(window)
frame_FLM.pack()

#labels(1) (Firstname, Lastname, Major)
first_name = Label(frame_FLM, text='First Name', anchor='w')
first_name.pack(side='left', padx = 40, pady = 10)

last_name = Label(frame_FLM, text='Last Name', anchor='w')
last_name.pack(side='left', padx = 40, pady = 10)

major = Label(frame_FLM, text='Major')
major.pack(padx = 40, pady = 10)

#Entry frame(1) (Firstname, Lastname, Major)
frame_entry_FLM = Frame(window)
frame_entry_FLM.pack()

fname_entry = Entry(frame_entry_FLM)
fname_entry.pack(side='left', padx = 5, pady = 5)

lname_entry = Entry(frame_entry_FLM)
lname_entry.pack(side='left', padx = 5, pady = 5)

major_label = Label(frame_entry_FLM)
major_combobox = ttk.Combobox(frame_entry_FLM, values=['Computer science','Computer Engineering', 'CyberSecurity','Information Technology','Biology','Chemistry','Physics','Civil Engineering','Aviation','Undecided','Other'])
major_label.pack(side='left', padx = 5, pady = 5)
major_combobox.pack(side='left', padx = 5, pady = 5)

#student information(2) frame and labels (Age, Year, NUID)
frame_AYN = Frame(window)
frame_AYN.pack()

#labels(2) (Age, Year, NUID)
age = Label(frame_AYN, text='Age', anchor='w')
age.pack(side='left', padx = 60, pady = 20)

year = Label(frame_AYN, text='Year', anchor='w')
year.pack(side='left', padx = 40, pady = 20)

NUID = Label(frame_AYN, text='NUID Number')
NUID.pack(padx = 50, pady = 20)

#Entry frame(2) (Age, Year, NUID)
frame_entry_AYN = Frame(window)
frame_entry_AYN.pack()

age = Entry(frame_entry_AYN)
#age.pack(side='left', padx = 5, pady = 5)
age_box = Spinbox(frame_entry_AYN, from_=14, to=120)
age_box.pack(side='left', padx = 5, pady = 5)

year_combobox = ttk.Combobox(frame_entry_AYN, values=['Freshman', 'Sophmore', 'Junior', 'Senior', '5th-year and above'])
year_combobox.pack(side='left', padx = 5, pady = 5)

NUID_entry = Entry(frame_entry_AYN)
NUID_entry.pack(side='left', padx = 5, pady = 5)

#Prerequisites frame and labels(3) frame and labels (General Eds, Intro to CS 1)
frame_Prerequisites = Frame(window)
frame_Prerequisites.pack(pady=20)

Prerequisite1_label = Label(frame_Prerequisites, text='are you done with all of your General Eds?')
Prerequisite1_label.pack(side='top')
Prerequisite2_label = Label(frame_Prerequisites, text='Did you take and complete Intro to CS I with at least a C?')
Prerequisite2_label.pack(side='bottom')

#Entry frame(3) (General Eds, Intro to CS 1)
Prerequisites_entryframe = Frame(window)
Prerequisites_entryframe.pack()

#THIS IS A TEST
#valid_var = StringVar(value = 'Box unticked')
#Prerequisite1_entry = Checkbutton(Prerequisites_entryframe, text='Yes or no', variable=valid_var, onvalue='Box ticked' , offvalue='Box unticked')

Prerequisite1_var = StringVar(value = 'General Ed Classes not Complete')
Prerequisite1_entry = Checkbutton(Prerequisites_entryframe, text='I did finish all my General Ed classes', variable=Prerequisite1_var, onvalue='General Ed Classes Completed' , offvalue='General Ed Classes not Complete')
Prerequisite1_entry.pack(side='top')

valid_var = StringVar(value = 'Box unticked')
Prerequisite2_entry = Checkbutton(Prerequisites_entryframe, text='I took and passed Intro to CS 1 with at least a C grade', variable=valid_var, onvalue='Box ticked', offvalue= 'Box unticked')
Prerequisite2_entry.pack(side='bottom')

#enroll button
frame_enroll = Frame(window)
frame_enroll.pack()
button = Button(frame_enroll, text='Enroll in class', command = enter_data)
button.pack(pady=30)


window.mainloop()
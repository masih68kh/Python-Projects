import tkinter as tk
import pickle
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib
matplotlib.use('TkAgg')

import sys
sys.setrecursionlimit(5000)

class Course:
    
    def __init__(self, name):
        self.name = name
        self.slots = []
    def add_slot(self, slot):
        '''
        slot is a list with the following signature:
        [from, to, day]
        '''
        self.slots.append(slot)
    def del_slot(self, slot):
        '''
        slot is a list with the following signature:
        [from, to, day]
        '''
        self.slots.remove(self, slot)
    def num_slots(self):
        return len(self.slots)



try:
    with open('list_of_courses.pkl', 'rb') as fp:
        course_list = pickle.load(fp)
except:
    course_list = []
    print("couldn't open the course list saved")

config = {}
'''
<config> signature:
config = {"add": [] , "del": [] , "clear_all": 0}
<"add"> keyword is a list of courses needs to be added
<"del"> keyword is a list of courses needs to be deleted
<"clear_all"> value is 0: no clear_all, or 1: clear_all
'''
config['clear_all'] = 0
config['del'] = []
window = tk.Tk()
window.title('Hi, converting numbers')
window.geometry("600x500")

# ** Global Vars:
course_name_value = tk.StringVar()
day_slot1 = tk.StringVar()
to_slot1_value = tk.StringVar()
from_slot1_value = tk.StringVar()
to_slot2_value = tk.StringVar()
from_slot2_value = tk.StringVar()
to_slot3_value = tk.StringVar()
from_slot3_value = tk.StringVar()
day_slot2 = tk.StringVar()
day_slot3 = tk.StringVar()
#course_list = []
# ***********************************


def show_plot_act():
    from week_schedule_window import show_plot
    mat = show_plot(course_list, config)

def clear():
    show_data.delete('1.0',tk.END)
    global show_data_string
    show_data_string = ''
    global course_list
    course_list = []
    config['clear_all'] = 1

show_data_string = ''
def show_data_act():
    whole_data_show = ''
    for crs in course_list:
        temp_str = "\nCourse: " + crs.name + '\n'
        for i in range(len(crs.slots)):
               temp_str += 'From ' + str(crs.slots[i][0]) + ' to ' + str(crs.slots[i][1]) + ' on ' + crs.slots[i][2]+'\n'
        whole_data_show += temp_str
    show_data.delete('1.0',tk.END)
    show_data.insert('1.0', whole_data_show)
    # save data:
    with open('list_of_courses.pkl', 'wb') as fp:
        pickle.dump(course_list, fp)
    


def add_data_act():
    temp_course = Course(course_name.get())
    temp_course.add_slot([float(from_slot1.get()), float(to_slot1.get()), day_slot1.get()])
    if (from_slot2.get() != ''):
        temp_course.add_slot([float(from_slot2.get()), float(to_slot2.get()), day_slot2.get()])
    if (from_slot3.get() != ''):
        temp_course.add_slot([float(from_slot3.get()), float(to_slot3.get()), day_slot3.get()])
    course_list.append(temp_course)
    del temp_course
    ## clearing the fields**************************************
    show_data.delete('1.0', tk.END)
    show_data.insert(tk.END, "New Data is added successfully")
    day_slot1.set('')
    day_slot2.set('')
    day_slot3.set('')
    course_name.delete(0,'end')
    to_slot1.delete(0,'end')
    to_slot2.delete(0,'end')
    to_slot3.delete(0,'end')
    from_slot1.delete(0,'end')
    from_slot2.delete(0,'end')
    from_slot3.delete(0,'end')
    # *********************************************************

def remove_data_act():
     for crs in course_list:
        if crs.name == course_name.get():
            config['del'].append(crs.name)
            course_list.remove(crs)
            show_data.delete('1.0', tk.END)
            show_data.insert(tk.END, "Course {} is removed successfully".format(crs.name))
            break



####### Row 1 ************
course_name = tk.Entry(window,textvariable=course_name_value)
course_name.grid(row=1, column=1)
tk.Label(window, text='Course Name').grid(row=1,column=0)

days_of_week = { 'Monday','Tuesday','Wednesday','Thursday','Friday', 'Saturday', 'Sunday', ''}
####### Row 2 ************
to_slot1 = tk.Entry(window,textvariable=to_slot1_value)
to_slot1.grid(row=2, column=3)
from_slot1 = tk.Entry(window,textvariable=from_slot1_value)
from_slot1.grid(row=2, column=1)
l2_from = tk.Label(window, text='From')
l2_from.grid(row=2,column=0, sticky=tk.E)
days2 = tk.OptionMenu(window, day_slot1, *days_of_week)
days2.grid(row=2, column=5)
tk.Label(window, text='To').grid(row=2,column=2, sticky=tk.E)
tk.Label(window, text='Day').grid(row=2,column=4, sticky=tk.E)
####### Row 3 ************
to_slot2 = tk.Entry(window,textvariable=to_slot2_value)
to_slot2.grid(row=3, column=3)
from_slot2 = tk.Entry(window,textvariable=from_slot2_value)
from_slot2.grid(row=3, column=1)
tk.Label(window, text='From').grid(row=3,column=0, sticky=tk.E)
days3 = tk.OptionMenu(window, day_slot2, *days_of_week)
days3.grid(row=3, column=5)
tk.Label(window, text='To').grid(row=3,column=2, sticky=tk.E)
tk.Label(window, text='Day').grid(row=3,column=4, sticky=tk.E)
####### Row 4 ************
to_slot3 = tk.Entry(window,textvariable=to_slot3_value)
to_slot3.grid(row=4, column=3)
from_slot3 = tk.Entry(window,textvariable=from_slot3_value)
from_slot3.grid(row=4, column=1)
tk.Label(window, text='From').grid(row=4,column=0, sticky=tk.E)
days4 = tk.OptionMenu(window, day_slot3, *days_of_week)
days4.grid(row=4, column=5)
tk.Label(window, text='To').grid(row=4,column=2, sticky=tk.E)
tk.Label(window, text='Day').grid(row=4,column=4, sticky=tk.E)

show_data = tk.Text(window, width=60, height=20)
show_data.grid(row=5, column=0, columnspan=8)


add_B = tk.Button(master=window, text='  Add  ', command=add_data_act)
add_B.grid(row=0,column=0)
remove_B = tk.Button(master=window, text='Remove', command=remove_data_act)
remove_B.grid(row=0,column=1)
clear_B = tk.Button(master=window, text='Clear All', command=clear)
clear_B.grid(row=0,column=2)
show_B = tk.Button(master=window, text='Show Data and Save', command=show_data_act)
show_B.grid(row=0,column=3)
plot_B = tk.Button(master=window, text='Show Plot', command=show_plot_act)
plot_B.grid(row=0,column=4)



window.mainloop()



'''
at this point we have a list called <course_list>. This list consists of Course objects that each 
<Course> object has the following attributes:
Course.name  :  is the name of the course
Course.slots :  is a list with the following signature: [<slot1>, <slot2>, ...]
    each <slot> is again a list with the following signature: [<from>, <to>, <day>]
        <from> is int
        <to> is int
        <day> is str
'''


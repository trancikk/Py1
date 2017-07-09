from Tkinter import *
import processing
import Dialog
import serial
from person import  *
from processing import *
from tkMessageBox import *


win = Tk()
win.title('Gen processing program')
# win.width=2000
# =Toplevel(root)
# win.title='cool'
form = Label(win, text='Fill this form:')
# form.title='cool'
form.pack(side=TOP)
gens_list = serial.load('gens_list')
#print gens_list


class Form_and_text(Frame):
    
    def __init__(self, parent=None, form_text=None):
        self.frame = Frame(parent)
        self.form_txt = Label(self.frame, text='Fill gen %s' % form_text)
        self.form_txt.pack(side=LEFT)
        self.form_entry = Entry(self.frame)
        self.form_entry.pack(side=RIGHT)
        self.frame.pack(side=TOP, expand=YES, fill=BOTH)
    
    def get(self):
        return self.form_entry.get()
        # return self
'''text1=Label(win, text='Gen1:')
text1.pack(side=LEFT)    
form1=Entry(win)
form1.pack(side=RIGHT)
form2=Entry(win)
form3=Entry(win)
form4=Entry(win)
form5=Entry(win)'''

form = dict()

for i in gens_list:
    form[i] = Form_and_text(win, i)
    
def printme(event):
    for i in form:
        print form[i].get()       

b = Button(win, text='Click me')

def proc(event):
    person=Example_Person([form[i].get() for i in form],[i for i in form])
    print person.printGens()
    person.normaliseGens(gens_list)
    person_gens=person.getNormalGen()
    print person_gens
    showinfo('OK',calculate(person_gens))
    
def pp(event):
    print 'pp'

b.bind('<Button-1>', proc)

b.pack()
#win.pack()
win.mainloop()

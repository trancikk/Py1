from Tkinter import *
import processing
import Dialog
import serial
from click.decorators import command


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
        self = Frame(parent)
        self.form_text = Label(self, text='Fill gen %s' % form_text)
        self.form_text.pack(side=LEFT)
        self.form_entry = Entry(self)
        self.form_entry.pack(side=RIGHT)
        self.pack(side=TOP, expand=YES, fill=BOTH)
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
        print i       
b = Button(win, text='Click me')
def pp(event):
    print 'pp'
b.bind('<Button-1>', printme)

b.pack()
#win.pack()
win.mainloop()

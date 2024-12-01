import tkinter
import firebase_admin
from firebase_admin import db, credentials
from firebase_admin import firestore

# Use the application default credentials.
cred = credentials.Certificate('credentials.json')
firebase_admin.initialize_app(cred, {"databaseURL": "https://to-do-for-you-default-rtdb.firebaseio.com/"})

#create reference to root node
ref = db.reference('/')
list_ref = ref.child('items')
items = list_ref.get()

bg_color = '#eeecc2'
list_color = '#dfd2ae'

class CheckBtn(tkinter.Checkbutton):
    def __init__(self, master=None, **kw):
        super().__init__(master, **kw)
        self.config(bg=list_color)
        self.config(command=self.click_function)
        self.variable = 0
    def click_function(self):
        if self.variable == 0:
            self.variable = 1
        elif self.variable == 1:
            self.variable = 0
        if self.variable == 1:
            list_ref.update({self['text']: True})
        if self.variable == 0:
            list_ref.update({self['text']: False})
    def check(self):
        self.variable = 1
        self.select()

def set_item(item, root):

    new_frame = tkinter.Frame(root)
    checkbtn = CheckBtn(new_frame, text=item).grid(column=0, row=0)
    delete_btn = tkinter.Button(new_frame, text='X', bg=list_color, command=lambda: [delete_db_item(item), new_frame.destroy()]).grid(column=1, row=0)
    new_frame.grid(sticky='w')
    add_db_item(item)

def load(root):
    items = list_ref.get()
    if items:
        for item in items:
            set_item(item, root)
def add_db_item(item):
    if list_ref.get()[item] == True:
        list_ref.update({item: True})
    else:
        list_ref.update({item: False})


def delete_db_item(item):
    list_ref.child(item).delete()

def check_item(var, item):
    if var == 1:
        list_ref.update({item: True})
    if var == 0:
        list_ref.update({item: False})
def add_item():


    frame = tkinter.Frame(root)
    frame.configure(bg=bg_color)
    textbox = tkinter.Entry(frame)
    textbox.grid(column=0, row=0)
    create_btn = tkinter.Button(frame, text='✓', command=lambda: [set_item(textbox.get(), root), frame.destroy()], bg=bg_color).grid(column=1, row=0)
    frame.grid(sticky='w')
    textbox.focus()



root = tkinter.Tk(className='For You To-Do')
root.geometry('400x400')
root.configure(bg=bg_color)
add_btn = tkinter.Button(root, text='+', width=10, bg=bg_color)
add_btn['command'] = add_item 
add_btn.grid(sticky='w')

load(root)

root.mainloop()


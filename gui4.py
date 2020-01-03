import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('Label frame')

label_frame = ttk.LabelFrame(win, text='Enter your detail below')
label_frame.grid(row=0,column=0, padx=40)

label = ['what is your name','what is your age','what is your gender : ','country : ',
'state : ','city : ']

for i in range(len(label)):
    cur_label = 'label' + str(i)
    cur_label = ttk.Label(label_frame, text = label[i])
    cur_label.grid(row=i, column=0, sticky=tk.W, padx=2, pady=2)

name_var=tk.StringVar()
user_info = {
    'name':tk.StringVar(),
    'age':tk.StringVar(),
    'gender':tk.StringVar(),
    'country':tk.StringVar(),
    'state':tk.StringVar(),
    'city':tk.StringVar(),
}
count=0
for i in user_info:
    cur_entrybox = 'entry' + i
    cur_entrybox = ttk.Entry(label_frame, width=16, textvariable=user_info[i])
    cur_entrybox.grid(row=count, column=1, padx=2, pady=2)
    count +=1

def submit():
    print(user_info.get('name').get())
    print(user_info.get('age').get())
    print(user_info.get('gender').get())
    print(user_info.get('country').get())
    print(user_info.get('state').get())
    print(user_info.get('city').get())

submit_btn = ttk.Button(win, text='Submit', command=submit)
submit_btn.grid(row=1, columnspan=2)

for child in label_frame.winfo_children():
    child.grid_configure(padx=4, pady=4)

win.mainloop()
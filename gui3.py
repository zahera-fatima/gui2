import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title('Loop')

label = ['what is your name','what is your age','what is your gender : ','country : ',
'state : ','city : ']

for i in range(len(label)):
    cur_label = 'label' + str(i)
    cur_label = ttk.Label(win, text = label[i])
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
    cur_entrybox = ttk.Entry(win, width=16, textvariable=user_info[i])
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
submit_btn.grid(row=6, columnspan=2)
win.mainloop()
import tkinter as tk
import datetime as dt
from time import strftime
from service import login_service_permission as ps, login_service as ls


def tk_window():
    return tk.Tk()


def start():
    root = tk_window()
    root.geometry("375x667")
    root.title("DBMS Login Page")

    def time():
        string = strftime('%H:%M:%S')
        lbl.config(text=string)
        lbl.after(1000, time)

    def submit_act(username, password):
        user = username.get()
        password_get = password.get()
        return check_password(user, password_get)

    lbl = tk.Label(root, font=('century gothic', 40, 'bold'))
    lbl.place(x=80, y=150)
    time()

    date = dt.datetime.now()
    label = tk.Label(root, text=f"{date:%A, %B %d, %Y}", font=('century gothic', 12))
    label.place(x=60, y=210)

    lbl_first_row = tk.Label(root, text="Username")
    lbl_first_row.place(x=70, y=500)

    quit_button = tk.Button(root, text='Quit', command=root.withdraw)
    quit_button.place(x=330, y=10)

    username_entry = tk.Entry(root, width=50)
    username_entry.place(x=150, y=500, width=150)

    lbl_sec_row = tk.Label(root, text="Password")
    lbl_sec_row.place(x=70, y=530)

    pass_entry = tk.Entry(root, width=50)
    pass_entry.place(x=150, y=530, width=150)

    submit_btn = tk.Button(root, text="Login", command=lambda: submit_act(username_entry, pass_entry))
    submit_btn.place(x=40, y=585, width=300, height=50)

    copy_mark = tk.Label(root, text='Made by Edward and Andreas')
    copy_mark.place(x=0, y=0)

    notification_text = tk.Label(root, text='Welcome!', fg='red')
    notification_text.place(x=160, y=555)

    def close():
        root.withdraw()

    def check_password(user, password):
        my_result = ls.login_to_db()
        admin = my_result[0][1]
        parent = my_result[0][2]
        guest = my_result[0][4]
        child = my_result[0][3]

        if user == 'admin' and password == admin:
            close()
            return ps.read_perm(user)

        elif user == 'parent' and password == parent:
            close()
            return ps.read_perm(user)

        elif user == 'guest' and password == guest:
            close()
            return ps.read_perm(user)

        elif user == 'child' and password == child:
            close()
            return ps.read_perm(user)

        elif user == '' or password == '':
            notification_text.config(text='Username or password cannot be empty!')
            notification_text.place(x=80, y=555)

        else:
            notification_text.config(text="Username or password is incorrect!")
            notification_text.place(x=90, y=555)

    root.mainloop()

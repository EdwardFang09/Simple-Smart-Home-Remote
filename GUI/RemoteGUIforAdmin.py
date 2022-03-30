import tkinter as tk
import datetime as dt
from service import admin_service as ads
from GUI import LoginPageGUI as Lg
from time import strftime


def run():
    # GUI
    wss = tk.Tk()
    wss.title("Remote GUI")
    wss.geometry("375x667")

    def time():
        string = strftime('%H:%M:%S')
        lbl.config(text=string)
        lbl.after(1000, time)

    # Time
    time_label = tk.LabelFrame(wss, text="Time")
    time_label.pack(expand='yes', fill='both')

    def main_gui():
        wss.withdraw()
        Lg.start()

    def submit_act(username, old_pass, password, notification):
        user = username.get()
        old_password = old_pass.get()
        new_password = password.get()
        ads.login_to_db(user, old_password, new_password, notification)

    lbl = tk.Label(time_label, font=('century gothic', 40, 'bold'))
    lbl.place(x=80, y=0)
    time()

    date = dt.datetime.now()
    label = tk.Label(time_label, text=f"{date:%A, %B %d, %Y}", font=('century gothic', 12))
    label.place(x=60, y=60)

    # Status
    mode_label = tk.LabelFrame(wss, text="Status")
    mode_label.pack(expand='yes', fill='both')

    time_label = tk.Label(mode_label, text="Hello, Admin!")
    time_label.place(x=10, y=10)

    logout_button = tk.Button(mode_label, text="Logout", command=main_gui)
    logout_button.place(x=300, y=10)

    # Admin Tools
    adm_label = tk.LabelFrame(wss, text="Admin Tools")
    adm_label.pack(expand='yes', fill='both')

    lbl_first_row = tk.Label(adm_label, text="Username: ")
    lbl_first_row.place(x=10, y=0)

    username_entry = tk.Entry(adm_label, width=50)
    username_entry.place(x=100, y=0, width=150)

    old_password_label = tk.Label(adm_label, text="Old Password: ")
    old_password_label.place(x=10, y=20)

    old_pass_entry = tk.Entry(adm_label, width=50)
    old_pass_entry.place(x=100, y=20, width=150)

    new_password_label = tk.Label(adm_label, text="New Password: ")
    new_password_label.place(x=10, y=40)

    new_pass_entry = tk.Entry(adm_label, width=50)
    new_pass_entry.place(x=100, y=40, width=150)

    # Empty slot
    empty_slot1 = tk.LabelFrame(wss)
    empty_slot1.pack(expand='yes', fill='both')

    notification_text = tk.Label(empty_slot1, text='Welcome!', fg='red')
    notification_text.place(x=160, y=50)

    submit_btn = tk.Button(adm_label, text="Change password",
                           command=lambda: submit_act(username_entry,
                                                      old_pass_entry, new_pass_entry, notification_text))
    submit_btn.place(x=30, y=75, width=320)

    empty_slot2 = tk.LabelFrame(wss)
    empty_slot2.pack(expand='yes', fill='both')

    wss.mainloop()

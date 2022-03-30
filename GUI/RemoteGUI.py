import tkinter as tk
from time import strftime
from tkinter.ttk import *
import datetime as dt
from GUI import LoginPageGUI as Lg
from service import main_service as ms, automatic_service as asv, simulator_service as ss
import threading

# init
lock = threading.Lock()
running = False
hour = -1

old_bedroom_ac_sensor = ''
old_bedroom_light_sensor = ''
old_bedroom_music_sensor = ''

old_bathroom_light_sensor = ''
old_bathroom_music_sensor = ''

old_living_room_ac_sensor = ''
old_living_room_light_sensor = ''
old_living_room_music_sensor = ''

old_kitchen_ac_sensor = ''
old_kitchen_light_sensor = ''
old_kitchen_music_sensor = ''


def main_run(number, user):
    def run():
        def in_run_1():
            def simulate_time_only():
                global hour
                my_hour = hour
                if my_hour == 23:
                    my_hour = -1
                my_hour = my_hour + 1
                hour = my_hour
                lbl.config(text=f'{hour}:00:00')

                lbl.after(1000, simulate_time_only)

            def main_gui():
                ms.write('auto_mode', 'mode', 0)
                wss.destroy()
                Lg.start()

            def time_real():
                string = strftime('%H:%M:%S')
                lbl.config(text=string)
                lbl.after(1000, time_real)

            def automatic(switch1):
                switch1["state"] = tk.DISABLED

            def manual(switch1):
                switch1["state"] = tk.NORMAL

            def remote_mode_func():
                ms.mode_convert(dummy_label, remote_mode_button, 'auto_mode', 'mode',
                                on, off)
                return remote_config()

            def remote_config():
                if remote_mode_button.config('text')[-1] == 'Manual':
                    group_manual()

                else:
                    group_automatic()
                    check_file()

            def group_manual():
                manual(ac_button1)
                manual(music_button1)
                manual(bulb_button1)

                manual(music_button2)
                manual(bulb_button2)

                manual(ac_button3)
                manual(music_button3)
                manual(bulb_button3)

                manual(ac_button4)
                manual(music_button4)
                manual(bulb_button4)

            def group_automatic():
                automatic(ac_button1)
                automatic(music_button1)
                automatic(bulb_button1)

                automatic(music_button2)
                automatic(bulb_button2)

                automatic(ac_button3)
                automatic(music_button3)
                automatic(bulb_button3)

                automatic(ac_button4)
                automatic(music_button4)
                automatic(bulb_button4)

            ms.write('auto_mode', 'mode', 0)

            # GUI
            wss = tk.Tk()
            wss.title("Remote GUI")
            wss.geometry("375x667")

            # Time
            time_label = tk.LabelFrame(wss, text="Time")
            time_label.pack(expand='yes', fill='both')

            lbl = tk.Label(time_label, font=('century gothic', 40, 'bold'))
            lbl.place(x=80, y=0)
            simulate_time_only()

            date = dt.datetime.now()
            label = Label(time_label, text=f"{date:%A, %B %d, %Y}", font=('century gothic', 12))
            label.place(x=60, y=60)

            dummy_label = tk.Label(time_label)

            def greetings(name):
                return f'Hello, {name}!'

            greet = greetings(user)

            # Status
            mode_label = tk.LabelFrame(wss, text="Status")
            mode_label.pack(expand='yes', fill='both')

            time_label = tk.Label(mode_label, text=greet)
            time_label.place(x=10, y=10)

            logout_button = tk.Button(mode_label, text="Logout", command=main_gui)
            logout_button.place(x=305, y=8)

            guest_mode = 0
            guest_room_text = ms.read('guest_mode', guest_mode)
            g = tk.Label(mode_label, text="Guest Mode")
            g.place(x=250, y=50)
            guest_room_button = tk.Button(mode_label, text=guest_room_text)
            guest_room_button.config(command=lambda: ms.mode_convert(g, guest_room_button, 'guest_mode', 'mode'))
            guest_room_button.place(x=320, y=48)
            ms.mode_state(g, guest_room_button, 'guest_mode', guest_mode, 'mode')

            remote_mode = 0
            remote_mode_text = ms.read('auto_mode', remote_mode)
            on = 'Automatic'
            off = 'Manual'
            remote_label = tk.Label(mode_label, text="Mode")
            remote_label.place(x=10, y=50)
            remote_mode_button = tk.Button(mode_label, text=remote_mode_text)
            remote_mode_button.config(command=remote_mode_func)
            remote_mode_button.place(x=70, y=48)
            ms.mode_state(dummy_label, remote_mode_button, 'auto_mode', remote_mode, 'mode', on, off)

            # Bedroom
            ws = tk.LabelFrame(wss, text="Bedroom")
            ws.pack(expand='yes', fill='both')

            # Bedroom AC
            bedroom_ac = 0
            bedroom_ac_status = ms.read('bedroom', bedroom_ac)
            ac1 = tk.Label(ws, text="AC")
            ac1.place(x=10, y=10)
            ac_button1 = tk.Button(ws, text=bedroom_ac_status)
            ac_button1.config(command=lambda: ms.mode_convert(ac1, ac_button1, 'bedroom', 'ac'))
            ac_button1.place(x=45, y=8)
            ms.mode_state(ac1, ac_button1, 'bedroom', bedroom_ac, 'ac')

            # Bedroom music
            bedroom_music = 1
            bedroom_music_status = ms.read('bedroom', bedroom_music)
            music1 = tk.Label(ws, text="Music")
            music1.place(x=125, y=10)
            music_button1 = tk.Button(ws, text=bedroom_music_status)
            music_button1.config(command=lambda: ms.mode_convert(music1, music_button1, 'bedroom', 'music'))
            music_button1.place(x=180, y=8)
            ms.mode_state(music1, music_button1, 'bedroom', bedroom_music, 'music')

            # Bedroom light
            bedroom_light = 2
            bedroom_light_status = ms.read('bedroom', bedroom_light)
            bulb1 = tk.Label(ws, text="Light")
            bulb1.place(x=270, y=10)
            bulb_button1 = tk.Button(ws, text=bedroom_light_status)
            bulb_button1.config(command=lambda: ms.mode_convert(bulb1, bulb_button1, 'bedroom', 'light'))
            bulb_button1.place(x=320, y=8)
            ms.mode_state(bulb1, bulb_button1, 'bedroom', bedroom_light, 'light')

            # Bathroom
            bathroom = tk.LabelFrame(wss, text="Bathroom")
            bathroom.pack(expand='yes', fill='both')

            # Bathroom music
            bathroom_music = 1
            bathroom_music_status = ms.read('bathroom', bathroom_music)
            music2 = tk.Label(bathroom, text="Music")
            music2.place(x=125, y=10)
            music_button2 = tk.Button(bathroom, text=bathroom_music_status)
            music_button2.config(command=lambda: ms.mode_convert(music2, music_button2, 'bathroom', 'music'))
            music_button2.place(x=180, y=8)
            ms.mode_state(music2, music_button2, 'bathroom', bathroom_music, 'music')

            # Bathroom light
            bathroom_light = 2
            bathroom_light_status = ms.read('bathroom', bathroom_light)
            bulb2 = tk.Label(bathroom, text="Light")
            bulb2.place(x=270, y=10)
            bulb_button2 = tk.Button(bathroom, text=bathroom_light_status)
            bulb_button2.config(command=lambda: ms.mode_convert(bulb2, bulb_button2, 'bathroom', 'light'))
            bulb_button2.place(x=320, y=8)
            ms.mode_state(bulb2, bulb_button2, 'bathroom', bathroom_light, 'light')

            # Living room
            living_room = tk.LabelFrame(wss, text="Living room")
            living_room.pack(expand='yes', fill='both')

            # Living room ac
            living_room_ac = 0
            living_room_ac_status = ms.read('bathroom', living_room_ac)
            ac3 = tk.Label(living_room, text="AC")
            ac3.place(x=10, y=10)
            ac_button3 = tk.Button(living_room, text=living_room_ac_status)
            ac_button3.config(command=lambda: ms.mode_convert(ac3, ac_button3, 'living_room', 'ac'))
            ac_button3.place(x=45, y=8)
            ms.mode_state(ac3, ac_button3, 'living_room', living_room_ac, 'ac')

            living_room_music = 1
            living_room_music_status = ms.read('bathroom', living_room_music)
            music3 = tk.Label(living_room, text="Music")
            music3.place(x=125, y=10)
            music_button3 = tk.Button(living_room, text=living_room_music_status)
            music_button3.config(command=lambda: ms.mode_convert(music3, music_button3, 'living_room', 'music'))
            music_button3.place(x=180, y=8)
            ms.mode_state(music3, music_button3, 'living_room', living_room_music, 'music')

            living_room_light = 2
            living_room_light_status = ms.read('bathroom', living_room_light)
            bulb3 = tk.Label(living_room, text="Light")
            bulb3.place(x=270, y=10)
            bulb_button3 = tk.Button(living_room, text=living_room_light_status)
            bulb_button3.config(command=lambda: ms.mode_convert(bulb3, bulb_button3, 'living_room', 'light'))
            bulb_button3.place(x=320, y=8)
            ms.mode_state(bulb3, bulb_button3, 'living_room', living_room_light, 'light')

            # Kitchen
            kitchen = tk.LabelFrame(wss, text="Kitchen")
            kitchen.pack(expand='yes', fill='both')

            # Kitchen ac
            kitchen_ac = 0
            kitchen_ac_status = ms.read('kitchen', kitchen_ac)
            ac4 = tk.Label(kitchen, text="AC")
            ac4.place(x=10, y=10)
            ac_button4 = tk.Button(kitchen, text=kitchen_ac_status)
            ac_button4.config(command=lambda: ms.mode_convert(ac4, ac_button4, 'kitchen', 'ac'))
            ac_button4.place(x=45, y=8)
            ms.mode_state(ac4, ac_button4, 'kitchen', kitchen_ac, 'ac')

            # Kitchen music
            kitchen_music = 1
            kitchen_music_status = ms.read('kitchen', kitchen_music)
            music4 = tk.Label(kitchen, text="Music")
            music4.place(x=125, y=10)
            music_button4 = tk.Button(kitchen, text=kitchen_music_status)
            music_button4.config(command=lambda: ms.mode_convert(music4, music_button4, 'kitchen', 'music'))
            music_button4.place(x=180, y=8)
            ms.mode_state(music4, music_button4, 'kitchen', kitchen_music, 'music')

            # Kitchen light
            kitchen_light = 2
            kitchen_light_status = ms.read('kitchen', kitchen_light)
            bulb4 = tk.Label(kitchen, text="Light")
            bulb4.place(x=270, y=10)
            bulb_button4 = tk.Button(kitchen, text=kitchen_light_status)
            bulb_button4.config(command=lambda: ms.mode_convert(bulb4, bulb_button4, 'kitchen', 'light'))
            bulb_button4.place(x=320, y=8)
            ms.mode_state(bulb4, bulb_button4, 'kitchen', kitchen_light, 'light')

            remote_config()

            def disable_parent_tools():
                guest_room_button["state"] = tk.DISABLED
                remote_mode_button["state"] = tk.DISABLED

            def disable_all_button():
                group_automatic()
                disable_parent_tools()

            if number == 1:
                disable_parent_tools()

            elif number == 2:
                if guest_room_text == 'OFF':
                    disable_all_button()

                else:
                    guest_room_button["state"] = tk.DISABLED

            def check_file():
                global old_bedroom_ac_sensor
                global old_bedroom_light_sensor
                global old_bedroom_music_sensor

                global old_bathroom_light_sensor
                global old_bathroom_music_sensor

                global old_living_room_ac_sensor
                global old_living_room_light_sensor
                global old_living_room_music_sensor

                global old_kitchen_ac_sensor
                global old_kitchen_light_sensor
                global old_kitchen_music_sensor

                if remote_mode_button.config('text')[-1] == 'Manual':
                    pass

                else:
                    bedroom_ac_sensor = int(asv.read_sensor('BEDROOM', 'temperature'))
                    bedroom_light_sensor = int(asv.read_sensor('BEDROOM', 'brightness'))
                    bedroom_music_sensor = int(asv.read_sensor('BEDROOM', 'people'))

                    bathroom_light_sensor = int(asv.read_sensor('BATHROOM', 'brightness'))
                    bathroom_music_sensor = int(asv.read_sensor('BATHROOM', 'people'))

                    living_ac_sensor = int(asv.read_sensor('LIVING_ROOM', 'temperature'))
                    living_light_sensor = int(asv.read_sensor('LIVING_ROOM', 'brightness'))
                    living_music_sensor = int(asv.read_sensor('LIVING_ROOM', 'people'))

                    kitchen_ac_sensor = int(asv.read_sensor('KITCHEN', 'temperature'))
                    kitchen_light_sensor = int(asv.read_sensor('KITCHEN', 'brightness'))
                    kitchen_music_sensor = int(asv.read_sensor('KITCHEN', 'people'))

                    # bedroom
                    if hour >= 21 or hour <= 5:
                        ms.mode_off_state(ac1, ac_button1, 'bedroom', 'ac')
                        ms.mode_state(ac1, ac_button1, 'bedroom', bedroom_ac, 'ac')
                        if old_bedroom_ac_sensor != bedroom_ac_sensor:
                            ms.save_log('Bedroom', 'AC', 'OFF')

                    elif bedroom_ac_sensor > 25 and bedroom_music_sensor > 0:
                        ms.mode_on_state(ac1, ac_button1, 'bedroom', 'ac')
                        ms.mode_state(ac1, ac_button1, 'bedroom', bedroom_ac, 'ac')
                        if old_bedroom_ac_sensor != bedroom_ac_sensor:
                            ms.save_log('Bedroom', 'AC', 'ON')

                    elif bedroom_ac_sensor < 50 and bedroom_music_sensor == 0:
                        ms.mode_off_state(ac1, ac_button1, 'bedroom', 'ac')
                        ms.mode_state(ac1, ac_button1, 'bedroom', bedroom_ac, 'ac')
                        if old_bedroom_ac_sensor != bedroom_ac_sensor:
                            ms.save_log('Bedroom', 'AC', 'OFF')

                    else:
                        ms.mode_off_state(ac1, ac_button1, 'bedroom', 'ac')
                        ms.mode_state(ac1, ac_button1, 'bedroom', bedroom_ac, 'ac')
                        if old_bedroom_ac_sensor != bedroom_ac_sensor:
                            ms.save_log('Bedroom', 'AC', 'OFF')

                    if bedroom_light_sensor < 100 and bedroom_music_sensor > 0:
                        ms.mode_on_state(bulb1, bulb_button1, 'bedroom', 'light')
                        ms.mode_state(bulb1, bulb_button1, 'bedroom', bedroom_light, 'light')
                        if old_bedroom_light_sensor != bedroom_light_sensor:
                            ms.save_log('Bedroom', 'light', 'ON')

                    elif bedroom_light_sensor > 50 and bedroom_music_sensor == 0:
                        ms.mode_off_state(bulb1, bulb_button1, 'bedroom', 'light')
                        ms.mode_state(bulb1, bulb_button1, 'bedroom', bedroom_light, 'light')
                        if old_bedroom_light_sensor != bedroom_light_sensor:
                            ms.save_log('Bedroom', 'light', 'OFF')

                    else:
                        ms.mode_off_state(bulb1, bulb_button1, 'bedroom', 'light')
                        ms.mode_state(bulb1, bulb_button1, 'bedroom', bedroom_light, 'light')
                        if old_bedroom_light_sensor != bedroom_light_sensor:
                            ms.save_log('Bedroom', 'light', 'OFF')

                    if 7 <= hour <= 11:
                        ms.mode_on_state(music1, music_button1, 'bedroom', 'music')
                        ms.mode_state(music1, music_button1, 'bedroom', bedroom_music, 'music')
                        if old_bedroom_music_sensor != bedroom_music_sensor:
                            ms.save_log('Bedroom', 'music', 'ON')

                    elif hour >= 21 or hour <= 5:
                        ms.mode_off_state(music1, music_button1, 'bedroom', 'music')
                        ms.mode_state(music1, music_button1, 'bedroom', bedroom_music, 'music')
                        if old_bedroom_music_sensor != bedroom_music_sensor:
                            ms.save_log('Bedroom', 'music', 'OFF')

                    elif bedroom_music_sensor > 0:
                        ms.mode_on_state(music1, music_button1, 'bedroom', 'music')
                        ms.mode_state(music1, music_button1, 'bedroom', bedroom_music, 'music')
                        if old_bedroom_music_sensor != bedroom_music_sensor:
                            ms.save_log('Bedroom', 'music', 'ON')

                    elif bedroom_music_sensor == 0:
                        ms.mode_off_state(music1, music_button1, 'bedroom', 'music')
                        ms.mode_state(music1, music_button1, 'bedroom', bedroom_music, 'music')
                        if old_bedroom_music_sensor != bedroom_music_sensor:
                            ms.save_log('Bedroom', 'music', 'OFF')

                    else:
                        ms.mode_off_state(music1, music_button1, 'bedroom', 'music')
                        ms.mode_state(music1, music_button1, 'bedroom', bedroom_music, 'music')
                        if old_bedroom_music_sensor != bedroom_music_sensor:
                            ms.save_log('Bedroom', 'music', 'OFF')

                    # bathroom
                    if bathroom_light_sensor < 100 and bathroom_music_sensor > 0:
                        ms.mode_on_state(bulb2, bulb_button2, 'bathroom', 'light')
                        ms.mode_state(bulb2, bulb_button2, 'bathroom', bathroom_light, 'light')
                        if old_bathroom_light_sensor != bathroom_light_sensor:
                            ms.save_log('Bathroom', 'light', 'ON')

                    else:
                        ms.mode_off_state(bulb2, bulb_button2, 'bathroom', 'light')
                        ms.mode_state(bulb2, bulb_button2, 'bathroom', bathroom_light, 'light')
                        if old_bathroom_light_sensor != bathroom_light_sensor:
                            ms.save_log('Bathroom', 'light', 'OFF')

                    if 7 <= hour <= 11:
                        ms.mode_on_state(music2, music_button2, 'bathroom', 'music')
                        ms.mode_state(music2, music_button2, 'bathroom', bathroom_music, 'music')
                        if old_bathroom_music_sensor != bathroom_music_sensor:
                            ms.save_log('Bathroom', 'music', 'ON')

                    elif bathroom_music_sensor > 0:
                        ms.mode_on_state(music2, music_button2, 'bathroom', 'music')
                        ms.mode_state(music2, music_button2, 'bathroom', bathroom_music, 'music')
                        if old_bathroom_music_sensor != bathroom_music_sensor:
                            ms.save_log('Bathroom', 'music', 'ON')

                    else:
                        ms.mode_off_state(music2, music_button2, 'bathroom', 'music')
                        ms.mode_state(music2, music_button2, 'bathroom', bathroom_music, 'music')
                        if old_bathroom_music_sensor != bathroom_music_sensor:
                            ms.save_log('Bathroom', 'music', 'OFF')

                    # living_room
                    if living_ac_sensor > 25 and living_music_sensor > 0:
                        ms.mode_on_state(ac3, ac_button3, 'living_room', 'ac')
                        ms.mode_state(ac3, ac_button3, 'living_room', living_room_ac, 'ac')
                        if old_living_room_ac_sensor != living_ac_sensor:
                            ms.save_log('Living room', 'AC', 'ON')

                    else:
                        ms.mode_off_state(ac3, ac_button3, 'living_room', 'ac')
                        ms.mode_state(ac3, ac_button3, 'living_room', living_room_ac, 'ac')
                        if old_living_room_ac_sensor != living_ac_sensor:
                            ms.save_log('Living room', 'AC', 'OFF')

                    if living_light_sensor < 100 and living_music_sensor > 0:
                        ms.mode_on_state(bulb3, bulb_button3, 'living_room', 'light')
                        ms.mode_state(bulb3, bulb_button3, 'living_room', living_room_light, 'light')
                        if old_living_room_light_sensor != living_light_sensor:
                            ms.save_log('Living room', 'light', 'ON')

                    else:
                        ms.mode_off_state(bulb3, bulb_button3, 'living_room', 'light')
                        ms.mode_state(bulb3, bulb_button3, 'living_room', living_room_light, 'light')
                        if old_living_room_light_sensor != living_light_sensor:
                            ms.save_log('Living room', 'light', 'OFF')

                    if 7 <= hour <= 11:
                        ms.mode_on_state(music3, music_button3, 'living_room', 'music')
                        ms.mode_state(music3, music_button3, 'living_room', living_room_music, 'music')
                        if old_living_room_music_sensor != living_music_sensor:
                            ms.save_log('Living room', 'music', 'ON')

                    elif living_music_sensor > 0:
                        ms.mode_on_state(music3, music_button3, 'living_room', 'music')
                        ms.mode_state(music3, music_button3, 'living_room', living_room_music, 'music')
                        if old_living_room_music_sensor != living_music_sensor:
                            ms.save_log('Living room', 'music', 'ON')

                    else:
                        ms.mode_off_state(music3, music_button3, 'living_room', 'music')
                        ms.mode_state(music3, music_button3, 'living_room', living_room_music, 'music')
                        if old_living_room_music_sensor != living_music_sensor:
                            ms.save_log('Living room', 'music', 'oOFF')

                    # kitchen
                    if kitchen_ac_sensor > 25 and kitchen_music_sensor > 0:
                        ms.mode_on_state(ac4, ac_button4, 'kitchen', 'ac')
                        ms.mode_state(ac4, ac_button4, 'kitchen', kitchen_ac, 'ac')
                        if old_kitchen_ac_sensor != kitchen_ac_sensor:
                            ms.save_log('Living room', 'AC', 'ON')

                    else:
                        ms.mode_off_state(ac4, ac_button4, 'kitchen', 'ac')
                        ms.mode_state(ac4, ac_button4, 'kitchen', kitchen_ac, 'ac')
                        if old_kitchen_ac_sensor != kitchen_ac_sensor:
                            ms.save_log('Living room', 'AC', 'OFF')

                    if kitchen_light_sensor < 100 and kitchen_music_sensor > 0:
                        ms.mode_on_state(bulb4, bulb_button4, 'kitchen', 'light')
                        ms.mode_state(bulb4, bulb_button4, 'kitchen', kitchen_light, 'light')
                        if old_kitchen_light_sensor != kitchen_light_sensor:
                            ms.save_log('Living room', 'light', 'ON')

                    else:
                        ms.mode_off_state(bulb4, bulb_button4, 'kitchen', 'light')
                        ms.mode_state(bulb4, bulb_button4, 'kitchen', kitchen_light, 'light')
                        if old_kitchen_light_sensor != kitchen_light_sensor:
                            ms.save_log('Living room', 'light', 'OFF')

                    if 7 <= hour <= 11:
                        ms.mode_on_state(music4, music_button4, 'kitchen', 'music')
                        ms.mode_state(music4, music_button4, 'kitchen', kitchen_music, 'music')
                        if old_kitchen_music_sensor != kitchen_music_sensor:
                            ms.save_log('Living room', 'music', 'ON')

                    elif kitchen_music_sensor > 0:
                        ms.mode_on_state(music4, music_button4, 'kitchen', 'music')
                        ms.mode_state(music4, music_button4, 'kitchen', kitchen_music, 'music')
                        if old_kitchen_music_sensor != kitchen_music_sensor:
                            ms.save_log('Living room', 'music', 'ON')

                    else:
                        ms.mode_off_state(music4, music_button4, 'kitchen', 'music')
                        ms.mode_state(music4, music_button4, 'kitchen', kitchen_music, 'music')
                        if old_kitchen_music_sensor != kitchen_music_sensor:
                            ms.save_log('Living room', 'music', 'OFF')

                    old_bedroom_ac_sensor = bedroom_ac_sensor
                    old_bedroom_light_sensor = bedroom_light_sensor
                    old_bedroom_music_sensor = bedroom_music_sensor

                    old_bathroom_light_sensor = bathroom_light_sensor
                    old_bathroom_music_sensor = bathroom_music_sensor

                    old_living_room_ac_sensor = living_ac_sensor
                    old_living_room_light_sensor = living_light_sensor
                    old_living_room_music_sensor = living_music_sensor

                    old_kitchen_ac_sensor = kitchen_ac_sensor
                    old_kitchen_light_sensor = kitchen_light_sensor
                    old_kitchen_music_sensor = kitchen_music_sensor

                    wss.after(1000, check_file)

            wss.mainloop()

        in_thread_1 = threading.Thread(target=in_run_1, args=())
        in_thread_1.start()

    my_thread_2 = threading.Thread(target=run, args=())
    my_thread_2.start()

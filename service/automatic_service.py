from time import strftime
import time
import configparser
import threading

lock = threading.Lock()
file = r'sensor.ini'

# Note: Auto mode
# 22 - 6, no music and lights at bedroom
# 8 - 11, music


def read_time_real():
    real_hour = int(strftime('%H'))
    return real_hour


def read_sensor(location, sensor):
    hardware = configparser.ConfigParser()
    hardware.read(file)
    result = hardware.get(location, sensor)
    return result


def update_sensor(location, sensor, from_time, to_time, value_up, value_down, hour):
    hardware = configparser.ConfigParser()
    hardware.read(file)

    if from_time <= hour <= to_time:
        hardware.set(location, sensor, value_up)
    else:
        hardware.set(location, sensor, value_down)

    with open(file, 'w') as configfile:
        hardware.write(configfile)



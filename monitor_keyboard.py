import datetime
import time

from pynput import keyboard

last_one = ''
def on_press(key):
    global last_one
    try:
        str = 'press:{}'.format(key)
        if last_one != str:
            print('press: {} - {}'.format(time.perf_counter(), key))
            last_one = str
    except AttributeError:
        print('press: {} - {}'.format(time.perf_counter(), key))
        last_one = str

def on_release(key):
    str = 'release:{}'.format(key)
    global last_one
    if last_one != str:
        print('release: {} - {}'.format(time.perf_counter(), key))
        last_one = str

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
import time

from pynput.keyboard import Key, Controller

def run():
    with open('records.txt', 'r') as fd:
        before_t = 0.0
        for line in fd.readlines():
            arr = line.strip().split(' ')

            key_type = arr[0]
            t = float(arr[1])
            key_char = arr[-1].replace("'", "")

            if before_t == 0.0:
                before_t = t

            diff_t = t - before_t
            before_t = t
            print(key_type, diff_t, key_char)

            time.sleep(diff_t)
            if key_type == 'press:':
                if key_char == 'Key.space':
                    keyboard.press(Key.space)
                else:
                    keyboard.press(key_char)
            else:
                if key_char == 'Key.space':
                    keyboard.release(Key.space)
                else:
                    keyboard.release(key_char)



if __name__ == '__main__':
    keyboard = Controller()

    while True:
        time.sleep(10)
        print('begin')
        run()



from PIL import ImageGrab
import keyboard

import datetime, time, random

import asyncio, threading, multiprocessing

# while True:

#     try:
#         if keyboard.is_pressed('h'):
#             image = ImageGrab.grab()
#             image.save('screens/{0}.png'.format(datetime.datetime.now().strftime('%H-%M-%S')))
#         else:
#             pass
#     except:
#         print('nope')
#         input()

#     pass

if __name__ == '__main__':

    now = datetime.datetime.now()
    time_limit = now + datetime.timedelta(seconds=30)
    # time_limit = now + datetime.timedelta(minutes=25)

    print('Enter the additional name:')
    name = ''
    name = input()

    print('All threads are queued.')
    print('Process will be closed at {0} + 1 sec.'.format(time_limit))

    while datetime.datetime.now() < time_limit:

        time.sleep(0.5)

        if keyboard.is_pressed('q') or keyboard.is_pressed('i') or keyboard.is_pressed('o'):
            image = ImageGrab.grab()
            filename = 'screens/pressed/{0}={1}.png'.format(name, datetime.datetime.now().strftime('%H-%M-%S'))
            image.save(filename)
            print('_PRESSED_ : {0}'.format(filename))
        else:
            pass

        tmp = random.randrange(0,2000)
        if tmp < 250:
            image = ImageGrab.grab()
            filename = 'screens/randomly/{0}={1}.png'.format(name, datetime.datetime.now().strftime('%H-%M-%S'))
            image.save(filename)
            print('_LUCKYBOY_ : {0}'.format(filename))
        else:
            pass

        time.sleep(0.5)

        pass

    pass
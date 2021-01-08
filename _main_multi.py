
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

def random_part(time_limit, name):

    print('Random part is activated')

    while datetime.datetime.now() < time_limit:
        tmp = random.randrange(0,2000)
        if tmp < 250:
            image = ImageGrab.grab()
            filename = 'screens/randomly/{0}={1}.png'.format(name, datetime.datetime.now().strftime('%H-%M-%S'))
            image.save(filename)
            print('_LUCKYBOY_ : {0}'.format(filename))
        else:
            pass
        time.sleep(1)

    pass

def press_part(name):

    print('Press part is activated')
    ind = 0

    while True:
        if keyboard.is_pressed('q') or keyboard.is_pressed('i') or keyboard.is_pressed('o'):
            image = ImageGrab.grab()
            filename = 'screens/pressed/{0}={1}.png'.format(name, datetime.datetime.now().strftime('%H-%M-%S'))
            image.save(filename)
            print('_PRESSED_ : {0}'.format(filename))
        else:
            pass

        ind = ind + 1

        if ind == 3000:
            ind = 0
            time.sleep(1)
            pass
        pass

    pass

if __name__ == '__main__':

    now = datetime.datetime.now()
    time_limit = now + datetime.timedelta(seconds=30)
    # time_limit = now + datetime.timedelta(minutes=25)

    print('Enter the additional name:')
    name = ''
    name = input()

    t_press = multiprocessing.Process(target=press_part, args=(name,))
    t_press.daemon = True
    t_press.start()

    t_rand = multiprocessing.Process(target=random_part, args=(time_limit,name,))
    t_rand.start()

    print('All threads are queued.')
    print('Process will be closed at {0} + 1 sec.'.format(time_limit))

    while True:
        if not t_rand.is_alive():
            t_press.terminate()
            t_press.join()
            t_press.close()
            t_rand.close()
            print('All processes are closed')
            break
            pass
        time.sleep(1)
        pass

    pass

from PIL import ImageGrab
import keyboard

import datetime
import time
import random

import asyncio
import threading
import multiprocessing

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

    last_time = datetime.datetime.now() + datetime.timedelta(seconds=2)

    while datetime.datetime.now() < time_limit:
        tmp = random.randrange(0, 2000)
        # tmp = random.randrange(0,250)
        if tmp < 250:

            if last_time + datetime.timedelta(seconds=1) > datetime.datetime.now():
                print('_LUCKYBOY_ : Skipped once because of time')
                continue
                pass

            image = ImageGrab.grab()
            last_time = datetime.datetime.now()
            filename = 'screens/randomly/{0}={1}.png'.format(
                name, datetime.datetime.now().strftime('%H-%M-%S'))
            image.save(filename)
            print('_LUCKYBOY_ : {0}'.format(filename))
        else:
            pass
        time.sleep(1)

    pass


def press_part(name):

    print('Press part is activated')
    ind = 0

    last_time = datetime.datetime.now()

    while True:
        if keyboard.is_pressed('q') or keyboard.is_pressed('i') or keyboard.is_pressed('o'):

            if last_time + datetime.timedelta(seconds=1) > datetime.datetime.now():
                print('_PRESSED_ : Skipped once because of time')
                continue
                pass

            image = ImageGrab.grab()
            last_time = datetime.datetime.now()
            filename = 'screens/pressed/{0}={1}.png'.format(
                name, datetime.datetime.now().strftime('%H-%M-%S'))
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


def period_part(name, period):

    print('Period part is activated')

    while True:

        time.sleep(period)

        image = ImageGrab.grab()
        filename = 'screens/period/{0}={1}.png'.format(
            name, datetime.datetime.now().strftime('%H-%M-%S'))
        image.save(filename)
        print('_PERIOD_ : {0}'.format(filename))

        pass

    pass


if __name__ == '__main__':

    now = datetime.datetime.now()
    time_limit = now + datetime.timedelta(seconds=30)
    # time_limit = now + datetime.timedelta(minutes=25)

    print('Enter the additional name:')
    name = ''
    name = input()

    print('Enter the period:')
    period = input()
    if period == '':
        period = 15

    t_rand = multiprocessing.Process(
        target=random_part, args=(time_limit, name,))
    t_rand.start()

    t_press = multiprocessing.Process(target=press_part, args=(name,))
    t_press.daemon = True
    t_press.start()

    t_period = multiprocessing.Process(
        target=period_part, args=(name, period,))
    t_period.daemon = True
    t_period.start()

    print('All threads are queued.')
    print('Process will be closed at {0} + 1 sec.'.format(time_limit))

    while True:
        if not t_rand.is_alive():

            t_press.terminate()
            t_press.join()
            t_press.close()

            t_period.terminate()
            t_period.join()
            t_period.close()

            t_rand.close()

            print('All processes are closed')
            break
            pass
        time.sleep(1)
        pass

    pass



from PIL import ImageGrab
import keyboard

import datetime
import time
import random
import os

import asyncio
import threading
import multiprocessing

# own imports
from counter import Counter
import recognizing as recog

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

    # count_token = Counter.get_new_token('screens/randomly')

    total, scale = folderSize('screens/randomly')
    #total = size_[0]
    #scale = size_[1]

    print('\nRandom part is activated\nSize is {0} {1}\n'.format(
        round(total, 2), scale))

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
                name, datetime.datetime.now().strftime('%m%d%Y,%H-%M-%S'))
            image.save(filename)
            print('_LUCKYBOY_ : {0}'.format(filename))
            # Counter.inc(count_token, filename)
        else:
            pass
        time.sleep(1)

    pass


def press_part(name):

    # count_token = Counter.get_new_token('screens/pressed')

    total, scale = folderSize('screens/pressed')
    #total = size_[0]
    #scale = size_[1]

    print('\nPress part is activated\nSize is {0} {1}\n'.format(
        round(total, 2), scale))
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
                name, datetime.datetime.now().strftime('%m%d%Y,%H-%M-%S'))
            image.save(filename)
            print('_PRESSED_ : {0}'.format(filename))
            # Counter.inc(count_token, filename)
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

    # count_token = Counter.get_new_token('screens/pressed')

    total, scale = folderSize('screens/period')
    #total = size_[0]
    #scale = size_[1]

    print('\nPeriod part is activated\nSize is {0} {1}\n'.format(
        round(total, 2), scale))
    while True:

        time.sleep(period)

        image = ImageGrab.grab()
        filename = 'screens/period/{0}={1}.png'.format(
            name, datetime.datetime.now().strftime('%m%d%Y,%H-%M-%S'))
        image.save(filename)
        print('_PERIOD_ : {0}'.format(filename))
        # Counter.inc(count_token, filename)

        pass

    pass


def delete_equals_pics(name, period=5):

    print('\nDelete part is activated\nPeriod is {0}'.format(period))
    print('Pathes for searching:\n')
    # for index, (i, j) in zip(range(0, len(Counter.values)), Counter.values):
    #     print('#{0} = {1}'.format(index, i))
    #     continue
    print('{0}'.format('='*20))

    while (True):

        time.sleep(period)

        # flag = [0] * (len(Counter.values))
        # indexer = 0
        for key, value in Counter.values:
            # key == token
            # value == array of filenames
            if (value > 0):
                Counter.pause_counting(key)
                recog.main1(key)
                Counter.clear(key)
                Counter.resume_counting(key)
                pass
            # indexer += 1
            continue

        # indexer = 0
        # for i in flag:
        #     if (i != 0):
        #         recog.main1(Counter.values)
        #         pass
        #     elif (i == 0):
        #         pass
        #     indexer += 1
        #     continue

        continue

    pass


def folderSize(dirPath):

    total = 0
    scale = 'bytes'

    for dirpath, dirnames, filenames in os.walk(dirPath):
        for f in filenames:
            # print(dirpath)
            fp = os.path.join(dirpath, f)
            # skip if it is symbolic link
            if not os.path.islink(fp):
                total += os.path.getsize(fp)

    # KiloBytes
    if total > 1024:
        total = total / 1024
        scale = 'Kb'
        pass

    # MegaBytes
    if total > 1024:
        total = total / 1024
        scale = 'Mb'
        pass

    # GigaBytes
    if total > 1024:
        total = total / 1024
        scale = 'Gb'
        pass

    return [total, scale]
    pass

def asking():

    last_name = ''
    with open('storage/saves.txt', 'r', encoding='utf-8') as file:
        file.seek(0)
        last_name = file.readline()
        file.close()
        pass
    print('last_name == {0}'.format(last_name))

    print('Enter the additional name:')
    name = input()
    if name.strip() != '':
        with open('storage/saves.txt', 'w', encoding='utf-8') as file:
            file.truncate()
            file.seek(0)
            file.write(name.lower())
            file.close()
            pass
        pass
    else:
        name = last_name

    print('Name == {0}'.format(name))

    print('Enter the period:')
    period = input()
    if period == '':
        period = 15

    print('Enter minutes:')
    mins = input()
    if mins == '':
        mins = 30
    now = datetime.datetime.now()
    # time_limit = now + datetime.timedelta(seconds=30)
    time_limit = now + datetime.timedelta(minutes=mins)

    return [name, period, mins, time_limit]

    pass

def skip_asking():

    name = 'testing'
    period = 3
    mins = 0
    now = datetime.datetime.now()
    time_limit = now + datetime.timedelta(seconds=30)

    return [name, period, mins, time_limit]


if __name__ == '__main__':

    print('Start')

    # name, period, mins, time_limit = asking()
    name, period, mins, time_limit = skip_asking()

    print('Name is {0} \t Period is {1} \t Minutes is {2}'.format(
        name, period, mins))

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

    print('================STATUS================')

    size_ = folderSize('screens/period')
    total = size_[0]
    scale = size_[1]
    print('\nPERIOD size is {0} {1}\n'.format(round(total, 2), scale))

    size_ = folderSize('screens/pressed')
    total = size_[0]
    scale = size_[1]
    print('\nPRESSED size is {0} {1}\n'.format(round(total, 2), scale))

    size_ = folderSize('screens/randomly')
    total = size_[0]
    scale = size_[1]
    print('\nRANDOMLY size is {0} {1}\n'.format(round(total, 2), scale))

    pass

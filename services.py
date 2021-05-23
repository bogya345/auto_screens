
import os, json, random

# own import
from myLogging import logMsgs

count_deleted = 0

def delete_repeated_pics(output, files):

    global count_deleted
    
    for i1, i2 in zip(output, files):
        if (i1 == 1):
            os.remove(i2)
            print('DELETED: {0}'.format(i2))
            logMsgs('1','DELETED: {0}'.format(i2))
            count_deleted += 1
            continue
        continue

    print('Deleted {0} images'.format(count_deleted))
    logMsgs('1','##Deleted {0} images##'.format(count_deleted))

    pass
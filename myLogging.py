
import os, json, random

def getToken():
    return random.randint(0,100)
    pass

def logMsgs(token, msg, path='storage/logs'): # D:/Profile/_source/vscode_repos/screensshots/storage/logs

    with open(path+'/{0}.txt'.format(token), 'a+') as file:
        file.write('{0}\n'.format(msg))
        pass

    pass

def log_check_many_pics_valsChecking(arg1, arg2, result, token, path='storage/logs'): # D:/Profile/_source/vscode_repos/screensshots/storage/logs

    # if(os.path.isfile('filename.txt')):
    #     os.
    #     pass

    with open(path+'/{0}.txt'.format(token), 'a+') as file:
        file.write('{0}\r\n{1}\r\nResult:\t{2}\r\n'.format(arg1, arg2, result))
        pass

    pass

import os, json, random

from PIL import Image, ImageEnhance

def getListOfFiles(dirName):
    # create a list of file and sub directories
    # names in the given directory
    listOfFile = os.listdir(dirName)
    allFiles = list()
    # Iterate over all the entries
    for entry in listOfFile:
        # Create full path
        fullPath = os.path.join(dirName, entry)
        # If entry is a directory then get the list of files in this directory
        if os.path.isdir(fullPath):
            allFiles = allFiles + getListOfFiles(fullPath)
        else:
            allFiles.append(fullPath)

    return allFiles

def getPixels(block):
    pix_val = list(block.getdata())
    pix_val_flat = [x for sets in pix_val for x in sets]

    return pix_val

def convertRGBtoInt(rgb=[-1, -1, -1], r=-1, g=-1, b=-1):
    if (rgb[0] != -1):
        return rgb[0] + rgb[1]*256 + rgb[2]*256*256
    elif (r != -1 and g != -1 and b != -1):
        return r + g*256 + b*256*256
    else:
        Exception('Well, you know what exactly you did wrong')

def changeSize(img, wsize=640, hsize=360):
    img = img.resize((wsize, hsize), Image.ANTIALIAS)
    return img

def cropPic(img, left=0, top=64, right=64, bottom=128):
    cropImg = img.crop((left, top, right, bottom))
    return cropImg
    pass

def main1(path='./storage/training/True(14).png'):
    img = Image.open(path)
    img = changeSize(img)

    accom = []

    orig_vals_rgb = []
    orig_vals_int = []

    top_ = 64
    while (top_ != 256):
        left_ = 0

        while(left_ != 640):

            crImg = cropPic(img, left_, top_, left_+64, top_+64)
            accom.append(crImg)

            tmp_ = getPixels(crImg)
            for i in tmp_:
                orig_vals_rgb.append(i)
                orig_vals_int.append(convertRGBtoInt(rgb=i))

            left_ += 64
            continue

        top_ += 64
        continue
    # print(len(accom))
    
    return orig_vals_int
    pass

def get_pics_data(dirPath):

    dirPath = 'D:/Profile/_source/vscode_repos/screensshots/' + dirPath

    print('Checking in {0} path:'.format(dirPath))
    files = getListOfFiles(dirPath)
    print(files)
    size = len(files)
    output = []
    inner_out = []

    rand_minus = random.randint(5, 1000)

    for i in files:

        tmp_ = main1(i)

        # needed to check on empty(big black frames)

        tmp_radixs = len(tmp_) - 1 - (rand_minus)
        tmp_size_str = str(tmp_radixs)
        first_digit = int(tmp_size_str[0])
        how_multiply = len(tmp_size_str) - 1

        num = first_digit * (pow(10, int(how_multiply)))

        # s = len(tmp_)
        # ss = str(s)
        # sss = len
                 
        # l = int(sss)
        # num = l * sss

        tmp = []
        for z in range(0,num):
            tmp.append(tmp_[z])
            continue

        phrase = ''
        for index, j in zip(range(0,num,1), tmp):
            phrase += str(j)
            if ( (index != 0) and (index % 100 == 0) ):
                inner_out.append(phrase)
                phrase = ''
                continue
            continue
        
        output.append(inner_out)
        inner_out = []
        continue    

    return [output, files]
    pass
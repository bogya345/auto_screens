
import random

from PIL import Image

# own import

# source - основная
def check_two_pics(source, pics_data):
    # size = len(pics_data)
    size = 2
    output = [-1] * (size)

    output_i = 0
    for i in range(0, size, 2):
        i1 = i
        i2 = i + 1

        continue

    return output
    pass

# pics_data - данные изображений, 0 будет в качестве первого исходника
def check_many_pics(pics_data):

    source = pics_data[0]
    
    size = len(pics_data)
    output = [-1] * (size)
    output[0] = 0

    output_i = 0
    for i in range(1, size, 1):
    
        for j_s, j in zip(range(0,len(source),1), range(0,len(pics_data[i]),1)):
            j_s_val = source[j_s]
            j_val = pics_data[i][j]
            if (j_s_val != j_val):
                output[i] = 0
                break

            ## for checking string one char by one
            # for k_s, k in zip(source[j_s], pics_data[i][j]):
            #     # k_s = rgb values as integer as string in source pic_data
            #     # k = rgb values as integer as string
            #     if (k_s != k):
            #         output[i] = 0
            #         break
            #     continue
            # if (output[i] == 0):
            #     # means that output[i] already different
            #     source = pics_data[i]
            #     break
            # # elif (output[i] == -1):
            # #     # means that source and pics_data[i] are equal
            # #     continue
            ##

            continue
        
        if (output[i] == -1):
            # means that source and pics_data[i] are still equals
            output[i] = 1
            continue
        elif (output[i] == 0):
            source = pics_data[i]
            continue

        continue

    return output
    pass
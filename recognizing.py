
import os, random, json

# own import
import load_pics as lp
import checking_pics as cp
import services as servs

def main1(path):

    output1, files = lp.get_pics_data(path)

    output2 = cp.check_many_pics(output1)

    servs.delete_repeated_pics(output2, files)

    pass
from BaseModel import *

__author__ = 'andrew'

def debug(str):
    if database.MB_DEBUG == True:
        print str

def get(wc,custom_values):
    print "Called get"
    return BaseModel(wc,custom_values,"nothing")
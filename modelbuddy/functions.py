import database

__author__ = 'andrew'

def debug(str):
    if database.MB_DEBUG == True:
        print str
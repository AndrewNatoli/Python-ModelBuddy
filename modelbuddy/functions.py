from BaseModel import *

__author__ = 'andrew'

def debug(str):
    if database.MB_DEBUG == True:
        print "== ModelBuddy == " + str

def get(table,wc="",custom_values=""):
    # Load a blank model for the table
    if custom_values == "" and wc == "":
        return BaseModel(table)
    # Try to load a record
    else:
        return BaseModel(table,wc,custom_values)
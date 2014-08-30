import database
from functions import *

__author__ = 'andrew'

class BaseModel() :
    mb_tableName        = ""
    mb_wc               = ""
    mb_custom_values    = ""
    mb_tableStructure   = {}
    mb_primaryKey       = ""

    def __init__(self,wc,custom_values):
        debug("Initializing ModelBuddy Model")
        self.wc = wc
        self.custom_values = custom_values



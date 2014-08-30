#If using a different db engine, change this import!
import database_mysql as database

import functions


__author__ = 'andrew'

class BaseModel():
    mb_tableName = ""  # Tuple (table structure, primary key
    mb_wc = ""
    mb_custom_values = ""
    mb_tableStructure = {}
    mb_primaryKey  = ""
    mb_recordData = {}

    # Find a record in the database based on a where clause
    def __init__(self, tableName, wc="", custom_values=""):
        functions.debug("Initializing ModelBuddy Model for " + tableName + " table.")
        self.mb_tableName = tableName
        self.mb_wc = wc
        self.mb_custom_values = custom_values


        #Get Table Structure
        self.mb_tableStructure = database.getTableStructure(self.mb_tableName)

        #If there's no WC, exit
        if wc == "" and type(wc) != dict:
            functions.debug("Loaded blank model")
            self.mb_recordData = database.assign_defaults(self.mb_tableStructure)
            print self.mb_recordData
            return

        #Generate our select query
        selectQuery = database.generate_selectQuery(self.mb_tableName,self.mb_wc,self.mb_custom_values)

        functions.debug("Fetching record")
        result = database.select(selectQuery[0],selectQuery[1])

        print result

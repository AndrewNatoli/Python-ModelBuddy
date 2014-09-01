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
        functions.debug("Got record.")

    #Change values in the model (but does not write them to the database)
    def set(self,values):
        for key in values:
            try:
                self.mb_recordData[key]
                self.mb_recordData[key] = values[key]
                functions.debug("Updated key " + str(key) + " with value " + str(values[key]))
            except KeyError:
                functions.debug("Uh oh! Key: " + str(key) + " does not exist in the record!")
        functions.debug("Record data set. Use save() or commit() to write to database")

    def commit(self):
        updateQuery = database.generate_updateQuery(self.mb_tableName,self.mb_recordData,self.mb_wc,self.mb_custom_values)
        #result = database.update(updateQuery[0],updateQuery[1])
        functions.debug(updateQuery[0])
        functions.debug(str(updateQuery[1]))

    def update(self):
        self.commit()

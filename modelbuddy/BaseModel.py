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
    mb_autoIncrement = False # Whether or not the primary key is an auto_increment field
    mb_recordData = {}

    # Find a record in the database based on a where clause
    def __init__(self, tableName, wc="", custom_values=""):
        functions.debug("Initializing ModelBuddy Model for " + tableName + " table.")
        self.mb_tableName = tableName
        self.mb_wc = wc
        self.mb_custom_values = custom_values


        #Get Table Structure
        self.mb_tableStructure = database.getTableStructure(self.mb_tableName)
        # TODO: Find primary key and determine if it's an auto-increment field. set mb_primaryKey and mb_autoIncrement

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
        self.mb_recordData = result
        functions.debug("Got record.")

    #Change values in the model (but does not write them to the database)
    def set(self,values):
        for key in values:
            try:
                # TODO: Don't allow modifying of an auto-increment primary key.
                # check if it's not a duplicate entry... but at the start it should be read only.
                self.mb_recordData[key]
                self.mb_recordData[key] = values[key]
                functions.debug("Updated key " + str(key) + " with value " + str(values[key]))
            except KeyError:
                functions.debug("Uh oh! Key: " + str(key) + " does not exist in the record!")
        functions.debug("Record data set. Use save() or commit() to write to database")

    def commit(self):
        # TODO: Deprecated. Remove in the future.
        self.update()

    def update(self):
        # TODO: Determine if the record already exists by checking if the primary key value is set.
        updateQuery = database.generate_updateQuery(self.mb_tableName,self.mb_recordData,self.mb_wc,self.mb_custom_values)
        #result = database.update(updateQuery[0],updateQuery[1])
        functions.debug(updateQuery[0])
        functions.debug(str(updateQuery[1]))
        database.update(updateQuery[0],updateQuery[1])

    def insert(self):
        # TODO: I'm okay with using this to duplicate a record but we have to unset or change the primary key first...
        insertQuery = database.generate_insertQuery(self.mb_tableName,self.mb_recordData)
        functions.debug(str(insertQuery[0]))
        functions.debug(str(insertQuery[1]))
        database.insert(insertQuery[0],insertQuery[1])

import database
import functions

__author__ = 'andrew'

class BaseModel() :
    mb_tableName        = ""
    mb_wc               = ""
    mb_custom_values    = ""
    mb_tableStructure   = {}
    mb_primaryKey       = ""

    def __init__(self, tableName, wc, custom_values):
        functions.debug("Initializing ModelBuddy Model for " + tableName + " table.")
        self.mb_tableName = tableName
        self.mb_wc = wc
        self.mb_custom_values = custom_values

        #Build our query...
        query = "SELECT * FROM " + tableName + " WHERE "
        for key in wc.keys():
            query = query + key + '="' + wc[key] + '" AND '

        # Trim off the last "AND"
        query = query[:-4]

        #Run the query and see what happens...
        database.cur.execute(query)

        #Now get the table structure...
        # self.mb_tableStructure = database.getTablestructure(table)




import MySQLdb
import functions
import time
import datetime

__author__ = 'andrew'

DB_HOST = "127.0.0.1"
DB_PORT = "8889"
DB_USER = "root"
DB_PASS = "root"
DB_NAME = "modelBuddy"
MB_DEBUG = True

try:
    db = MySQLdb.connect(host=str(DB_HOST), port=int(DB_PORT), user=str(DB_USER), passwd=str(DB_PASS), db=str(DB_NAME))
    cur = db.cursor()
    if MB_DEBUG == True:
        print "== database_mysql == Connected to database"
except Exception, e:
    exit("== database_mysql == Could not connected to database.\n" + str(e))

"""
    Find the table structure for (tableName) and return a tuple
    containing the table structure and primary key if there is one.
"""


def getTableStructure(tableName):
    functions.debug("Getting table structure for " + tableName)

    # This will contain the table structure in a tuple
    tableStructure = ""
    #This will hold the primay key if there is one
    primaryKey = ""

    #Do work
    try:
        tableStructure = cur.execute("DESCRIBE " + tableName)
        tableStructure = cur.fetchall()

        # Find the primary key if it exists
        for i in tableStructure:
            if i[3] == "PRI":
                primaryKey = i[0]
                functions.debug(primaryKey + " is the primary key.")
                break
    # Something went wrong...
    except Exception:
        functions.debug("Could not get table structure for " + tableName)

    return tableStructure, primaryKey

"""
    Returns a tuple, (query, values)
    query: "UPDATE table SET.... WHERE...."
"""
def generate_updateQuery(tableName,newValues,wc,custom_values=""):
    functions.debug("Generating an update query...")
    #Build our update query TODO: Build insert
    query = "UPDATE " + tableName + " SET "
    values = []
    for key in newValues.keys():
        query = str(query) + str(key) + " = %s, " #Key goes in the query
        values.append(newValues[key]) #Value goes in separate list

    # Trim the last comma and then add the where-clause
    query = query[:-2] + " WHERE "

    if type(wc) == dict:
        functions.debug("Given dictionary WC -- " + str(wc))
        # Add our keys to the statement and then we'll put the values in a tuple
        for key in wc.keys():
            query = str(query) + str(key) + '= %s AND '
            values.append(wc[key])

    elif type(wc) == str:
        functions.debug("Given String WC -- " + str(wc))
        query = str(query) + str(wc)
        functions.debug("custom_values: " + str(custom_values))
        for value in custom_values:
            values.append(value)

    # Trim off the last AND
    query = query[:-4]

    return (query,values)

"""
    Returns a tuple, (query,values)
    query: "SELECT * FROM table WHERE this=%s
    values: Tuple with the values for each key
"""


def generate_selectQuery(tableName,wc,custom_values=""):
    #Build our query...
    query = "SELECT * FROM " + tableName + " WHERE "
    values = []

    if type(wc) == dict:
        functions.debug("Given dictionary WC")
        # Add our keys to the statement and then we'll put the values in a tuple
        for key in wc.keys():
            query = query + key + '= %s AND '
            values.append(wc[key])

        # Trim off the last "AND" then limit us to one record
        query = query[:-4] + " LIMIT 1"
    elif type(wc) == str:
        functions.debug("Given String WC")
        query = query + wc
        values = custom_values

    return query, values

"""
    Execute a SELECT statement
    Requires a string, Query and a tuple of keys
"""

def select(query,values):
    # Make sure values is a tuple
    if type(values) != tuple:
        values = tuple(values)      # Create a tuple

     #Run the query and see what happens...
    try:
        cur.execute(query, values)

        result = {}
        columns = tuple([d[0].decode('utf8') for d in cur.description])

        for row in cur:
            field = zip(columns, row)
            print type(field)
            for column in field:
                result[column[0]] = str(column[1])




        print str(result)

    except Exception, e:
        functions.debug("Error getting record")
        exit("ModelBuddy Database Driver Error: " + str(e) + "\n modelbuddy.database.select("+ str(query) + ", " + str(values)+")")

    return result

"""
    Execute an UPDATE statement
    Requires a string (query) and a tuple of values that make up what to change and the where clause
"""
def update(query, values):
    # Make sure the values are in a tuple
    if type(values) != list:
        values = list(values)

    #Run the query and see what happens...
    try:
        cur.executemany(query,[values])
        db.commit()
        functions.debug("Updated.")
    except Exception, e:
        functions.debug("Error updating record.");
        exit("ModelBuddy Database Driver Error: " + str(e) + "\n modelbuddy.database.upate("+ str(query) + ", " + str(values)+")")

"""
    Create a blank record using default values from the tableStructure and return it back to BaseModel
"""

def assign_defaults(tableStructure):
    record = {}
    for row in tableStructure[0]:
        if str(row[4]) == "None":
            defaultValue = ""
        else:
            defaultValue = str(row[4])
        record[str(row[0])] = defaultValue

    return record
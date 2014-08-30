import MySQLdb
__author__ = 'andrew'

DB_HOST = "127.0.0.1"
DB_PORT = "8889"
DB_USER = "root"
DB_PASS = "root"
DB_NAME = "modelBuddy"
MB_DEBUG = True

db = MySQLdb.connect(host=str(DB_HOST), port=int(DB_PORT), user=str(DB_USER), passwd=str(DB_PASS), db=str(DB_NAME))

cur = db.cursor()

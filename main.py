from db_connect import DB_Connect
from tkGUI_Main_window import GUI

# Establish SQLite3 DB connection
db = DB_Connect()
# instantiate the window with connection to database
gui = GUI(db)

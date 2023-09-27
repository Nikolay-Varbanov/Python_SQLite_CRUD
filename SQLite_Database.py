# Build-in
import sqlite3

# User Defined
from SQLite_Selector_List import SQLite_Selector_List

class SQLite_Database:
#Utilities
#Constructs
	def __init__(self):
		print("Constructing a SQLite_Database class")
		self.selector_list: SQLite_Selector_List
		self.isConnected = False
		self.database_connection: sqlite3
	def __del__(self):
		print("Destructuing a SQLite_Database class")
		self.OnCleanup()
#Facilities
	def OnInit(self):
		print("In SQLite_Database.OnInit()")
		self.selector_list = SQLite_Selector_List()
		self.selector_list.OnInit()
	def OnCleanup(self):
		print("Cleaningup a SQLite_Database class")
		if self.isConnected:
			print('Closing a Database Connection')
			self.database_connection.close()
	def OnConnect(self, database_path: str):
		database_path = 'data_bases\\' + database_path + '.db'
		print(database_path)
		# !!! Here must see if connection is active
		self.database_connection = sqlite3.connect(database_path)
		self.isConnected = True


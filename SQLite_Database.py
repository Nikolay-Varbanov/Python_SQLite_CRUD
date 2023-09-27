from SQLite_Selector_List import SQLite_Selector_List

class SQLite_Database:
#Utilities
#Constructs
	def __init__(self):
		print("Constructing a SQLite_Database class")
		selector_list: SQLite_Selector_List
	def __del__(self):
		print("Destructuing a SQLite_Database class")
#Facilities
	def OnInit(self):
		print("In SQLite_Database.OnInit()")
		self.selector_list = SQLite_Selector_List()
		self.selector_list.OnInit()


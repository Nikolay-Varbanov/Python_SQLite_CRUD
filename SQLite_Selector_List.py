class SQLite_Selector_List:
	def __init__(self):
		print("Initializing a SQLite_Selector_List class")
		self.selector_list = []
	def __del__(self):
		print("Destructuing a SQLite_Selector_List class")
# Facilities
	def OnInit(self):
		selector_input: str
		selector_input = str(input("Enter a database name to be imported. The name should be without extention. Only aphabetical character allowed. Press Any Non alphabet key to continue") )
		
		if selector_input.isalpha():
			print("Database to be imported is: ", selector_input)
			self.selector_list.append(selector_input)
	def getSelector(self, which: int):
		which = which - 1
		if (which >= 0 or which < len(self.selector_list)) and len(self.selector_list) > 0 :
			return self.selector_list[which]
		else:
			return "NULL"
print("Hey I'm working here!!!")

# python imports

# user imports
from SQLite_Database import SQLite_Database

# globals
#user defined classes
global database
database: SQLite_Database

# variables
global running
running: bool
global engine_input
engine_input: str



def OnInit(): # all initializations are done here
	
	print("In OnInit()")
	# classes
	global database
	database = SQLite_Database()
	database.OnInit()
	# variables
	global running
	running = True
	
	print("Exiting OnInit()")
		
def app():
	print("Entering CRUD_App")

	OnInit()
	
	global running
	global engine_input
	
	while running == True:
		
		print("Engine spinning")

		engine_input = str(input("Enter \exit to exit: "))
	
		match engine_input:
			case "\exit": # exit the app
				print("Engine Command for exit detected")
				running = False
				print("On engine level running is: ", running)
			case _: # this is the default case no engine command found
				print("Non Engine Command detected")

	print("Exiting CRUD_App")


app()
	
# from os import system, name
import importlib
import sys
from datetime import date
from Modules.mainmenufile import userAction, nonOfOptionsChosen
from Modules.newEntry import breakfastLogging
from Modules.showEntries import showEntriesMenu
from Modules.deleteEntries import deleteEntriesMenu
from Modules.editEntries import editOne
import Modules.smallFunctions as smallFuncs
from Modules.fileHandling import fillBreakfastList
from Modules.admin import toggleAdminMode
from Modules.timeFocus import setTimeFocus
from Modules.togglers import toggleDateStamp, toggleForcedOnePerDay

####################################
# start of app
####################################

# global vars

globals = {	'youWantDateStamp':True,
			'oneRecPerDayForced':True,
			'adminModeOn':False,
			'pathToCurrentFile':'',
			'selectedMonth':'',
			'selectedYear':'',
			'mainMenu':{'inputRecs':['1', breakfastLogging],
						'showRecs':['2', showEntriesMenu],
						'editRecs':['3', editOne],
						'deleteRecs':['4', deleteEntriesMenu],
						'dateStampToggle':['d', toggleDateStamp],
						'oneRecPerDayForced':['f', toggleForcedOnePerDay],
						'adminAccess':['a', toggleAdminMode],
						'timeFocus':['s',setTimeFocus],
						'help':'?',
						'exit':'x'}
			}


# Clear screen
smallFuncs.clearScreen()
print(sys.getdefaultencoding())

# populate breakfastList
year = globals['selectedYear'] = date.today().strftime('%Y')
month = globals['selectedMonth'] = date.today().strftime('%m')
breakfastList = fillBreakfastList(year, month)

# MAIN LOOP
loop = True
while loop:
	# global youWantDateStamp
	userChoice = userAction() # menu
	# Needs user input checking
	if userChoice == globals['mainMenu']['inputRecs'][0]:
		globals['mainMenu']['inputRecs'][1](breakfastList, globals['oneRecPerDayForced'], globals['youWantDateStamp'])
	elif userChoice == globals['mainMenu']['showRecs'][0]:
		globals['mainMenu']['showRecs'][1](breakfastList)
	elif userChoice == globals['mainMenu']['editRecs'][0] and globals['adminModeOn']:
		globals['mainMenu']['editRecs'][1](breakfastList) # editOne
	elif userChoice == globals['mainMenu']['deleteRecs'][0] and globals['adminModeOn']:
		globals['mainMenu']['deleteRecs'][1](breakfastList) # deleteEntriesMenu
	elif userChoice == globals['mainMenu']['dateStampToggle'][0] and globals['adminModeOn']:
		globals['mainMenu']['dateStampToggle'][1]() # toggleDateStamp
	elif userChoice == globals['mainMenu']['oneRecPerDayForced'][0] and globals['adminModeOn']:
		globals['mainMenu']['oneRecPerDayForced'][1]() # toggleForcedOnePerDay
	elif userChoice == globals['mainMenu']['adminAccess'][0]:
		globals['mainMenu']['adminAccess'][1]() # toggleAdminMode
	elif userChoice == globals['mainMenu']['timeFocus'][0]:
		globals['mainMenu']['timeFocus'][1]()
	elif userChoice == globals['mainMenu']['help']:
		print(globals)
	elif userChoice == globals['mainMenu']['exit']:
		loop = False # exit program
	else:
		nonOfOptionsChosen()

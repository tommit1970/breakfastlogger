# from os import system, name
import sys
from Modules.mainmenufile import userAction
from Modules.newEntry import breakfastLogging
from Modules.showEntries import showEntriesMenu
from Modules.deleteEntries import deleteEntriesMenu
from Modules.editEntries import editOne
import Modules.smallFunctions as smallFuncs
from Modules.fileHandling import readFile
from Modules.admin import toggleAdminMode
from Modules.togglers import toggleDateStamp, toggleForcedOnePerDay

####################################
# start of app
####################################

# global vars

globals = {	'youWantDateStamp':True,
			'oneRecPerDayForced':True,
			'adminModeOn':False,
			'mainMenu':{'inputRecs':['1', breakfastLogging],
						'showRecs':['2', showEntriesMenu],
						'editRecs':['3', editOne],
						'deleteRecs':['4', deleteEntriesMenu],
						'dateStampToggle':['d', toggleDateStamp],
						'oneRecPerDayForced':['f', toggleForcedOnePerDay],
						'adminAccess':['a', toggleAdminMode],
						'exit':'x'}
			}



youWantDateStamp = True
oneRecPerDayForced = True
adminModeOn = False

# global list
breakfastList = readFile('breakfastDataFile.txt') # The file where the breakfasts are logged

# Clear screen
smallFuncs.clearScreen()
# print(globals)
print(sys.getdefaultencoding())

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
		globals['mainMenu']['editRecs'][1](breakfastList)
	elif userChoice == globals['mainMenu']['deleteRecs'][0] and globals['adminModeOn']:
		globals['mainMenu']['deleteRecs'][1](breakfastList)
	elif userChoice == globals['mainMenu']['dateStampToggle'][0] and globals['adminModeOn']:
		globals['mainMenu']['dateStampToggle'][1]()
	elif userChoice == globals['mainMenu']['oneRecPerDayForced'][0] and globals['adminModeOn']:
		globals['mainMenu']['oneRecPerDayForced'][1]()
	elif userChoice == globals['mainMenu']['adminAccess'][0]:
		globals['mainMenu']['adminAccess'][1]()
	elif userChoice == globals['mainMenu']['exit']:
		loop = False

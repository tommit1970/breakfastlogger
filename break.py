# from os import system, name
import sys
from Modules.mainmenufile import userAction
from Modules.newEntry import breakfastLogging
from Modules.showEntries import showEntriesMenu
from Modules.deleteEntries import deleteEntriesMenu
import Modules.smallFunctions as smallFuncs
from Modules.fileHandling import readFile
from Modules.admin import toggleAdminMode

def toggleDateStamp():
	global youWantDateStamp
	youWantDateStamp = False if youWantDateStamp == True else True # Ternary Operator in Python

def toggleForcedOnePerDay():
	global oneRecPerDayForced
	oneRecPerDayForced = False if oneRecPerDayForced == True else True


####################################
# start of app
####################################

# global vars

globals = {	'youWantDateStamp':True,
			'oneRecPerDayForced':True,
			'adminModeOn':False,
			'mainMenu':{'inputRecs':['1', breakfastLogging],
						'showRecs':['2', showEntriesMenu],
						'deleteRecs':['3', deleteEntriesMenu],
						'dateStampToggle':['d', toggleDateStamp],
						'oneRecPerDayForced':['f', toggleForcedOnePerDay],
						'adminAccess':['a', toggleAdminMode],
						'exit':'x'}
			}



youWantDateStamp = True
oneRecPerDayForced = True
adminModeOn = False

# global list
breakfastList = readFile('log.txt') # The file where the breakfasts are logged

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
		breakfastLogging(breakfastList, oneRecPerDayForced, youWantDateStamp)
	elif userChoice == globals['mainMenu']['showRecs'][0]:
		showEntriesMenu(breakfastList)
	elif userChoice == globals['mainMenu']['deleteRecs'][0] and globals['adminModeOn']:
		deleteEntriesMenu(breakfastList)
	elif userChoice == globals['mainMenu']['dateStampToggle'][0] and globals['adminModeOn']:
		toggleDateStamp()
	elif userChoice == globals['mainMenu']['oneRecPerDayForced'][0] and globals['adminModeOn']:
		toggleForcedOnePerDay()
	elif userChoice == globals['mainMenu']['adminAccess'][0]:
		toggleAdminMode()
	elif userChoice == globals['mainMenu']['exit']:
		loop = False

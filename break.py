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
	global oneRegPerDayForced
	oneRegPerDayForced = False if oneRegPerDayForced == True else True


####################################
# start of app
####################################

# global vars

globals = {	'youWantDateStamp':True,
			'oneRegPerDayForced':True,
			'adminModeOn':False,
			'mainMenu':{'inputRecs':['1',breakfastLogging],
						'showRecs':['2',showEntriesMenu],
						'deleteRecs':['3',deleteEntriesMenu],
						'dateStampToggle':'d',
						'oneRecPerDayForced':'f',
						'adminAccess':'a',
						'exit':'x'}
			}



youWantDateStamp = True
oneRegPerDayForced = True
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
	if userChoice == '1':
		breakfastLogging(breakfastList, oneRegPerDayForced, youWantDateStamp)
	elif userChoice == '2':
		showEntriesMenu(breakfastList)
	elif userChoice == '3' and globals['adminModeOn']:
		deleteEntriesMenu(breakfastList)
	elif userChoice == 'd' and globals['adminModeOn']:
		toggleDateStamp()
	elif userChoice == 'f' and globals['adminModeOn']:
		toggleForcedOnePerDay()
	elif userChoice == 'a':
		toggleAdminMode()
	elif userChoice == 'x':
		loop = False

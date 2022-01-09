# from os import system, name
from Modules.mainmenufile import userAction
from Modules.newEntry import breakfastLogging
from Modules.showAllEntries import showBreakfastLog
from Modules.showOneEntry import showOneBreakfastEntry
from Modules.deleteEntries import deleteBreakfastEntries
import Modules.smallFunctions as smallFuncs
from Modules.fileHandling import writeFile, readFile

def toggleDateStamp():
	global youWantDateStamp
	youWantDateStamp = False if youWantDateStamp == True else True

def toggleForcedOnePerDay():
	global oneRegPerDayForced
	oneRegPerDayForced = False if oneRegPerDayForced == True else True


####################################
# start of app
####################################

# global vars
loop = True
youWantDateStamp = True
oneRegPerDayForced = True

# global list
breakfastList = readFile()

# Clear screen
smallFuncs.clearScreen()

# MAIN LOOP
while loop:
	# global youWantDateStamp
	userchoice = userAction(youWantDateStamp, oneRegPerDayForced) # menu
	# Needs user input checking
	if userchoice == '1':
		breakfastLogging(breakfastList, oneRegPerDayForced, youWantDateStamp,writeFile)
	elif userchoice == '2':
		showBreakfastLog(breakfastList)
	elif userchoice == '3':
		showOneBreakfastEntry(breakfastList)
	elif userchoice == '4':
		deleteBreakfastEntries(breakfastList, writeFile)
	elif userchoice == 'd':
		toggleDateStamp()
	elif userchoice == 'f':
		toggleForcedOnePerDay()
	elif userchoice == 'x':
		loop = False

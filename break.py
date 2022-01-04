# from os import system, name
from Modules.mainmenufile import userAction
from Modules.newEntry import breakfastLogging
from Modules.showAllEntries import showBreakfastLog
from Modules.showOneEntry import showOneBreakfastEntry
from Modules.deleteOneEntry import deleteOneBreakfastEntry
import Modules.smallFunctions as smallFuncs

#Colors ANSI break codes - See file: ansi_colors.txt (only local)


# sub_selectors

# file_handling

def readFile():
	logfileOne = open('log.txt', 'r')
	content = logfileOne.readlines() # from lines in a file to list
	logfileOne.close()
	return content

def writeFile(content):
	logfileOne = open('log.txt','w')
	logfileOne.writelines(content)
	logfileOne.close()


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

smallFuncs.clearScreen()

# main loop
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
		deleteOneBreakfastEntry(breakfastList, writeFile)
	elif userchoice == 'd':
		toggleDateStamp()
	elif userchoice == 'f':
		toggleForcedOnePerDay()
	elif userchoice == 'x':
		loop = False

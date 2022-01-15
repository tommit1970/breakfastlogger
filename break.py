# from os import system, name
import sys
from Modules.mainmenufile import userAction
from Modules.newEntry import breakfastLogging
import Modules.showEntries as show
from Modules.deleteEntries import deleteBreakfastEntries
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
loop = True
youWantDateStamp = True
oneRegPerDayForced = True
adminModeOn = False

# global list
breakfastList = readFile('log.txt')

# Clear screen
smallFuncs.clearScreen()
print(sys.getdefaultencoding())

# MAIN LOOP
while loop:
	# global youWantDateStamp
	userchoice = userAction() # menu
	# Needs user input checking
	if userchoice == '1':
		breakfastLogging(breakfastList, oneRegPerDayForced, youWantDateStamp)
	elif userchoice == '2':
		show.showMenu(breakfastList)
	elif userchoice == '3' and adminModeOn:
		deleteBreakfastEntries(breakfastList)
	elif userchoice == 'd' and adminModeOn:
		toggleDateStamp()
	elif userchoice == 'f' and adminModeOn:
		toggleForcedOnePerDay()
	elif userchoice == 'a':
		toggleAdminMode()
	elif userchoice == 'x':
		loop = False

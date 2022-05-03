# from os import system, name
import importlib
import sys
from datetime import date
from Modules.mainmenufile import menuOptions, nonOfOptionsChosen
from Modules.newEntry import breakfastLogging
from Modules.showEntries import showEntriesMenu
from Modules.deleteEntries import deleteEntriesMenu
from Modules.editEntries import editMenu
import Modules.smallFunctions as smallFuncs
from Modules.fileHandling import fillBreakfastList
from Modules.admin import toggleAdminMode, newPassword
from Modules.timeFocus import setTimeFocus
from Modules.togglers import toggleDateStamp, toggleForcedOnePerDay
from Modules.dbHandling import usersMenu
from Modules.extraDBHandling import whichDB,dbActionMenu
from Modules.car import Car
import multiprocessing as mp
from tkinter import Tk, ttk

####################################
# start of app
####################################

# global vars

globals = {	'youWantDateStamp':True,
			'oneRecPerDayForced':True,
			'adminModeOn':False,
			'pathToPresentFile':'',
			'presentYear':'',
			'presentMonth':'',
			'pathToCurrentFile':'',
			'selectedYear':'',
			'selectedMonth':'',
			'dbTypeActive':'local',
			'lastEntryDateFile':'./DataFolder/lastEntryDate.txt',
			'dbAddressActive':'mongodb://localhost:27017',
			'dbAddressLocal':'mongodb://localhost:27017',
			'dbAddressCloud':'mongodb+srv://user:user@cluster0.itadr.mongodb.net/breakfast?retryWrites=true&w=majority',
			'mainMenu':{'inputRecs':{'key':'1',
									'func':breakfastLogging},
						'showRecs':{'key':'2',
									'func':showEntriesMenu},
						'editRecs':{'key':'3',
									'func':editMenu},
						'deleteRecs':{'key':'4',
									'func':deleteEntriesMenu},
						'dateStampToggle':{'key':'d',
									'func':toggleDateStamp},
						'oneRecPerDayForced':{'key':'f',
									'func':toggleForcedOnePerDay},
						'adminAccess':{'key':'a',
									'func':toggleAdminMode},
						'userActions':{'key':'u',
									'func':usersMenu},
						'mongodb':	{'key':'m',
									'func':whichDB},
						'dbActions':{'key':'b',
									'func':dbActionMenu},
						'timeFocus':{'key':'s',
									'func':setTimeFocus},
						'help':'?',
						'exit':'x'}
			}


# Clear screen
smallFuncs.clearScreen()
print(sys.getdefaultencoding())
# populate breakfastList
year = globals['selectedYear'] = globals['presentYear'] = date.today().strftime('%Y')
month = globals['selectedMonth'] = globals['presentMonth'] = date.today().strftime('%m')
globals['pathToPresentFile'] = './DataFolder/{}/{}-{}_breakfastDataFile.txt'.format(year,year,month)
breakfastList = fillBreakfastList(year, month) # globals['pathToCurrentFile'] will be filled here

# MAIN LOOP
def mainFunc():
	loop = True
	while loop:
		# global youWantDateStamp
		userChoice = menuOptions() # menu
		# Needs user input checking
		if userChoice == globals['mainMenu']['inputRecs']['key']:
			globals['mainMenu']['inputRecs']['func'](breakfastList, globals['oneRecPerDayForced'], globals['youWantDateStamp'])
		elif userChoice == globals['mainMenu']['showRecs']['key']:
			globals['mainMenu']['showRecs']['func'](breakfastList)
		elif userChoice == globals['mainMenu']['editRecs']['key'] and globals['adminModeOn']:
			globals['mainMenu']['editRecs']['func'](breakfastList) # editOne
		elif userChoice == globals['mainMenu']['deleteRecs']['key'] and globals['adminModeOn']:
			globals['mainMenu']['deleteRecs']['func'](breakfastList) # deleteEntriesMenu
		elif userChoice == globals['mainMenu']['dateStampToggle']['key'] and globals['adminModeOn']:
			globals['mainMenu']['dateStampToggle']['func']() # toggleDateStamp
		elif userChoice == globals['mainMenu']['oneRecPerDayForced']['key'] and globals['adminModeOn']:
			globals['mainMenu']['oneRecPerDayForced']['func']() # toggleForcedOnePerDay
		elif userChoice == globals['mainMenu']['adminAccess']['key']:
			globals['mainMenu']['adminAccess']['func']() # toggleAdminMode
		elif userChoice == globals['mainMenu']['userActions']['key'] and globals['adminModeOn']:
			globals['mainMenu']['userActions']['func']() # toggleAdminMode
		elif userChoice == globals['mainMenu']['dbActions']['key'] and globals['adminModeOn']:
			globals['mainMenu']['dbActions']['func']() # do some other mongodb stuff

		elif userChoice == globals['mainMenu']['timeFocus']['key']:
			globals['mainMenu']['timeFocus']['func']()
		elif userChoice == globals['mainMenu']['help']:
			print(globals)
		elif userChoice == globals['mainMenu']['exit']:
			loop = False # exit program
		else:
			nonOfOptionsChosen()



# Create a Window
def createWindow(windowName):
	root = Tk()
	frm = ttk.Frame(root, padding=150)
	frm.grid()
	ttk.Label(frm, text="Hello World!").grid(column=0, row=0)
	ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)
	root.mainloop()

def startApp(carName):
	c = Car(carName)
	c.showName()
	mainFunc()


if __name__ == '__main__':
	startApp('blue')
	# p = mp.Process(target=startApp, args=('blue',))
	# p.start()
	# w.join()

	# createWindow('Tkinter window')



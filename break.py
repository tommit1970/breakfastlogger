from datetime import date
from os import system, name
from Modules.mainmenufile import userAction


#Colors ANSI break codes - See file: ansi_colors.txt (only local)


# sub_selectors

def breakfastLogging():
	today = date.today()
	todayString = today.strftime('%Y - %m - %d')
	lastEntry = breakfastList[len(breakfastList)-1]
	lastEntry = lastEntry.split('->')
	lastEntryDate = lastEntry[0].strip()
	# print(lastEntry)
	# print(lastEntryDate)
	# print(todayString)
	if lastEntryDate == todayString and oneRegPerDayForced:
		print("\033[31;1m",end="") # brightred
		print('\nToday is allready recorded')
		print('Only one entry each day\n')
		print('\u001b[37m', end="") # white
	else:
		breakfastData = input('What did you eat for breakfast today?') + "\n"
		if youWantDateStamp:
			breakfastData = todayString + ' -> ' + breakfastData
		breakfastList.append(breakfastData)
		writeFile(breakfastList) # from list to lines in a file
		print('\n\033[035m',end="") # magenta
		print('Recorded: ',end="")
		print('\n\033[037m',end="") # white
		print(breakfastData)

def showBreakfastLog():
	colorOne = '\u001b[31;1m' # bright red
	normalColor = '\u001b[37m' # white
	clearScreen()
	counter = 0
	for item in breakfastList:
		# each item has a linefeed in the end
		textJunction = '({}{}{}) {}'.format(colorOne,counter,normalColor,item)
		# textJunction = '{}'.format(item)
		print(textJunction, end="")
		counter += 1
	printLines()

def showOneBreakfastEntry():
	loop = True
	while loop:
		listlengthStr = str(len(breakfastList)-1)
		listlength = len(breakfastList)-1
		userChoice = input('Which item(from 0 to ' + listlengthStr + ')?')

		# input check one - number
		if userChoice.isnumeric():
			userNumber = int(userChoice)

			# input check two - range
			if userNumber <= listlength:

				for item in range(5):
						print()
				print(breakfastList[int(userChoice)])
				for item in range(5):
					print()
				loop = False
			else:
				outOfRangeMessage()
		else:
			notANumberMessage()

def deleteOneBreakfastEntry():
	colorOne = '\u001b[31;1m' # bright red
	normalColor = '\u001b[37m' # white
	showBreakfastLog()
	listlength = len(breakfastList)
	print('Which entry do you want to delete?',end="\n\n")
	userChoice = input()
	if userChoice.isnumeric():
		userChoice = int(userChoice)
		if userChoice >= 0 and userChoice < listlength:
			selectedItem = breakfastList[userChoice]
			print("\nRemoved:")
			print('({}{}{}) {}'.format(colorOne,str(userChoice),normalColor,selectedItem))
			del breakfastList[userChoice]
			writeFile(breakfastList)
		else:
			outOfRangeMessage()
	else:
		notANumberMessage()

def printLines(lines = 5):
	for item in range(lines):
		print()

def clearScreen():
	if name == 'nt':
		_ = system('cls') # will clear your screen on nt-systems
	else:
		_ = system('clear') # will clear your screen on mac/linux-systems

def notANumberMessage():
	print("You did not type a number")

def outOfRangeMessage():
	print("You're number is out of range")


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

clearScreen()

# main loop
while loop:
	# global youWantDateStamp
	userchoice = userAction(youWantDateStamp,oneRegPerDayForced) # menu
	# Needs user input checking
	if userchoice == '1':
		breakfastLogging()
	elif userchoice == '2':
		showBreakfastLog()
	elif userchoice == '3':
		showOneBreakfastEntry()
	elif userchoice == '4':
		deleteOneBreakfastEntry()
	elif userchoice == 'd':
		toggleDateStamp()
	elif userchoice == 'f':
		toggleForcedOnePerDay()
	elif userchoice == 'x':
		loop = False





import datetime
from os import system, name

#Colors ANSI break codes
	# 
	# \u001b[31m
	# \u001b[32m
	# \u001b[33m
	# \u001b[34m
	# \u001b[35m
	# \u001b[36m # cyan
	# \u001b[37m # white

# main_menu_selector
def userAction():
	print("\033[0;36m",end="") # cyan
	print('BREAKFAST - LOGGER\n')
	print('\u001b[32m', end="") #
	print('What do you want to do?')
	print("\033[1;37m",end="") # white
	print('1 - Input Recording')
	print('2 - Show Recordings')
	print('3 - Show One Recording')
	print('d - Toggle DateStamp - Now: {}'.format(dateStamp))
	print('x - exit')
	return input()

# sub_selectors

def breakfastLogging():
	breakfastData = input('What did you eat for breakfast today?') + "\n"
	if dateStamp:
		date = datetime.datetime.now()
		breakfastData = date.strftime('%c') + ' -> ' + breakfastData
	breakfastList.append(breakfastData)
	writeFile(breakfastList) # from list to lines in a file
	print(breakfastData,' recorded')


def showBreakfastLog():
	clearScreen()
	for item in breakfastList:
		print(item)
	printLines()

def showOneBreakfastItem():
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
				print("You're number is out of range")
		else:
			print("You did not type a number")


def printLines(lines = 5):
	for item in range(lines):
		print()

def clearScreen():
	if name == 'nt':
		_ = system('cls') # will clear your screen on nt-systems
	else:
		_ = system('clear') # will clear your screen on mac/linux-systems



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
	global dateStamp
	if dateStamp == True:
		dateStamp = False
	else:
		dateStamp = True

####################################
# start of app
####################################

# global vars
loop = True
dateStamp = True

# global list
breakfastList = readFile()

clearScreen()

# main loop
while loop:
	userchoice = userAction()
	# Needs user input checking
	if userchoice == '1':
		breakfastLogging()
	elif userchoice == '2':
		showBreakfastLog()
	elif userchoice == '3':
		showOneBreakfastItem()
	elif userchoice == 'd':
		toggleDateStamp()
	elif userchoice == 'x':
		loop = False





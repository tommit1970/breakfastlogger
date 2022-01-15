import Modules.smallFunctions as smallFuncs
import Modules.colors as colors

#Colors ANSI break codes - See file: ansi_colors.txt (only local)

def showAll(breakfastList):
	# smallFuncs.clearScreen()
	counter = 0
	for item in breakfastList:
		# each item has a linefeed in the end
		textJunction = '({}{}{}) {}'.format(colors.brightRed,counter,colors.white,item)
		print(textJunction)
		counter += 1
	smallFuncs.printLines(3)
	return False # loop


def showRange(breakfastList):
	# pass
	pass

def showOne(breakfastList):
	loop = True
	while loop:
		listlengthStr = str(len(breakfastList)-1)
		listlength = len(breakfastList)-1
		print('Which item(from 0 to ' + listlengthStr + ')? (x to abort)\n')
		userChoice = input()
		if userChoice == 'x':
			loop = False
		else:
			# input check one - number
			if userChoice.isnumeric():
				userNumber = int(userChoice)

				# input check two - range
				if userNumber <= listlength:

					smallFuncs.printLines(2)
					textJunction = '({}{}{}) {}'.format(colors.brightRed,userChoice,colors.white,breakfastList[userNumber])
					print(textJunction)
					smallFuncs.printLines(2)
					return False # loop
				else:
					smallFuncs.outOfRangeMessage()
			else:
				smallFuncs.notANumberMessage()


def showMenu(breakfastList):
	loop = True
	while loop:

		print('Do you want to show (a)ll, (r)ange or (1) entry? (x to abort)')
		userChoice = input()
		if userChoice == 'a':
			loop = showAll(breakfastList)
		elif userChoice == 'r':
			loop = showRange(breakfastList)
		elif userChoice == '1':
			loop = showOne(breakfastList)
		elif userChoice == 'x':
			loop = False


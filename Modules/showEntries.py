import Modules.smallFunctions as smallFuncs
# from Modules.smallFunctions import numberAndRangeCheck
import Modules.colors as colors

#Colors ANSI break codes - See file: ansi_colors.txt (only local)

def handleRangeShow(firstIndex, lastIndex, breakfastList):
	if lastIndex - firstIndex < 0:
		# lastIndex is First Index
		temp = firstIndex
		firstIndex = lastIndex
		lastIndex = temp

	print('Range is {} to {}'.format(firstIndex, lastIndex))
	counter = firstIndex
	for item in range(firstIndex,lastIndex+1):
		# each item has a linefeed in the end
		textJunction = '({}{}{}) {}'.format(colors.brightRed,counter,colors.white,breakfastList[item])
		print(textJunction)
		counter += 1
	smallFuncs.printLines(3)
	return False # loop


def showAll(breakfastList):
	# smallFuncs.clearScreen()
	counter = 0
	for item in breakfastList:
		# each item has a linefeed in the end
		textJunction = '({}{}{}) {}'.format(colors.brightRed,counter,colors.white,item)
		print(textJunction)
		counter += 1
	smallFuncs.printLines(3)
	return False


def showRange(breakfastList):
	loop = True
	print('Show a range')

	firstIndex = lastIndex = 0

	# Get first index
	firstInputOK = False

	while not firstInputOK:
		print('Which is your first entry(index) to show in range? (x to abort)', end="\n\n")
		userChoice = input()
		if userChoice == 'x':
			loop = False
			firstInputOK = True
			print('Aborted!!!')

		else:
			message = smallFuncs.numberAndRangeCheck(breakfastList,userChoice)
			if isinstance(message, bool):
				firstIndex = int(userChoice)
				firstInputOK = True
			else:
				print(message)

	if loop: # not aborted
		
		# Get last index
		lastInputOK = False

		while not lastInputOK:
			print('Which is your last entry(index) to show in range? (x to abort)', end="\n\n")
			userChoice = input()
			if userChoice == 'x':
				loop = False
				lastInputOK = True
				print('Aborted!!!')
			else:
				message = smallFuncs.numberAndRangeCheck(breakfastList,userChoice)
				if isinstance(message, bool):
					lastIndex = int(userChoice)
					lastInputOK = True
					handleRangeShow(firstIndex, lastIndex, breakfastList)
					loop = False
				else:
					print(message)

def showOne(breakfastList):
	loop = True
	while loop:
		listlengthStr = str(len(breakfastList)-1)
		listlength = len(breakfastList)-1
		print('Which item do you want to show(0 to {})? (x to abort)\n'.format(listlengthStr))
		userChoice = input()
		if userChoice == 'x':
			loop = False
		else:
			message = smallFuncs.numberAndRangeCheck(breakfastList,userChoice)
			if isinstance(message, bool): # Checks if message is a boolean value
				# show entry at index userChoice
				textJunction = "\n({}{}{}) {}".format(colors.brightRed,userChoice,colors.white,breakfastList[int(userChoice)])
				print(textJunction, end="\n\n")
				loop = False # exit loop
			else:
				print(message) # notNumber or outOfRange

def showEntriesMenu(breakfastList):
	if len(breakfastList) != 0:
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
	else:
		smallFuncs.nothingToShow()


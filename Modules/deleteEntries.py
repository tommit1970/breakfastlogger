from Modules.showEntries import showAll
import Modules.smallFunctions as smallFuncs
from Modules.fileHandling import writeFile, readFile
import Modules.colors as colors

#Colors ANSI break codes - See file: ansi_colors.txt and Modules/colors.py


def handleRangeDeletion(firstIndex, lastIndex, breakfastList):
	# code goes here
	print('Range is {} to {}'.format(firstIndex, lastIndex))
	if lastIndex - firstIndex < 0:
		entriesToBeRemoved = firstIndex - lastIndex + 1
		# lastIndex is First Index
		firstIndex = lastIndex
		# print('Range is {}'.format(entriesToBeRemoved))
	elif lastIndex - firstIndex > 0:
		entriesToBeRemoved = lastIndex - firstIndex + 1
		#firstIndex is First Index
		# print('Range is {}'.format(entriesToBeRemoved))
	else: # firstIndex = lastIndex
		entriesToBeRemoved = 1
		#firstIndex is also First Index
		# print('Range is {}'.format(entriesToBeRemoved))

	# print('FirstIndex = {}'.format(firstIndex))

	for index in range(entriesToBeRemoved):
		print('\n{}Removed:{}'.format(colors.brightRed, colors.white))
		# firstIndex + index will show former index of deleted entry - the list will shrink on each deletion
		print('({}{}{}) {}\n\n'.format(colors.brightRed,str(firstIndex+index),colors.white,breakfastList[firstIndex]))
		del breakfastList[firstIndex]

	writeFile()

def deleteRange(breakfastList):
	loop = True
	print('Delete a range')

	firstIndex = lastIndex = 0

	# Get first index
	firstInputNotOK = True

	while firstInputNotOK:
		print('Which is your first entry(index) to remove from range? (x to abort)', end="\n\n")
		userChoice = input()
		if userChoice == 'x':
			loop = False
			firstInputNotOK = False
			print('Aborted!!!')

		else:
			if userChoice.isnumeric():
				userChoice = int(userChoice)
				listlength = len(breakfastList)
				if userChoice >= 0 and userChoice < listlength:
					firstIndex = userChoice
					firstInputNotOK = False
				else:
					smallFuncs.outOfRangeMessage()
			else:
				smallFuncs.notANumberMessage()

	if loop: # not aborted
		
		# Get last index
		lastInputNotOK = True

		while lastInputNotOK:
			print('Which is your last entry(index) to remove from range? (x to abort)', end="\n\n")
			userChoice = input()
			if userChoice == 'x':
				loop = False
				lastInputNotOK = False
				print('RangeDeletion part 2 aborted!!!')
			else:
				if userChoice.isnumeric():
					userChoice = int(userChoice)
					listlength = len(breakfastList)
					if userChoice >= 0 and userChoice < listlength:
						lastIndex = userChoice
						lastInputNotOK = False
					else:
						smallFuncs.outOfRangeMessage()
				else:
					smallFuncs.notANumberMessage()

				handleRangeDeletion(firstIndex, lastIndex, breakfastList)
				loop = False


def deleteOne(breakfastList):
	loop = True
	while loop:
		print('You chose Delete One Entry')
		listlength = len(breakfastList)
		print('Which entry do you want to delete? (x to abort)',end="\n\n")
		userChoice = input()
		if userChoice == 'x':
			loop = False
			print('Aborted!!!')
		else:
			if userChoice.isnumeric():
				userChoice = int(userChoice)
				if userChoice >= 0 and userChoice < listlength:
					selectedItem = breakfastList[userChoice]
					print('\n{}Removed:{}'.format(colors.brightRed, colors.white))
					print('({}{}{}) {}\n'.format(colors.brightRed,str(userChoice),colors.white,selectedItem))
					del breakfastList[userChoice]
					writeFile()
					loop = False
				else:
					smallFuncs.outOfRangeMessage()
			else:
				smallFuncs.notANumberMessage()


def deleteEntriesMenu(breakfastList):
	loop = True
	while loop:

		print('Do you want to delete a (r)ange or (1) entry? (x to abort)')
		userChoice = input()
		if userChoice == 'r':
			loop = deleteRange(breakfastList)
		elif userChoice == '1':
			loop = deleteOne(breakfastList)
		elif userChoice == 'x':
			loop = False
		else:
			print('Please choose "1", "r" or "x"')

from Modules.showEntries import showAll
from Modules.fileHandling import writeFile
import Modules.colors as colors
from Modules.smallFunctions import numberAndRangeCheck

#Colors ANSI break codes - See file: ansi_colors.txt and Modules/colors.py


def handleRangeDeletion(firstIndex, lastIndex, breakfastList):
	# code goes here
	print('Range is {} to {}'.format(firstIndex, lastIndex))
	if lastIndex - firstIndex < 0: # lastIndex is lower than firstIndex
		entriesToBeRemoved = firstIndex - lastIndex + 1
		firstIndex = lastIndex
	elif lastIndex - firstIndex > 0:
		entriesToBeRemoved = lastIndex - firstIndex + 1
	else: # firstIndex = lastIndex
		entriesToBeRemoved = 1

	changes = ""

	for index in range(entriesToBeRemoved):
		print('\n{}Removed:{}'.format(colors.brightRed, colors.white))
		# firstIndex + index will show former index of deleted entry - the list will shrink on each deletion
		print('({}{}{}) {}\n\n'.format(colors.brightRed,str(firstIndex+index),colors.white,breakfastList[firstIndex]))

		# appended to log.txt
		if changes == '':
			changes = breakfastList[firstIndex]
		else:
			changes = changes + '\n' + breakfastList[firstIndex]
		del breakfastList[firstIndex]

	changes = 'Removed\n' + changes
	writeFile(changes)

def deleteRange(breakfastList):
	loop = True
	print('Delete a range')

	firstIndex = lastIndex = 0

	# Get first index
	firstInputOK = False

	while not firstInputOK:
		print('Which is your first entry(index) to remove from range? (x to abort)', end="\n\n")
		userChoice = input()
		if userChoice == 'x':
			loop = False
			firstInputOK = True
			print('Aborted!!!')

		else:
			message = numberAndRangeCheck(breakfastList, userChoice)
			if isinstance(message, bool):
				userChoice = int(userChoice)
				firstIndex = userChoice
				firstInputOK = True
			else:
				print(message)

	if loop: # not aborted
		
		# Get last index
		lastInputOK = False

		while not lastInputOK:
			print('Which is your last entry(index) to remove from range? (x to abort)', end="\n\n")
			userChoice = input()
			if userChoice == 'x':
				loop = False
				lastInputOK = True
				print('Aborted!!!')
			else:
				message = numberAndRangeCheck(breakfastList, userChoice)
				if isinstance(message, bool):
					userChoice = int(userChoice)
					lastIndex = userChoice
					lastInputOK = True
					handleRangeDeletion(firstIndex, lastIndex, breakfastList)
					loop = False
				else:
					print(message)



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
			message = numberAndRangeCheck(breakfastList, userChoice)
			if isinstance(message, bool):
				userChoice = int(userChoice)
				selectedItem = breakfastList[userChoice]
				print('\n{}Removed:{}'.format(colors.brightRed, colors.white))
				print('({}{}{}) {}\n'.format(colors.brightRed,str(userChoice),colors.white,selectedItem))
				
				#appended to log.txt
				changes = "Removed\n" + breakfastList[userChoice]
				
				del breakfastList[userChoice]
				writeFile(changes)
				loop = False
			else:
				print(message)


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

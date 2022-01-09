from Modules.showAllEntries import showBreakfastLog
import Modules.smallFunctions as smallFuncs

#Colors ANSI break codes - See file: ansi_colors.txt (only local)

colorOne = '\u001b[31;1m' # bright red
normalColor = '\u001b[37m' # white

def handleRangeDeletion(firstIndex, lastIndex):
	# code goes here
	print('Range is {} to {}'.format(firstIndex, lastIndex))
	if lastIndex - firstIndex < 0:
		diff = firstIndex - lastIndex + 1
		# lastIndex is First Index
		firstIndex = lastIndex
		print('Range is {}'.format(diff))
	elif lastIndex - firstIndex > 0:
		diff = lastIndex - firstIndex + 1
		#firstIndex is First Index
		print('Range is {}'.format(diff))
	else: # firstIndex = lastIndex
		diff = 1
		#firstIndex is also First Index
		print('Range is {}'.format(diff))

	print('FirstIndex = {}'.format(firstIndex))

	for index in range(diff):
		print("\nRemoved:")
		# firstIndex + index will show former index of deleted entry - the list will shrink on each deletion
		print('({}{}{}) {}'.format(colorOne,str(firstIndex+index),normalColor,breakfastList[firstIndex]))
		del breakfastList[firstIndex]

	writeFile(breakfastList)

	loop = False


def deleteBreakfastEntries(breakfastList, writeFile):
	# while loop waiting for 1, r or x
	loop = True
	
	
	while loop:
		print('Do you want to delete\none entry(1) or\na range(r),\n(x to abort)?')
		userChoice = input()
		if userChoice == '1':
			showBreakfastLog(breakfastList)
			
			loop = True

			while loop:
				print('You chose Delete One Entry')
				listlength = len(breakfastList)
				print('Which entry do you want to delete? (x to abort)',end="\n\n")
				userChoice = input()
				if userChoice == 'x':
					loop = False
					print('One Deletion aborted!!!')
				else:
					if userChoice.isnumeric():
						userChoice = int(userChoice)
						if userChoice >= 0 and userChoice < listlength:
							selectedItem = breakfastList[userChoice]
							print("\nRemoved:")
							print('({}{}{}) {}'.format(colorOne,str(userChoice),normalColor,selectedItem))
							del breakfastList[userChoice]
							writeFile(breakfastList)
							loop = False
						else:
							smallFuncs.outOfRangeMessage()
					else:
						smallFuncs.notANumberMessage()

		elif userChoice == 'r':
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
					print('RangeDeletion part 1 aborted!!!')

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

						handleRangeDeletion(firstIndex, lastIndex)


		elif userChoice == 'x':
			loop = False
		else:
			print('Please choose "1", "r" or "x"')
			
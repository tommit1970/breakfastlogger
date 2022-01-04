import Modules.smallFunctions as smallFuncs

def showOneBreakfastEntry(breakfastList):
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
				smallFuncs.outOfRangeMessage()
		else:
			smallFuncs.notANumberMessage()
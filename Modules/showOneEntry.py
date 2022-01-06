import Modules.smallFunctions as smallFuncs

#Colors ANSI break codes - See file: ansi_colors.txt (only local)

def showOneBreakfastEntry(breakfastList):
	colorOne = '\u001b[31;1m' # bright red
	normalColor = '\u001b[37m' # white
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

				smallFuncs.printLines(2)
				textJunction = '({}{}{}) {}'.format(colorOne,userChoice,normalColor,breakfastList[userNumber])
				print(textJunction)
				smallFuncs.printLines(2)
				loop = False
			else:
				smallFuncs.outOfRangeMessage()
		else:
			smallFuncs.notANumberMessage()
import Modules.smallFunctions as smallFuncs
import Modules.colors as colors

#Colors ANSI break codes - See file: ansi_colors.txt (only local)

def showOneBreakfastEntry(breakfastList):
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
					loop = False
				else:
					smallFuncs.outOfRangeMessage()
			else:
				smallFuncs.notANumberMessage()
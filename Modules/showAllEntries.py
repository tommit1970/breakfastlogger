import Modules.smallFunctions as smallFuncs

#Colors ANSI break codes - See file: ansi_colors.txt (only local)

def showBreakfastLog(breakfastList):
	colorOne = '\u001b[31;1m' # bright red
	normalColor = '\u001b[37m' # white
	smallFuncs.clearScreen()
	counter = 0
	for item in breakfastList:
		# each item has a linefeed in the end
		textJunction = '({}{}{}) {}'.format(colorOne,counter,normalColor,item)
		# textJunction = '{}'.format(item)
		print(textJunction, end="")
		counter += 1
	smallFuncs.printLines(3)
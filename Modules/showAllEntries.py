import Modules.smallFunctions as smallFuncs
import Modules.colors as colors

#Colors ANSI break codes - See file: ansi_colors.txt (only local)

def showBreakfastLog(breakfastList):
	# smallFuncs.clearScreen()
	counter = 0
	for item in breakfastList:
		# each item has a linefeed in the end
		textJunction = '({}{}{}) {}'.format(colors.brightRed,counter,colors.white,item)
		print(textJunction)
		counter += 1
	smallFuncs.printLines(3)
from Modules.showAllEntries import showBreakfastLog
import Modules.smallFunctions as smallFuncs


def deleteOneBreakfastEntry(breakfastList, writeFile):
	colorOne = '\u001b[31;1m' # bright red
	normalColor = '\u001b[37m' # white
	showBreakfastLog(breakfastList)
	listlength = len(breakfastList)
	print('Which entry do you want to delete?',end="\n\n")
	userChoice = input()
	if userChoice.isnumeric():
		userChoice = int(userChoice)
		if userChoice >= 0 and userChoice < listlength:
			selectedItem = breakfastList[userChoice]
			print("\nRemoved:")
			print('({}{}{}) {}'.format(colorOne,str(userChoice),normalColor,selectedItem))
			del breakfastList[userChoice]
			writeFile(breakfastList)
		else:
			smallFuncs.outOfRangeMessage()
	else:
		smallFuncs.notANumberMessage()
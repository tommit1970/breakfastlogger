import __main__ as main
from Modules.fileHandling import fillBreakfastList


def setTimeFocus():
	print('\n\nWhat year? ', end="")
	year = main.globals['selectedYear'] = input()
	print('What month? ', end="")
	month = main.globals['selectedMonth'] = input()
	fileLoc = main.globals['pathToCurrentFile'] = './DataFolder/{}/{}/breakfastDataFile.txt'.format(year,month)
	print(fileLoc)
	main.breakfastList = fillBreakfastList(year, month)



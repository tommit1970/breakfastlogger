import __main__ as main
from Modules.fileHandling import fillBreakfastList


def setTimeFocus():
	loop = True
	while loop:
		print('\n\nWhat year? (x to abort)', end="")
		userChoice = input()
		if userChoice == 'x':
			return
		# check if userChoice(year) is a number is equal to or more than 2020
		if userChoice.isnumeric():
			userChoice = int(userChoice)
			if userChoice >= 2020:
				year = str(userChoice)
				while loop:
					print('What month? (x to abort)', end="")
					userChoice = input()
					if userChoice == 'x':
						return
					if userChoice.isnumeric():
						userChoice = int(userChoice)
						if userChoice >= 1 and userChoice <= 12:
							main.globals['selectedYear'] = year
							month = userChoice
							if month < 10:
								month = '0'+str(month)
							else:
								month = str(month)
							main.globals['selectedMonth'] = month
							fileLoc = main.globals['pathToCurrentFile'] = './DataFolder/{}/{}-{}_breakfastDataFile.txt'.format(year,year,month)
							print(fileLoc)
							main.breakfastList = fillBreakfastList(year, month)
							return
						else:
							print('Pick a month from 1 to 12 please!')
					else:
						print('Please write a month number! (01 = January, etc.)')
			else:
				print('Your year is not accessible!')
		else:
			print('Please input a number!')



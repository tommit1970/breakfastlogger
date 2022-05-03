import datetime
from Modules.showEntries import showAll
from Modules.fileHandling import writeFile
import Modules.colors as colors
from Modules.smallFunctions import numberAndRangeCheck
import __main__ as main

def editingEntry(breakfastList, userChoice):
	# feedback preparations
	oldValue = selectedItem = breakfastList[userChoice]
	selectedItem = selectedItem.split('->')
	selectedItemDate = selectedItem[0].strip()
	selectedItemValue = selectedItem[1].strip()

	# feedback before edit
	textJunction = '{}Old value is:{} {}'.format(colors.brightRed, colors.white, selectedItemValue)
	print(textJunction)
	textJunction = '{}Date is:{} {}\n'.format(colors.magenta,colors.white,selectedItemDate)
	print(textJunction)
	print('{}What is the new value?{}'.format(colors.cyan, colors.white), end='\n\n')
	newValue = input()
	print()

	#value handling to breakfastList and YEAR-MONTH_breakfastDataFile.txt
	newValue = selectedItemDate + ' -> ' + newValue
	breakfastList.insert(userChoice, newValue) # insert new value
	changes = "From\n" + oldValue + '\nto\n' + newValue
	del breakfastList[userChoice+1] # remove old value
	writeFile("Edited",changes, False)

	# feedback after edit
	print('\n{}Edited:{}'.format(colors.green, colors.white))
	print('({}{}{}) {}\n'.format(colors.brightRed,str(userChoice),colors.white,newValue))

def validDate(year, month, day):
	isValidDateFeedback = True
	try:
	    datetime.datetime(year, month, day)
	except ValueError:
	    isValidDateFeedback = False

	return isValidDateFeedback


def insertEntry(breakfastList, position):
	# check date on pos and date before, is there a gap more than 1 in days
	# if gap allow insert, else tell no gap
	# insert in 
	# save breakfastDataFile

	prevDayOfMonthEntry = int(breakfastList[position-1].split('->')[0].split('-')[2].strip())

	dayOfMonthEntry = int(breakfastList[position].split('->')[0].split('-')[2].strip())
	year = int(breakfastList[position].split('->')[0].split('-')[0].strip())
	month = int(breakfastList[position].split('->')[0].split('-')[1].strip())
	
	gap = dayOfMonthEntry - prevDayOfMonthEntry - 1

	# unneccessary ??
	# if datetime.date.today() < datetime.date(int(main.globals['selectedYear']), int(main.globals['selectedMonth']), dayOfMonthEntry):
	# 	print('You can not log future breakfasts')
	# else:
	# 	print('Your breakfast can be inserted if it is passes this functions testing')

	# neccessary
	if position == 0: # front edge check
		# check if date is more than the first
		if dayOfMonthEntry > 1: # date, not posistion
			print('Insert possible, gapsize:', gap)
			insertBreakfastData(year, month, prevDayOfMonthEntry, position, gap)
		else:
			print('No gap in beginning of list')

	elif position > 0 and position < 28: # middle check 2-28
		if gap == 0:
			print('No gap at pos:', position, end="\n\n")
		else:
			print('Gap is:', gap)
			insertBreakfastData(year, month, prevDayOfMonthEntry, position, gap)
	elif position > 27: # dependes on the month and year, jan 31, feb 28/29, march 31, april 30, etc.
		# check for last date of current month
		if isValidDateFeedback(year, month, dayOfMonthEntry):
			print('Date is valid')
			insertBreakfastData(year, month, prevDayOfMonthEntry, position, gap)
		else:
			print('Date is invalid')


def chooseDay(year,month,prevDayOfMonthEntry,gap):
	if gap > 1:
		while True:
			print('Which day({}0-{}{})? (x to abort)'.format(colors.brightRed,gap-1,colors.white))
			for i in range(gap):
				print('({}{}{}){} - {} - {}'.format(colors.brightRed,i,colors.white,year,month,prevDayOfMonthEntry+1+i))
			userChoice = input()
			if userChoice == 'x':
				return False
			if userChoice.isnumeric():
				userChoice = int(userChoice)
				if userChoice < gap-1 and userChoice > -1: # in gap range
					# do stuff
					return datetime.date(year, month, prevDayOfMonthEntry+1+userChoice).strftime('%Y - %m - %d')
					# return "{} - {} - {}".format(year,month,prevDayOfMonthEntry+1+userChoice)
				else:
					print('Your number is out of range')
			else:
				print('Please enter a number')
	else:
		return datetime.date(year, month, prevDayOfMonthEntry+1).strftime('%Y - %m - %d')
		# return "{} - {} - {}".format(year,month,prevDayOfMonthEntry+1)


def insertBreakfastData(year, month, prevDayOfMonthEntry, position, gap):
	choosenDay = chooseDay(year,month,prevDayOfMonthEntry,gap)
	if isinstance(choosenDay, bool):
		return
	print('What did you eat for breakfast {}? (x to abort)\n'.format(choosenDay))
	breakfastData = input()
	if breakfastData == 'x': # abort
		print('No data recorded')
	else:
		if main.globals['youWantDateStamp']:
			breakfastData = choosenDay + ' -> ' + breakfastData
		writeFile("Inserted",breakfastData, position) # save to file
		print('\n{}Recorded:{}{}\n'.format(colors.magenta, colors.white,breakfastData))


def editMenu(breakfastList):
	while True:
		listlength = len(breakfastList)
		print('Do you want to (e)dit or (i)nsert an entry? (x to abort)')
		userChoice = input()
		if userChoice == 'x':
			break
		elif userChoice == 'e':
			showAll(breakfastList)
			print('Which entry do you want to edit? (x to abort)',end="\n\n")
			userChoice = input()
			if userChoice == 'x':
				print('{}\nEdit aborted!!!\n'.format(colors.brightRed))
				break
			else:
				message = numberAndRangeCheck(breakfastList, userChoice)
				if isinstance(message, bool):
					editingEntry(breakfastList, int(userChoice))
					break
				else:
					print(message)
		elif userChoice == 'i':
			while True:
				showAll(breakfastList)
				print('Where do you want to insert entry? (x to abort)')
				userChoice = input()
				if userChoice == 'x':
					print('{}\nInsert aborted!!!\n'.format(colors.brightRed))
					break
				else:
					message = numberAndRangeCheck(breakfastList, userChoice)
					if isinstance(message, bool):
						insertEntry(breakfastList, int(userChoice))
						return
					else:
						print(message)

from datetime import date
import Modules.colors as colors
from Modules.fileHandling import writeFile, readFile
from os import path
import time
import __main__ as main

def breakfastLogging(breakfastList, oneRegPerDayForced, youWantDateStamp):
	# Checking last entry
	todayString = date.today().strftime('%Y - %m - %d')
	length = len(breakfastList)

	todayFile = main.globals['lastEntryDateFile']

	if path.exists(todayFile):
		print('lastEntryDate.txt exists')
	else:
		print('lastEntryDate.txt was created')
		fp = open(todayFile, 'w', encoding='utf-8')
		fp.write('2021 - 12 - 01') # before any savings, start of the Epoch for this App
		fp.close()

	lastEntryDate = readFile(todayFile)
	
	# if last entry date is today and oneRegPerDay is forced go to else
	if lastEntryDate[0] == todayString and oneRegPerDayForced:
		print('\n{}Today is allready recorded'.format(colors.brightRed))
		print('Only one entry each day{}\n'.format(colors.white))
	else:
		print('What did you eat for breakfast today? (x to abort)\n')
		breakfastData = input()
		if breakfastData == 'x': # abort
			print('No data recorded')
		else:
			if youWantDateStamp:
				breakfastData = todayString + ' -> ' + breakfastData
			writeFile("New",breakfastData, False) # save to file, False is the position-parameter for Inserted entries
			print('\n{}Recorded:{}{}\n'.format(colors.magenta, colors.white,breakfastData))

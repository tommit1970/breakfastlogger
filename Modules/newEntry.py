from datetime import date
import Modules.colors as colors

def breakfastLogging(breakfastList, oneRegPerDayForced, youWantDateStamp, writeFile):
	# Checking last entry
	today = date.today()
	todayString = today.strftime('%Y - %m - %d')
	lastEntry = breakfastList[len(breakfastList)-1]
	lastEntry = lastEntry.split('->')
	lastEntryDate = lastEntry[0].strip()

	# if last entry date is today and oneRegPerDay is forced go to else
	if lastEntryDate == todayString and oneRegPerDayForced:
		print('\n{}Today is allready recorded'.format(colors.brightRed))
		print('Only one entry each day{}\n'.format(colors.white))
	else:
		breakfastData = input('What did you eat for breakfast today?') + "\n"
		if youWantDateStamp:
			breakfastData = todayString + ' -> ' + breakfastData
		breakfastList.append(breakfastData)
		writeFile(breakfastList) # from list to lines in a file
		print('{}Recorded:{}'.format(colors.magenta, colors.white),end="")
		print(breakfastData)
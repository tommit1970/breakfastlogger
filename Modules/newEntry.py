from datetime import date

#Colors ANSI break codes - See file: ansi_colors.txt (only local)

def breakfastLogging(breakfastList, oneRegPerDayForced, youWantDateStamp, writeFile):
	today = date.today()
	todayString = today.strftime('%Y - %m - %d')
	lastEntry = breakfastList[len(breakfastList)-1]
	lastEntry = lastEntry.split('->')
	lastEntryDate = lastEntry[0].strip()
	# print(lastEntry)
	# print(lastEntryDate)
	# print(todayString)
	if lastEntryDate == todayString and oneRegPerDayForced:
		print("\033[31;1m",end="") # brightred
		print('\nToday is allready recorded')
		print('Only one entry each day\n')
		print('\u001b[37m', end="") # white
	else:
		breakfastData = input('What did you eat for breakfast today?') + "\n"
		if youWantDateStamp:
			breakfastData = todayString + ' -> ' + breakfastData
		breakfastList.append(breakfastData)
		writeFile(breakfastList) # from list to lines in a file
		print('\n\033[035m',end="") # magenta
		print('Recorded: ',end="")
		print('\n\033[037m',end="") # white
		print(breakfastData)
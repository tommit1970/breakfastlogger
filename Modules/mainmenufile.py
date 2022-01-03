# main_menu_selector
def userAction(youWantDateStamp,oneRegPerDayForced):
	print("\033[36m",end="") # cyan
	print('BREAKFAST - LOGGER\n')
	print('\u001b[32m', end="") # green
	print('What do you want to do?')
	print("\033[37m",end="") # white
	print('1 - Input Recording')
	print('2 - Show Recordings')
	print('3 - Show One Recording')
	print('4 - Delete One Recording')
	print('d - Toggle DateStamp       - Now: ',end="")
	print('\033[35;1m',end="") # magenta
	print('{}'.format(youWantDateStamp))
	print('\u001b[37m',end="") # white
	print('f - Toggle ForcedOnePerDay - Now: ',end="")
	print('\033[35;1m',end="") # magenta
	print('{}'.format(oneRegPerDayForced))
	print('\u001b[37m',end="") # white
	print('x - exit',end="\n\n")
	return input()
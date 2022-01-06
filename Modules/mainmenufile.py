# main_menu_selector
def userAction(youWantDateStamp,oneRegPerDayForced):
	bgColorOne = '\033[41m' # red
	bgColorTwo = '\033[0;37m' # light grey
	cyan = '\033[36m'
	green = '\u001b[32m'
	white = '\u001b[37m'
	magenta = '\u001b[34m'

	textJunction = '{}BREAKFAST - LOGGER\n'.format(cyan)
	print(textJunction)
	textJunction = '{}What do you want to do?'.format(green)
	print(textJunction)
	print(white,end="") # white
	textJunction = '{} 1 {} - Input Recording'.format(bgColorOne, bgColorTwo)
	print(textJunction)
	textJunction = '{} 2 {} - Show Recordings'.format(bgColorOne, bgColorTwo)
	print(textJunction)
	textJunction = '{} 3 {} - Show One Recording'.format(bgColorOne, bgColorTwo)
	print(textJunction)
	textJunction = '{} 4 {} - Delete One Recording'.format(bgColorOne, bgColorTwo)
	print(textJunction)
	textJunction = '{} d {} - Toggle DateStamp - Now: {}{}{}'.format(bgColorOne, bgColorTwo,magenta,youWantDateStamp,white)
	print(textJunction)
	textJunction = '{} f {} - Toggle ForcedOnePerDay - Now: {}{}{}'.format(bgColorOne, bgColorTwo,magenta,oneRegPerDayForced,white)
	print(textJunction)
	textJunction = '{} x {} - Exit'.format(bgColorOne, bgColorTwo)
	print(textJunction)
	print()
	return input()
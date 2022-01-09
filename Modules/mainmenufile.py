import Modules.colors as colors

# main_menu_selector
def userAction(youWantDateStamp,oneRegPerDayForced):
	
	textJunction = '{}BREAKFAST - LOGGER\n'.format(colors.cyan)
	print(textJunction)
	textJunction = '{}What do you want to do?'.format(colors.green)
	print(textJunction)
	print(colors.white,end="")
	textJunction = '{} 1 {} - Input Recording'.format(colors.bgRed, colors.bgLightGrey)
	print(textJunction)
	textJunction = '{} 2 {} - Show Recordings'.format(colors.bgRed, colors.bgLightGrey)
	print(textJunction)
	textJunction = '{} 3 {} - Show One Recording'.format(colors.bgRed, colors.bgLightGrey)
	print(textJunction)
	textJunction = '{} 4 {} - Delete Recordings'.format(colors.bgRed, colors.bgLightGrey)
	print(textJunction)
	textJunction = '{} d {} - Toggle DateStamp - Now: {}{}{}'.format(colors.bgRed, colors.bgLightGrey,colors.magenta,youWantDateStamp,colors.white)
	print(textJunction)
	textJunction = '{} f {} - Toggle ForcedOnePerDay - Now: {}{}{}'.format(colors.bgRed, colors.bgLightGrey,colors.magenta,oneRegPerDayForced,colors.white)
	print(textJunction)
	textJunction = '{} x {} - Exit'.format(colors.bgRed, colors.bgLightGrey)
	print(textJunction)
	print()
	return input()
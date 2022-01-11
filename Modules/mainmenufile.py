import Modules.colors as colors
import __main__ as main



def showMenuRegular():
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


def showMenuAdmin():
	textJunction = '{} 4 {} - Delete Recordings'.format(colors.bgRed, colors.bgLightGrey)
	print(textJunction)
	textJunction = '{} d {} - Toggle DateStamp - Now: {}{}{}'.format(colors.bgRed, colors.bgLightGrey,colors.magenta,main.youWantDateStamp,colors.white)
	print(textJunction)
	textJunction = '{} f {} - Toggle ForcedOnePerDay - Now: {}{}{}'.format(colors.bgRed, colors.bgLightGrey,colors.magenta,main.oneRegPerDayForced,colors.white)
	print(textJunction)


# main_menu_selector
def userAction():
	showMenuRegular()
	if main.adminModeOn:
		showMenuAdmin()
	
	textJunction = '{} a {} - AdminAccess: {}{}{}'.format(colors.bgRed, colors.bgLightGrey, colors.magenta,main.adminModeOn,colors.white)
	print(textJunction)

	textJunction = '{} x {} - Exit'.format(colors.bgRed, colors.bgLightGrey)
	print(textJunction)
	print()
	return input()
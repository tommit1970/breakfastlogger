import Modules.colors as colors
import __main__ as main



def showMenuRegular():
	textJunction = '{}BREAKFAST - LOGGER {}Year: {}{} {}Month: {}{}\n'.format(colors.cyan,colors.magenta,colors.green,main.globals['selectedYear'],colors.magenta, colors.green,main.globals['selectedMonth'])
	print(textJunction)
	textJunction = '{}What do you want to do?'.format(colors.green)
	print(textJunction)
	print(colors.white,end="")
	textJunction = '{} {} {} - Input Recording'.format(colors.bgRed, main.globals['mainMenu']['inputRecs'][0], colors.bgLightGrey)
	print(textJunction)
	textJunction = '{} {} {} - Show Recordings'.format(colors.bgRed, main.globals['mainMenu']['showRecs'][0], colors.bgLightGrey)
	print(textJunction)
	

def showMenuAdmin():
	textJunction = '{} {} {} - Edit Recordings'.format(colors.bgRed, main.globals['mainMenu']['editRecs'][0], colors.bgLightGrey)
	print(textJunction)
	textJunction = '{} {} {} - Delete Recordings'.format(colors.bgRed, main.globals['mainMenu']['deleteRecs'][0], colors.bgLightGrey)
	print(textJunction)
	textJunction = '{} {} {} - Toggle DateStamp - Now: {}{}{}'.format(colors.bgRed, main.globals['mainMenu']['dateStampToggle'][0], colors.bgLightGrey,colors.magenta,main.globals['youWantDateStamp'],colors.white)
	print(textJunction)
	textJunction = '{} {} {} - Toggle ForcedOnePerDay - Now: {}{}{}'.format(colors.bgRed, main.globals['mainMenu']['oneRecPerDayForced'][0], colors.bgLightGrey,colors.magenta,main.globals['oneRecPerDayForced'],colors.white)
	print(textJunction)


def nonOfOptionsChosen():
	textJunction = '{}Please choose from the menu!\n{}'.format(colors.brightRed,colors.white)
	print(textJunction)

# main_menu_selector
def userAction():
	showMenuRegular()
	if main.globals['adminModeOn']:
		showMenuAdmin()
	
	textJunction = '{} {} {} - AdminAccess: {}{}{}'.format(colors.bgRed, main.globals['mainMenu']['adminAccess'][0], colors.bgLightGrey, colors.magenta,main.globals['adminModeOn'],colors.white)
	print(textJunction)

	textJunction = '{} {} {} - Set Time Focus'.format(colors.bgRed, main.globals['mainMenu']['timeFocus'][0], colors.bgLightGrey)
	print(textJunction)

	textJunction = '{} {} {} - Help'.format(colors.bgRed, main.globals['mainMenu']['help'], colors.bgLightGrey)
	print(textJunction)

	textJunction = '{} {} {} - Exit'.format(colors.bgRed, main.globals['mainMenu']['exit'], colors.bgLightGrey)
	print(textJunction)
	print()
	return input()
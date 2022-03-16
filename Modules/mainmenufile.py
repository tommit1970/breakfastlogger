import Modules.colors as colors
import __main__ as main



def showMenuRegularTop():
	textJunction = '{}BREAKFAST - LOGGER'.format(colors.cyan)
	print(textJunction)
	textJunction = '{}What do you want to do?'.format(colors.green)
	print(textJunction)
	print(colors.white,end="")
	textJunction = '{} {} {} - Input Recording'.format(colors.bgRed, main.globals['mainMenu']['inputRecs']['key'], colors.bgLightGrey)
	print(textJunction)
	textJunction = '{} {} {} - Show Recordings'.format(colors.bgRed, main.globals['mainMenu']['showRecs']['key'], colors.bgLightGrey)
	print(textJunction)
	


def showMenuAdmin():
	textJunction = '{} {} {} - Edit Recordings'.format(colors.bgRed, main.globals['mainMenu']['editRecs']['key'], colors.bgLightGrey)
	print(textJunction)
	textJunction = '{} {} {} - Delete Recordings'.format(colors.bgRed, main.globals['mainMenu']['deleteRecs']['key'], colors.bgLightGrey)
	print(textJunction)
	textJunction = '{} {} {} - DateStamp - On: {}{}{}'.format(colors.bgRed, main.globals['mainMenu']['dateStampToggle']['key'], colors.bgLightGrey,colors.magenta,main.globals['youWantDateStamp'],colors.white)
	print(textJunction)
	textJunction = '{} {} {} - ForcedOnePerDay - On: {}{}{}'.format(colors.bgRed, main.globals['mainMenu']['oneRecPerDayForced']['key'], colors.bgLightGrey,colors.magenta,main.globals['oneRecPerDayForced'],colors.white)
	print(textJunction)
	textJunction = '{} {} {} - User Actions'.format(colors.bgRed, main.globals['mainMenu']['userActions']['key'], colors.bgLightGrey)
	print(textJunction)
	textJunction = '{} {} {} - DB Actions'.format(colors.bgRed, main.globals['mainMenu']['dbActions']['key'], colors.bgLightGrey)
	print(textJunction)


def showMenuRegularBottom():
	textJunction = '{} {} {} - AdminAccess: {}{}{}'.format(colors.bgRed, main.globals['mainMenu']['adminAccess']['key'], colors.bgLightGrey, colors.magenta,main.globals['adminModeOn'],colors.white)
	print(textJunction)

	textJunction = '{} {} {} - Set Time Focus  {}Year: {}{} {}Month: {}{}{}'.format(colors.bgRed,main.globals['mainMenu']['timeFocus']['key'],colors.bgLightGrey,colors.magenta,colors.green,main.globals['selectedYear'],colors.magenta, colors.green,main.globals['selectedMonth'],colors.white)
	print(textJunction)

	textJunction = '{} {} {} - Help'.format(colors.bgRed, main.globals['mainMenu']['help'], colors.bgLightGrey)
	print(textJunction)

	textJunction = '{} {} {} - Exit'.format(colors.bgRed, main.globals['mainMenu']['exit'], colors.bgLightGrey)
	print(textJunction)


def nonOfOptionsChosen():
	textJunction = '{}Please choose from the menu!\n{}'.format(colors.brightRed,colors.white)
	print(textJunction)

# main_menu_selector
def menuOptions():
	showMenuRegularTop()

	if main.globals['adminModeOn']:
		showMenuAdmin()

	showMenuRegularBottom()

	print()
	return input()
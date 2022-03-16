from os import system, name
import Modules.colors as colors
import __main__ as main

def printLines(lines = 5):
	for item in range(lines):
		print()

def clearScreen():
	if name == 'nt':
		_ = system('cls') # will clear your screen on nt-systems
	else:
		_ = system('clear') # will clear your screen on mac/linux-systems

# def notANumberMessage():
# 	print()

# def outOfRangeMessage():
# 	print()

def numberAndRangeCheck(breakfastList, inputValue):
	# check if number
	if inputValue.isnumeric():
		inputValue = int(inputValue)
		length = len(breakfastList)
		# check range
		if inputValue >= 0 and inputValue < length:
			# return True if both are good else return errormessage
			return True
		else:
			return "{}You're number is out of range{}".format(colors.brightRed,colors.white)
	else:
		return '{}You did not type a number{}'.format(colors.brightRed,colors.white)


def nothingToShow():
	textJunction = '{}No data recorded in Year: {}{}{} Month: {}{}'.format(colors.brightRed, colors.magenta,main.globals['selectedYear'],colors.brightRed, colors.magenta,main.globals['selectedMonth'])
	print(textJunction)

def abortedFeedback():
	textJunction = '\n{}Aborted!\n'.format(colors.brightRed)
	print(textJunction)

def userNotFoundFeedback():
	textJunction = '\n{}User not found!\n'.format(colors.brightRed)
	print(textJunction)

def userDataModifiedFeedback(type):
	type = type.lower().capitalize()
	textJunction = '\n{}{}{} was modified!\n'.format(colors.brightRed,type,colors.white)
	print(textJunction)

def userCreatedFeedback(user):
	textJunction = '\n{}User {}{}{} was created!\n'.format(colors.white, colors.green, user, colors.white)
	print(textJunction)

def userDeletedFeedback(user):
	textJunction = '\n{}User {}{}{} was deleted!\n'.format(colors.white, colors.brightRed, user, colors.white)
	print(textJunction)

def userExistsFeedback(user):
	textJunction = '\n{}User {}{}{} already exists!\n'.format(colors.white, colors.brightRed, user, colors.white)
	print(textJunction)

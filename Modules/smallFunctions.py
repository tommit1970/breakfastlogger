from os import system, name
import Modules.colors as colors

def printLines(lines = 5):
	for item in range(lines):
		print()

def clearScreen():
	if name == 'nt':
		_ = system('cls') # will clear your screen on nt-systems
	else:
		_ = system('clear') # will clear your screen on mac/linux-systems

def notANumberMessage():
	print('{}You did not type a number{}'.format(colors.brightRed,colors.white))

def outOfRangeMessage():
	print("{}You're number is out of range{}".format(colors.brightRed,colors.white))

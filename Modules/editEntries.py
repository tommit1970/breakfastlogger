from Modules.showEntries import showAll
from Modules.fileHandling import writeFile
import Modules.colors as colors
from Modules.smallFunctions import numberAndRangeCheck

def editingEntry(breakfastList, userChoice):
	# feedback preparations
	selectedItem = breakfastList[userChoice]
	selectedItem = selectedItem.split('->')
	selectedItemDate = selectedItem[0].strip()
	selectedItemValue = selectedItem[1].strip()

	# feedback before edit
	textJunction = '{}Old value is:{} {}'.format(colors.brightRed, colors.white, selectedItemValue)
	print(textJunction)
	textJunction = '{}Date is:{} {}\n'.format(colors.magenta,colors.white,selectedItemDate)
	print(textJunction)
	print('{}What is the new value?{}'.format(colors.cyan, colors.white), end='\n\n')
	newValue = input()
	print()

	#value handling
	newValue = selectedItemDate + ' -> ' + newValue
	breakfastList.insert(userChoice, newValue)
	del breakfastList[userChoice+1]
	writeFile()

	# feedback after edit
	print('\n{}Edited:{}'.format(colors.green, colors.white))
	print('({}{}{}) {}\n'.format(colors.brightRed,str(userChoice),colors.white,newValue))

def editOne(breakfastList):
	loop = True
	while loop:
		listlength = len(breakfastList)
		showAll(breakfastList)
		print('Which entry do you want to edit? (x to abort)',end="\n\n")
		userChoice = input()
		if userChoice == 'x':
			loop = False
			print('Aborted!!!')
		else:
			message = numberAndRangeCheck(breakfastList, userChoice)
			if isinstance(message, bool):
				editingEntry(breakfastList, int(userChoice))
				loop = False
			else:
				print(message)
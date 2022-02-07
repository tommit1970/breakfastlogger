import __main__ as main
# import os
import datetime
from os import path, mkdir

# emtpy file check
def is_non_zero_file(fpath):  
    return path.isfile(fpath) and path.getsize(fpath) > 0


# filling the breakfastList
def fillBreakfastList(year, month):
	# if current time fill with this year and month - file
	# else fill with dateStringYear and dateStringMonth - file

	# check if file exists
	directory = './DataFolder/{}'.format(year)
	file = directory + '/{}-{}_breakfastDataFile.txt'.format(year,month)
	file_exists = path.exists(file)
	if file_exists:
		print(file + ' exists')
	else:
		# check directory year
		if not path.isdir(directory):
			# if no year make year
			mkdir(directory)
			print('{} was created'.format(directory))

		# create the file
		fp = open(file, 'x', encoding='utf-8')
		fp.close()
		print(file +' was created')
	main.globals['pathToCurrentFile'] = file
	return readFile(file)

# reading the file
def readFile(fileName):
	# if fileName == "./DataFolder/today.txt":
		# print('Loaded today.txt')
	print('Loaded {}'.format(fileName))
	file = open(fileName, 'r', encoding='utf-8')
	content = file.read().splitlines() # from lines in a file to list

	file.close()
	return content

def todayFileChange(date):
	file = './DataFolder/today.txt'
	print("Changing {}".format(file))
	todayFile = open(file, 'w', encoding='utf-8')
	todayFile.write(date)
	todayFile.close()


def logChange(changeType,changes):
	# log.txt
	file = 'log.txt'
	logActivityFile = open(file,'a', encoding='utf-8') # a = append
	todayString = datetime.datetime.now()
	todayString = todayString.strftime('%c') # format -> Wed Jan 26 13:23:23 2022
	logChanges = todayString + '\n' + changeType + '\n' + changes

	if is_non_zero_file(file):	# is log.txt empty
		logChanges = '\n' + logChanges # if not empty add a linefeed
	logActivityFile.write(logChanges)
	logActivityFile.close()


# writing to the file
def writeFile(changeType,changes):
	
	logChange(changeType,changes)

	# today.txt
	if changeType == "New":
		todayFileChange(changes.split('->')[0].strip())

	if changeType == 'New' and main.globals['pathToCurrentFile'] != main.globals['pathToPresentFile']:
		breakfastListChanged = True
	else:
		breakfastListChanged = False


	# improve the structure of this function
	# if changeType == 'New':
		# do this
	# elif changeType == 'Edited':
		# do this
	# elif changeType == 'Removed':
		# do this

	# possible subfunctions
		# writing to the file
		# writing changes to the log
		# if changeType == 'New':
			# change today.txt

	# is it a 'New' entry?, if not - it is a timeFocus-change(edit/remove)
	if changeType == "New":
		print('Writing to PresentTimeFile')
		file = main.globals['pathToPresentFile'] # pathToCurrentFile is irrelevant here
		# fill breakfastList with present time list
		main.breakfastList = fillBreakfastList(main.globals['presentYear'],main.globals['presentMonth'])
		main.breakfastList.append(changes) # add to present breakfastList
		print(main.breakfastList)
	else:
		print('Writing to SelectedTimeFile')
		file = main.globals['pathToCurrentFile'] # pathToPresentFile is irrelevant here
	
	# does <year>-<month>_breakfastDataFile.txt exist, if not create it
	file_exists = path.exists(file)
	if file_exists:
		print(file + ' exists')
	else:
		fp = open(file, 'x', encoding='utf-8') # create file
		fp.close()
		print(file +' was created')

	# prepare to write to file
	breakfastDataFile = open(file,'w', encoding='utf-8')
	breakfastListLength = len(main.breakfastList)
	print('Length of breakfastList:' + str(breakfastListLength))
	textCollection = ""
	for i in range(0,breakfastListLength):
		if i < breakfastListLength-1:
			textCollection = textCollection + main.breakfastList[i] + '\n'
		else:
			textCollection = textCollection + main.breakfastList[i]

	# write to file
	print(textCollection)
	breakfastDataFile.write(textCollection)
	breakfastDataFile.close()

	# change back to selected breakfastList from <year>-<month>_breakfastDataFile.txt
	if breakfastListChanged:
		main.breakfastList = fillBreakfastList(main.globals['selectedYear'],main.globals['selectedMonth'])
		print("Changed back to selected breakfastList")
		print(main.breakfastList)




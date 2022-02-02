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
	directory = './DataFolder/{}/{}'.format(year,month)
	file = directory + '/breakfastDataFile.txt'
	print(directory)
	file_exists = path.exists(file)
	if file_exists:
		print(file + ' exists')
	else:
		# check directory year
		yearPath = './DataFolder/{}'.format(year)
		if not path.isdir(yearPath):
			# if no year make year
			mkdir(yearPath)
		# make directory month
		mkdir(directory)

		# create the file
		fp = open(file, 'x', encoding='utf-8')
		fp.close()
		print(file +' was created')
	main.globals['pathToCurrentFile'] = file
	return readFile(file)

# reading the file
def readFile(fileName):
	if fileName == "./DataFolder/today.txt":
		print('Loaded today.txt')

	file = open(fileName, 'r', encoding='utf-8')
	content = file.read().splitlines() # from lines in a file to list

	file.close()
	return content

# writing to the file
def writeFile(changeType,changes):

	# does file exist
	file = main.globals['pathToCurrentFile'] # which file is it
	file_exists = path.exists(file)
	if file_exists:
		print(file + ' exists')
	else:
		fp = open(file, 'x', encoding='utf-8')
		fp.close()
		print(file +' was created')

	# prepare to write to file
	breakfastDataFile = open(main.globals['pathToCurrentFile'],'w', encoding='utf-8')
	breakfastListLength = len(main.breakfastList)
	textCollection = ""
	for i in range(0,breakfastListLength):
		if i < breakfastListLength-1:
			textCollection = textCollection + main.breakfastList[i] + '\n'
		else:
			textCollection = textCollection + main.breakfastList[i]

	# write to file
	breakfastDataFile.write(textCollection)
	breakfastDataFile.close()

	# 
	if changeType == "New":
		print("Changing ./DataFolder/today.txt")
		todayFile = open('./DataFolder/today.txt', 'w', encoding='utf-8')
		todayContent = changes.split('->')[0].strip()
		todayFile.write(todayContent)
		todayFile.close()

	# log changes with date to log.txt
	logActivityFile = open('log.txt','a', encoding='utf-8') # a = append
	todayString = datetime.datetime.now()
	todayString = todayString.strftime('%c')
	changes = todayString + '\n' + changeType + '\n' + changes

	# check if file is empty
	if is_non_zero_file(main.globals['pathToCurrentFile']):
		changes = '\n' + changes # linefeed
	logActivityFile.write(changes)
	logActivityFile.close()

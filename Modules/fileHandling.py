import __main__ as main
import os
import datetime

# emtpy file check
def is_non_zero_file(fpath):  
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0


def readFile(fileName):
	logfileOne = open(fileName, 'r')
	content = logfileOne.read().splitlines() # from lines in a file to list

	logfileOne.close()
	return content

def writeFile(changes):
	breakfastDataFile = open('breakfastDataFile.txt','w')
	breakfastListLength = len(main.breakfastList)
	textCollection = ""
	for i in range(0,breakfastListLength):
		if i < breakfastListLength-1:
			textCollection = textCollection + main.breakfastList[i] + '\n'
		else:
			textCollection = textCollection + main.breakfastList[i]

	# print(textCollection)

	breakfastDataFile.write(textCollection)
	breakfastDataFile.close()


	# log.txt logging changes with date
	logActivityFile = open('log.txt','a')
	todayString = datetime.datetime.now()
	todayString = todayString.strftime('%c')
	
	changes = todayString + '\n' + changes

	# check if file is empty
	if is_non_zero_file('./log.txt'):
		changes = '\n' + changes # linefeed
	logActivityFile.write(changes)
	logActivityFile.close()
